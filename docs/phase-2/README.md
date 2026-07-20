# Phase 2 — Network Attack Simulation

## Overview

Phase 2 focuses on simulating realistic cyberattacks within a controlled virtual environment to study attacker behavior, observable network traffic, host-level artifacts, and opportunities for defensive monitoring.

All activities were performed in an isolated VirtualBox NAT Network using dedicated attacker and victim virtual machines. Network traffic was captured using `tcpdump` and analyzed with Wireshark. Each attack was documented immediately after execution to preserve observations and evidence.

The objective of this phase is **observation and analysis**, not exploitation.

---

## Lab Environment

| Component | Configuration |
|------------|---------------|
| Attacker | Kali Linux (10.0.2.4) |
| Victim | Ubuntu Server (10.0.2.15) |
| Network | VirtualBox NAT Network |
| Packet Capture | tcpdump |
| Analysis | Wireshark |
| Web Server | Apache HTTP Server |
| Web Application | DVWA |

---

## Lab Architecture

The following diagram illustrates the cyber range used throughout Phase 2.

![Lab Architecture](../../diagrams/phase-2-attack-workflow.png)
![Lab Architecture](../../diagrams/lab-architecture.png)

---

## Attack Progression

The attacks were intentionally designed to follow the reconnaissance and authentication stages of a realistic intrusion.

| Attack | Description | Documentation |
|---------|-------------|---------------|
| Attack 01 | Host Discovery (ICMP) | [attack-01-host-discovery.md](attack-01-host-discovery.md) |
| Attack 02 | TCP SYN Port Scan | [attack-02-port-scanning.md](attack-02-port-scanning.md) |
| Attack 03 | Service Enumeration | [attack-03-service-enumeration.md](attack-03-service-enumeration.md) |
| Attack 04 | SSH Authentication Analysis | [attack-04-ssh-authentication.md](attack-04-ssh-authentication.md) |
| Attack 05 | Web Application Enumeration | [attack-05-web-application-enum.md](attack-05-web-application-enum.md) |
| Attack 06 | Web Authentication Analysis | [attack-06-web-authentication-analysis.md](attack-06-web-authentication-analysis.md) |

---

## Workflow

Each attack followed the same repeatable methodology.

1. Define the attack objective.
2. Execute the attack from the Kali attacker VM.
3. Capture network traffic using tcpdump.
4. Observe host artifacts where applicable.
5. Analyze packet captures using Wireshark.
6. Document observations, evidence, and defender insights.

---

## Evidence Collected

Each attack includes:

- Packet capture (PCAP)
- Wireshark analysis
- Command execution
- Screenshots
- Network artifacts
- Host artifacts (where applicable)
- Defender perspective
- Detection opportunities
- Limitations
- Key takeaways

---

## Learning Outcomes

By completing this phase, the following concepts were demonstrated:

- Host discovery using ICMP
- TCP SYN scanning
- Service enumeration
- SSH authentication analysis
- HTTP directory enumeration
- Web authentication analysis
- Packet-level network analysis
- Correlation of network and host artifacts
- Defender-oriented observation of attack behavior

---

## Next Phase

Phase 3 builds upon the attacks documented in this phase by implementing simple, explainable detection techniques for each attack scenario. The emphasis shifts from generating attack traffic to identifying and analyzing it from a defender's perspective.