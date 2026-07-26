import argparse
from pathlib import Path
import pyshark


def detect_syn_scan(pcap_file, threshold):
    pcap_path = Path(pcap_file)

    if not pcap_path.exists():
        print(f"[ERROR] PCAP file not found: {pcap_path}")
        return

    print("=" * 60)
    print("TCP SYN Scan Detection")
    print("=" * 60)
    print(f"PCAP File : {pcap_path.name}")
    print(f"Threshold : {threshold} unique ports")
    print()

    capture = pyshark.FileCapture(
        str(pcap_path),
        display_filter="tcp"
    )

    scanners = {}

    for packet in capture:
        try:
            # Detect TCP SYN packets (SYN only)
            if packet.tcp.flags == "0x0002":

                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                dst_port = packet.tcp.dstport

                if src_ip not in scanners:
                    scanners[src_ip] = {
                        "target": dst_ip,
                        "ports": set(),
                        "syn_packets": 0
                    }

                scanners[src_ip]["syn_packets"] += 1
                scanners[src_ip]["ports"].add(dst_port)

        except AttributeError:
            continue

    capture.close()

    flagged = []

    for ip, data in scanners.items():
        if len(data["ports"]) >= threshold:
            flagged.append((ip, data))

    print("Status              : Detection Complete")

    if flagged:
        print("Detection Verdict   : Potential TCP SYN Scan")
    else:
        print("Detection Verdict   : No SYN Scan Detected")

    print(f"Scanners Detected   : {len(flagged)}")
    print()

    if flagged:
        print("Detected Scanner IPs")
        print("-" * 60)

        for index, (ip, data) in enumerate(flagged, start=1):

            sample_ports = sorted(data["ports"], key=int)[:10]

            print(f"[{index}]")
            print(f"Source IP        : {ip}")
            print(f"Target IP        : {data['target']}")
            print(f"Total SYN Packets: {data['syn_packets']}")
            print(f"Unique Ports     : {len(data['ports'])}")
            print(f"Sample Ports     : {', '.join(sample_ports)}")
            print()

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Detect TCP SYN scan activity from a PCAP file."
    )

    parser.add_argument(
        "pcap",
        help="Path to the PCAP file"
    )

    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        default=50,
        help="Minimum number of unique destination ports before alerting (default: 50)."
    )

    args = parser.parse_args()

    detect_syn_scan(args.pcap, args.threshold)


if __name__ == "__main__":
    main()