# Attack 04 – SSH Authentication Attack

## Objective

Simulate failed SSH authentication attempts to study both network-level and host-level artifacts generated during a login failure.

---

## Environment

| System | Role | IP Address |
|---------|------|------------|
| Kali Linux | Attacker | 10.0.2.4 |
| Ubuntu | Victim | 10.0.2.15 |

**Network:** VirtualBox NAT Network

---

## Attack Overview

After identifying exposed services, attackers often attempt to authenticate using valid or guessed credentials.

This experiment intentionally performed a small number of failed login attempts against the SSH service to observe authentication-related artifacts without attempting to compromise the system.

---

## Attack Method

SSH connection initiated from Kali:

```bash
ssh testuser@10.0.2.15
```

A non-existent username (`testuser`) was used.

Three incorrect password attempts were entered before the SSH session terminated.

---

## Packet Capture

Capture file:

```
captures/phase-2/attack-04/ssh_failed_login.pcap
```

Traffic captured using:

```bash
sudo tcpdump -i eth0 -w ssh_failed_login.pcap
```

Approximately **35 SSH packets** were observed.

---

## Network Artifacts

Observed protocols:

- TCP
- SSH

Observed activity:

- TCP connection established
- SSH protocol negotiation
- Encrypted authentication exchange
- Connection termination after repeated failures

Unlike HTTP traffic, SSH encrypts authentication data after the initial protocol negotiation.

---

## Host Artifacts

Ubuntu authentication logs recorded:

- Invalid username detection
- Failed authentication attempts
- Source IP address
- Source port
- SSH daemon process information
- Session termination

Example events included:

- Invalid user `testuser`
- Failed password attempts
- Connection closed by invalid user

---

## Defender Perspective

A defender monitoring both the network and the host would observe:

- Connection attempts to TCP port 22
- Multiple failed authentication attempts
- Repeated failures from a single source IP
- Invalid username usage
- SSH daemon log entries
- Session termination after authentication failures

Unlike previous attacks, this activity generates evidence in both packet captures and operating system logs.

---

## Detection Opportunities

Possible indicators include:

- Multiple failed SSH logins
- Invalid usernames
- Repeated authentication failures from the same IP
- High number of failed logins within a short time
- Correlation between SSH traffic and authentication logs

---

## Limitations

This experiment demonstrates authentication failures only.

It does not attempt credential compromise, privilege escalation, or persistence.

---

## Key Takeaways

- SSH authentication attempts generate both network and host evidence.
- Authentication logs provide detailed forensic information unavailable from packet captures alone.
- SSH encryption protects credentials from network observers.
- Correlating packet captures with system logs provides a more complete view of attacker activity.