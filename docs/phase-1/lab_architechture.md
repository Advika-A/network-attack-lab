# Phase 1 Lab Architecture

## Objective

Create an isolated virtual cybersecurity laboratory for studying network behavior, traffic analysis, attack simulation, and intrusion detection techniques.

## Architecture

```text
                         Internet
                             │
                     VirtualBox NAT
                             │
 ┌─────────────────────────────────────────────┐
 │           Windows Host Machine              │
 │                                             │
 │  Kali Linux Attacker VM                     │
 │  Ubuntu Victim Lab VM                       │
 │  Future Monitoring VM                       │
 └─────────────────────────────────────────────┘
```

## Components

| Component        | Purpose                                   |
| ---------------- | ----------------------------------------- |
| Windows Host     | Physical machine running VirtualBox       |
| Kali Linux VM    | Attack simulation and offensive testing   |
| Ubuntu Victim VM | Target system for experimentation         |
| Monitoring VM    | Future IDS, logging, and traffic analysis |
| VirtualBox NAT   | Ethical isolation from external networks  |


## Security Considerations
-All activity occurs inside controlled virtual machines.

-NAT networking prevents direct exposure to public networks.

-No testing is performed against third-party systems.

-The environment is intended solely for educational and defensive cybersecurity research.
