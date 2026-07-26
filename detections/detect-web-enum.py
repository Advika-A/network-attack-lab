import argparse
from pathlib import Path
from collections import Counter
import pyshark


def detect_web_enumeration(pcap_file, threshold, not_found_threshold):
    pcap_path = Path(pcap_file)

    if not pcap_path.exists():
        print(f"[ERROR] PCAP file not found: {pcap_path}")
        return

    print("=" * 60)
    print("Web Application Enumeration Detection")
    print("=" * 60)
    print(f"PCAP File : {pcap_path.name}")
    print(f"GET Request Threshold : {threshold}")
    print(f"HTTP 404 Threshold    : {not_found_threshold}")
    print()

    capture = pyshark.FileCapture(
        str(pcap_path),
        display_filter="http"
    )

    total_get_requests = 0
    unique_paths = set()
    status_counter = Counter()

    source_ip = None
    target_ip = None

    for packet in capture:
        try:
            # HTTP GET Requests
            if hasattr(packet.http, "request_method"):

                if packet.http.request_method == "GET":

                    total_get_requests += 1

                    source_ip = packet.ip.src
                    target_ip = packet.ip.dst

                    if hasattr(packet.http, "request_uri"):
                        unique_paths.add(packet.http.request_uri)

            # HTTP Responses
            elif hasattr(packet.http, "response_code"):

                status_code = packet.http.response_code
                status_counter[status_code] += 1

        except AttributeError:
            continue

    capture.close()

    total_404 = status_counter.get("404", 0)

    suspicious = (
        total_get_requests >= threshold or
        total_404 >= not_found_threshold
    )

    print("Status              : Detection Complete")

    if suspicious:
        print("Detection Verdict   : Potential Web Directory Enumeration")
    else:
        print("Detection Verdict   : No Enumeration Detected")

    print()

    print("Traffic Summary")
    print("-" * 60)
    print(f"Source IP           : {source_ip}")
    print(f"Target IP           : {target_ip}")
    print(f"Total GET Requests  : {total_get_requests}")
    print(f"Unique Paths        : {len(unique_paths)}")
    print(f"HTTP 404 Responses  : {total_404}")
    print()

    print("HTTP Status Code Distribution")
    print("-" * 60)

    if status_counter:
        for code in sorted(status_counter.keys()):
            print(f"{code:<5}: {status_counter[code]}")
    else:
        print("No HTTP responses found.")

    print()
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Detect web directory enumeration activity from a PCAP file."
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
        help="Minimum number of HTTP GET requests before alerting (default: 50)."
    )

    parser.add_argument(
        "-n",
        "--not-found-threshold",
        type=int,
        default=20,
        help="Minimum number of HTTP 404 responses before alerting (default: 20)."
    )

    args = parser.parse_args()

    detect_web_enumeration(
        args.pcap,
        args.threshold,
        args.not_found_threshold
    )


if __name__ == "__main__":
    main()