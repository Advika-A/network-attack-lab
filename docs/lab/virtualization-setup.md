# Virtualization Setup

## Virtual Machines

### Attacker

| Component | Details |
|-----------|---------|
| Operating System | Kali Linux |
| Role | Attack Simulation |
| IP Address | 10.0.2.4 |

### Victim

| Component | Details |
|-----------|---------|
| Operating System | Ubuntu Linux |
| Role | Target System |
| IP Address | 10.0.2.15 |

Enabled services:

- Apache Web Server
- OpenSSH
- Damn Vulnerable Web Application (DVWA)

---

## Network Configuration

Both virtual machines were connected to an isolated VirtualBox NAT Network.

This configuration provided:

- Communication between virtual machines
- No direct access to the hostel LAN
- No interaction with external devices
- A controlled environment for traffic capture and attack simulation

---

## Environment Validation

The environment was validated before conducting attack simulations by confirming:

- Network connectivity between the virtual machines
- SSH accessibility
- HTTP service availability
- DVWA accessibility through a web browser

Successful validation ensured that the cyber range was functioning correctly before traffic capture and detection development began.