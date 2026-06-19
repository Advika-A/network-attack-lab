# AI-Assisted Cyber Lab for Network Attack Simulation, Detection, and Incident Analysis

![Status](https://img.shields.io/badge/Status-Active-green)
![Phase](https://img.shields.io/badge/Phase-1%20Infrastructure-blue)
![Focus](https://img.shields.io/badge/Focus-Defensive%20Cybersecurity-red)
![Environment](https://img.shields.io/badge/Environment-Isolated%20Virtual%20Lab-orange)

A structured cybersecurity lab environment for studying network traffic, attack observability, packet analysis, and explainable intrusion detection inside isolated virtual machines.

---

## Overview

This project focuses on building a stable and observable cyber lab for understanding how attacks appear from a defender’s perspective.

The lab is designed to support:

- Safe attack simulation
- Network traffic observation
- Packet capture and analysis
- Security monitoring workflows
- Intrusion detection experimentation
- Explainable defensive analysis

The primary goal is not offensive exploitation, but understanding:
- what attacks look like,
- what artifacts they generate,
- and how defenders observe them inside controlled environments.

## Architechture Diagram


                                     Internet
                                         │
                                         │
                                  VirtualBox NAT
                                         │
                                         |
                                Windows Host Machine
                                         |
                                         |
    ┌───────────────────────────────────────────────────────────────────────────┐                            
    Kali Linux Attacker VM   |   Ubuntu Victim Lab VM  |  Future Monitoring VM 
        10.0.2.15 (NAT)              10.0.2.15 (NAT)     (Wireshark / IDS / Logging)

    -No direct access to hostel LAN
    -No interaction with public devices
## Ethical Scope

All experimentation is performed inside isolated virtual environments intended only for learning and research purposes.
