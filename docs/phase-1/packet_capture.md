# Packet Capture and Basic Traffic Visibility

## Objective

The goal of this exercise was to understand how network activity appears at the packet level inside an isolated virtual machine environment.

This phase focused on:

- Identifying active network interfaces
- Capturing live traffic
- Observing protocol behavior
- Understanding packet visibility during normal activity

The purpose was not attack simulation, but developing foundational observability skills.

---

## Environment

| Component | Details |
|---|---|
| Host System | Windows |
| Hypervisor | VirtualBox |
| VM | Ubuntu Victim Lab |
| Network Mode | NAT |
| Capture Tool | tcpdump |
| Interface Observed | enp0s3 |

---

## Commands Used

### Identify Active Network Interface

```bash
ip a
```

### Start Live Packet Capture
```bash
sudo tcpdump -i enp0s3
```

### Generate Network Traffic
```bash
ping google.com
curl example.com
nslookup google.com
```
