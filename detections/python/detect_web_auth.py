import argparse
from pathlib import Path
import pyshark


def detect_web_auth(pcap_file, threshold):
    pcap_path = Path(pcap_file)

    if not pcap_path.exists():
        print(f"[ERROR] PCAP file not found: {pcap_path}")
        return

    print("=" * 60)
    print("Web Authentication Detection")
    print("=" * 60)
    print(f"PCAP File : {pcap_path.name}")
    print(f"Threshold : {threshold} login attempts")
    print()

    capture = pyshark.FileCapture(
        str(pcap_path),
        display_filter="http.request.method == POST"
    )

    sources = {}

    for packet in capture:
        try:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            uri = packet.http.request_uri

            if src_ip not in sources:
                sources[src_ip] = {
                    "target": dst_ip,
                    "endpoint": uri,
                    "attempts": 0
                }

            sources[src_ip]["attempts"] += 1

        except AttributeError:
            continue

    capture.close()

    flagged = []

    for ip, data in sources.items():
        if data["attempts"] >= threshold:
            flagged.append((ip, data))

    print("Status              : Detection Complete")

    if flagged:
        print("Detection Verdict   : Potential Repeated Web Authentication Attempts")
    else:
        print("Detection Verdict   : No Suspicious Authentication Activity")

    print(f"Suspicious Sources  : {len(flagged)}")
    print()

    if flagged:
        print("Detected Sources")
        print("-" * 60)

        for index, (ip, data) in enumerate(flagged, start=1):
            print(f"[{index}]")
            print(f"Source IP       : {ip}")
            print(f"Target IP       : {data['target']}")
            print(f"Login Endpoint  : {data['endpoint']}")
            print(f"POST Requests   : {data['attempts']}")
            print()

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Detect repeated web authentication attempts from a PCAP file."
    )

    parser.add_argument(
        "pcap",
        help="Path to the PCAP file"
    )

    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        default=2,
        help="Minimum number of HTTP POST login requests before alerting (default: 2)."
    )

    args = parser.parse_args()

    detect_web_auth(
        args.pcap,
        args.threshold
    )


if __name__ == "__main__":
    main()