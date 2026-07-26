# Lab Overview

## Objective

This project was developed using an isolated cyber range to safely simulate common network attacks and study them from a defender's perspective. The environment provides a controlled platform for generating network traffic, capturing packet data, analyzing attack artifacts, and validating custom detection scripts.

The lab was designed with the following objectives:

- Build a reproducible cybersecurity testing environment
- Simulate realistic network attacks in isolation
- Capture and analyze network traffic
- Develop explainable Python-based detection scripts
- Support structured incident analysis and documentation

---

## Lab Environment

| Component | Details |
|-----------|---------|
| Host System | Windows |
| Hypervisor | Oracle VirtualBox |
| Attacker VM | Kali Linux |
| Victim VM | Ubuntu Linux |
| Network Configuration | VirtualBox NAT Network |
| Victim Services | Apache, OpenSSH, DVWA |
| Packet Capture | tcpdump |
| Packet Analysis | Wireshark |
| Detection Development | Python 3.12, PyShark, TShark |

---

## Network Layout

The cyber range consists of two virtual machines connected through an isolated VirtualBox NAT network.

- **Attacker:** Kali Linux (`10.0.2.4`)
- **Victim:** Ubuntu Linux (`10.0.2.15`)

This configuration enables controlled attack simulation without exposing external systems.

---

## Project Workflow

1. Configure the isolated cyber range.
2. Simulate network attacks from the Kali VM.
3. Capture network traffic using `tcpdump`.
4. Analyze captured traffic with Wireshark.
5. Develop Python-based detection scripts.
6. Validate detections against captured attack traffic.
7. Document findings and incident analysis.

---

## Ethical Scope

All experiments were conducted within an isolated VirtualBox NAT network using virtual machines owned and controlled by the author. No public systems, external networks, or unauthorized devices were targeted.

This project is intended solely for cybersecurity education, defensive research, and practical skill development.