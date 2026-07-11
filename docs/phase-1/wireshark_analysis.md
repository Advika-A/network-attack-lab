# Wireshark Analysis

## Objective

Analyze a baseline packet capture generated from normal Ubuntu system activity.

## Key Findings

### Network Address

Ubuntu VM:
10.0.2.15

### DNS Activity

DNS queries were primarily directed toward VirtualBox's internal DNS service (10.0.2.3).

### Background Traffic

The capture contained significant background traffic including DNS, NBNS, and routine network communications, demonstrating that operating systems continuously generate network activity even during normal operation.

### Capture Statistics

- Packets: 18,738
- Duration: 157.95 seconds
- Size: 77 MB

### Learning Outcome

This analysis established an initial understanding of packet capture workflows, protocol identification, and baseline network behavior within the virtual lab environment.
