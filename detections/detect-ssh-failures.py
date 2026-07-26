import argparse
import re
from pathlib import Path


def detect_ssh_failures(log_file, threshold):
    log_path = Path(log_file)

    if not log_path.exists():
        print(f"[ERROR] Log file not found: {log_path}")
        return

    print("=" * 60)
    print("SSH Failed Authentication Detection")
    print("=" * 60)
    print(f"Log File  : {log_path.name}")
    print(f"Threshold : {threshold} failed logins")
    print()

    # Store failed login attempts by source IP
    failed_attempts = {}

    # Regular expression to extract log information
    pattern = re.compile(
        r'^(.*?)\s+.*Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)'
    )

    with open(log_path, "r") as logfile:
        for line in logfile:

            match = pattern.search(line)

            if match:
                timestamp = match.group(1)
                username = match.group(2)
                source_ip = match.group(3)

                if source_ip not in failed_attempts:
                    failed_attempts[source_ip] = {
                        "username": username,
                        "count": 0,
                        "timestamps": []
                    }

                failed_attempts[source_ip]["count"] += 1
                failed_attempts[source_ip]["timestamps"].append(timestamp)

    suspicious = {
        ip: data
        for ip, data in failed_attempts.items()
        if data["count"] >= threshold
    }

    total_failures = sum(data["count"] for data in failed_attempts.values())

    print("Status              : Detection Complete")

    if suspicious:
        print("Detection Verdict   : Potential SSH Brute Force")
    else:
        print("Detection Verdict   : No Suspicious Activity")

    print(f"Failed Logins       : {total_failures}")
    print(f"Suspicious Sources  : {len(suspicious)}")
    print()

    if suspicious:
        print("Detected Sources")
        print("-" * 60)

        for index, (ip, data) in enumerate(suspicious.items(), start=1):

            print(f"[{index}]")
            print(f"Source IP       : {ip}")
            print(f"Username        : {data['username']}")
            print(f"Failed Attempts : {data['count']}")
            print(f"First Attempt   : {data['timestamps'][0]}")
            print(f"Last Attempt    : {data['timestamps'][-1]}")
            print()

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Detect failed SSH authentication attempts from auth.log."
    )

    parser.add_argument(
        "logfile",
        help="Path to auth.log"
    )

    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        default=3,
        help="Minimum failed login attempts before alerting."
    )

    args = parser.parse_args()

    detect_ssh_failures(args.logfile, args.threshold)


if __name__ == "__main__":
    main()