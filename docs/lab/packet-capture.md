# Packet Capture and Traffic Analysis

## Objective

The objective of packet capture was to establish visibility into network activity within the cyber range and understand how both normal and malicious traffic appear at the packet level.

Captured traffic later served as the primary data source for attack analysis and custom detection development.

---

## Capture Environment

| Component | Details |
|-----------|---------|
| Capture Tool | tcpdump |
| Analysis Tool | Wireshark |
| Network Interface | enp0s3 |
| Capture Format | PCAP |

---

## Packet Capture Procedure

### Identify the active network interface

```bash
ip a
```

### Start live packet capture

```bash
sudo tcpdump -i enp0s3
```

### Save traffic to a PCAP file

```bash
sudo tcpdump -i enp0s3 -w first_capture.pcap
```

---

## Traffic Generation

Normal network activity was generated to observe common protocols within the environment.

Examples included:

```bash
ping google.com
curl example.com
nslookup google.com
```

---

## Packet Observations

The baseline capture contained several common protocols, including:

- ICMP Echo Requests and Replies
- DNS queries and responses
- TCP connection establishment
- HTTPS communication
- TCP acknowledgments

Example packet:

```text
10:39:17.242844 IP Ubuntu.52910 > 151.101.210.49.https: Flags [.], ack 1844731, win 65535, length 0
```

Even when application data is encrypted, packet metadata remains observable, including:

- Source and destination IP addresses
- Protocol type
- Port numbers
- Packet timing
- Connection behavior

This metadata provides valuable context for network monitoring and intrusion detection.

---

## Capture Summary

| Metric | Value |
|---------|------:|
| Duration | 157.95 seconds |
| Packets | 18,738 |
| File Size | 77 MB |
| Average Packet Rate | 118 packets/s |

---

## Key Findings

The baseline capture demonstrated that operating systems continuously generate background network traffic, even during routine operation. This highlights the importance of establishing normal traffic baselines before analyzing attack behavior.

The captured PCAP files also formed the foundation for the attack simulations and detection engineering activities implemented throughout the remainder of the project.

