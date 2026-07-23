import argparse
from pathlib import Path
import pyshark


def detect_service_enumeration(pcap_file):
    pcap_path = Path(pcap_file)

    if not pcap_path.exists():
        print(f"[ERROR] PCAP file not found: {pcap_path}")
        return

    print("=" * 60)
    print("HTTP Service Enumeration Detection")
    print("=" * 60)
    print(f"PCAP File : {pcap_path.name}")
    print()

    capture = pyshark.FileCapture(
        str(pcap_path),
        display_filter="http"
    )

    detections = []
    status_counts = {}
    server_headers = set()

    for packet in capture:
        try:
            # Process only HTTP responses
            if hasattr(packet.http, "response_code"):

                server = getattr(packet.http, "server", None)

                if server:
                    status = packet.http.response_code

                    detections.append({
                        "time": packet.sniff_time,
                        "server_ip": packet.ip.src,
                        "client_ip": packet.ip.dst,
                        "status": status,
                        "server": server
                    })

                    server_headers.add(server)
                    status_counts[status] = status_counts.get(status, 0) + 1

        except AttributeError:
            continue

    capture.close()

    print("Status                 : Detection Complete")

    if detections:
        print("Detection Verdict      : Server Information Disclosure Detected")
    else:
        print("Detection Verdict      : No Server Information Disclosure Detected")

    print(f"HTTP Responses         : {len(detections)}")
    print(f"Unique Server Headers  : {len(server_headers)}")
    print()

    if status_counts:
        print("HTTP Status Summary")
        print("-" * 60)

        for code in sorted(status_counts):
            print(f"{code:<3} : {status_counts[code]}")

        print()

    if detections:
        print("Detected Services")
        print("-" * 60)

        for index, event in enumerate(detections, start=1):
            print(f"[{index}]")
            print(f"Time          : {event['time']}")
            print(f"Server IP     : {event['server_ip']}")
            print(f"Client IP     : {event['client_ip']}")
            print(f"HTTP Status   : {event['status']}")
            print(f"Server Header : {event['server']}")
            print()

    else:
        print("No HTTP Server headers detected.")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Detect HTTP service enumeration from a PCAP file."
    )

    parser.add_argument(
        "pcap",
        help="Path to the PCAP file"
    )

    args = parser.parse_args()

    detect_service_enumeration(args.pcap)


if __name__ == "__main__":
    main()