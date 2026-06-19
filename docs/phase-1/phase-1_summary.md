# Phase 1 Summary Report

## Objective

The objective of Phase 1 was to establish a stable, ethical, and observable virtual cybersecurity laboratory capable of supporting future attack simulation, network monitoring, intrusion detection, and security research activities.

This phase focused on infrastructure preparation, virtual networking fundamentals, packet visibility, and documentation practices rather than offensive security activities.

---

## Environment Setup

A VirtualBox-based lab environment was created on a Windows host machine.

### Virtual Machines

| VM | Purpose |
|----|----------|
| Kali Linux | Attack simulation environment |
| Ubuntu Victim Lab | Target system for experimentation |
| Monitoring VM (Future) | Traffic analysis, logging, and intrusion detection |

The Ubuntu victim machine was created from a clean base installation and cloned to support repeatable experimentation without affecting the original system.

---

## Network Architecture

The lab was configured using VirtualBox NAT networking.

This approach was selected to:

- Maintain ethical isolation
- Prevent interaction with external devices
- Avoid interference with hostel and public networks
- Provide controlled internet access for software installation and updates

The architecture ensures that all experimentation remains confined to the virtual environment.

---

## Packet Capture and Observability

Packet visibility was introduced using tcpdump and Wireshark.

### Initial Packet Capture

Traffic was captured using:

```bash
sudo tcpdump -i enp0s3 -w first_capture.pcap
```
The resulting packet capture contained:

| Metric              | Value           |
| ------------------- | --------------- |
| Packets Captured    | 18,738          |
| Capture Duration    | 157.95 seconds  |
| File Size           | 77 MB           |
| Average Packet Rate | 118 packets/sec |


The captured PCAP file was analyzed using Wireshark.

### Key observations included:

-DNS queries directed to VirtualBox's internal DNS service

-Routine operating system network activity

-Background traffic generated even during normal operation

-Basic protocol identification and packet inspection workflows


The analysis demonstrated that modern systems continuously generate network traffic and highlighted the importance of establishing baseline behavior before attempting intrusion detection.

## Documentation Produced

The following documentation was created during Phase 1:
```
docs/
└── phase-1/
    ├── virtualization-setup.md
    ├── packet_capture.md
    ├── pcap_analysis.md
    ├── lessons_learned.md  
    ├── networking_basics.md   
    ├── wireshark_analysis.md  
    ├── lab_architecture.md  
    └── phase-1-summary.md
```
## Key Learning Outcomes

### Phase 1 provided practical experience with:

-Virtual machine deployment and management

-Virtual networking concepts

-Network interface identification

-Packet capture techniques

-Wireshark-based traffic analysis

-Baseline traffic observation

-Technical documentation practices

-Ethical cybersecurity lab design

### Challenges Encountered

-Virtual machine recovery issues

-Snapshot and storage path problems

-OneDrive synchronization conflicts

-VirtualBox disk management issues

-Ubuntu installation and cloning procedures

Resolving these issues improved operational understanding of virtualization environments and highlighted the importance of reliable infrastructure management.

## Phase 1 Outcome

Phase 1 successfully established a stable and well-documented cybersecurity laboratory environment with foundational traffic observability capabilities.

The environment is now prepared for controlled attack simulation, evidence collection, and defensive analysis activities in subsequent phases.
