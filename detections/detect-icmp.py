import argparse
from pathlib import Path
import pyshark


def detect_icmp_echo_requests(pcap_file):
    pcap_path = Path(pcap_file)

    if not pcap_path.exists():
        print(f"[ERROR] PCAP file not found: {pcap_path}")
        return

    print("=" * 60)
    print("ICMP Echo Request Detection")
    print("=" * 60)
    print(f"PCAP File : {pcap_path.name}")
    print()

    capture = pyshark.FileCapture(
        str(pcap_path),
        display_filter="icmp"
    )

    events = []

    for packet in capture:
        try:
            if packet.icmp.type == "8":
                events.append({
                    "time": packet.sniff_time,
                    "src": packet.ip.src,
                    "dst": packet.ip.dst
                })
        except AttributeError:
            continue

    capture.close()

    print(f"Status               : Detection Complete")
    print(f"Echo Requests Found  : {len(events)}")
    print()

    if events:
        print("Detected Events")
        print("-" * 60)

        for index, event in enumerate(events, start=1):
            print(f"[{index}] Time        : {event['time']}")
            print(f"    Source      : {event['src']}")
            print(f"    Destination : {event['dst']}")
            print()

    else:
        print("No ICMP Echo Requests detected.")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Detect ICMP Echo Requests from a PCAP file."
    )

    parser.add_argument(
        "pcap",
        help="Path to the PCAP file"
    )

    args = parser.parse_args()

    detect_icmp_echo_requests(args.pcap)


if __name__ == "__main__":
    main()