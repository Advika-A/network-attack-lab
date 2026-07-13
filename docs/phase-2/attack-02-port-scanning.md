# Attack 02 – TCP SYN Port Scanning

## Objective

Identify open TCP ports on the target host using a TCP SYN scan while observing the resulting network traffic and understanding how defenders can recognize reconnaissance activity.

---

## Environment

| System | Role | IP Address |
|---------|------|------------|
| Kali Linux | Attacker | 10.0.2.4 |
| Ubuntu | Victim | 10.0.2.15 |

**Network:** VirtualBox NAT Network

---

## Attack Overview

After confirming that a host is reachable, an attacker typically performs port scanning to determine which network services are exposed. The information gathered during this phase helps identify potential attack vectors for later stages of an intrusion.

For this experiment, a TCP SYN scan was performed using Nmap.

---

## Attack Method

### Tool

- Nmap 7.95

### Command

```bash
sudo nmap -sS 10.0.2.15
```

---

## Expected Outcome

Before executing the scan, the listening services on the Ubuntu VM were verified.

Expected externally accessible service:

- TCP Port 80 (HTTP)

Localhost-only services (127.0.0.1) were not expected to be visible from the attacker.

---

## Scan Results

```
Starting Nmap 7.95

Nmap scan report for 10.0.2.15

Host is up (0.0020s latency).

Not shown: 999 closed tcp ports (reset)

PORT   STATE SERVICE
80/tcp open  http
```

The scan successfully identified the HTTP service running on TCP port 80.

---

## Packet Capture

Capture file:

```
captures/phase-2/attack-02/syn_scan.pcap
```

Traffic captured using:

```bash
sudo tcpdump -i eth0 -w syn_scan.pcap
```

---

## Observed Network Artifacts

Observed protocols:

- TCP
- ARP (background)
- DHCP (background)

### Closed Port Behavior

For closed ports:

```
Kali                Ubuntu
SYN -------------->
                <------------- RST, ACK
```

The victim immediately rejected connection attempts to closed ports.

---

### Open Port Behavior

For TCP port 80:

```
Kali                Ubuntu
SYN -------------->
                <------------- SYN, ACK
RST -------------->
```

Instead of completing the TCP three-way handshake, Nmap immediately terminated the connection with a TCP RST packet.

This behavior is characteristic of a TCP SYN (half-open) scan.

---

## Defender Perspective

A network defender would observe:

- A single source probing many destination ports
- Sequential SYN packets
- Numerous RST responses for closed ports
- SYN-ACK response from the HTTP service
- Immediate TCP reset from the scanner

These patterns are strong indicators of reconnaissance activity.

---

## Detection Opportunities

Possible detection indicators include:

- Large number of SYN packets within a short time
- Sequential destination port numbers
- High ratio of failed connection attempts
- Multiple ports probed from the same source IP
- SYN followed immediately by RST

These characteristics make TCP SYN scanning relatively easy to detect using network monitoring tools.

---

## Limitations

A SYN scan identifies open ports but does not reveal:

- Software version
- Service configuration
- Authentication requirements
- Application vulnerabilities

Additional enumeration is required after port discovery.

---

## Key Takeaways

- Port scanning is a common second stage of attacker reconnaissance.
- TCP SYN scans determine port state without completing full TCP connections.
- Closed ports respond with TCP RST packets.
- Open ports respond with TCP SYN-ACK packets.
- The observed packet sequence provides clear evidence of reconnaissance from a defender's perspective.