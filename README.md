# Defensive Cyber Range for Network Attack Simulation and Detection

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-VirtualBox-orange)
![Focus](https://img.shields.io/badge/Focus-Defensive%20Cybersecurity-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A portfolio-oriented cybersecurity project that demonstrates how common network attacks can be simulated within an isolated virtual environment, captured as network traffic, analyzed using packet inspection, and detected through custom Python-based detection scripts. The project emphasizes practical defensive security, explainable detection logic, and reproducible experimentation.

---

## Overview

This project focuses on building a stable and observable cyber range to understand how common network attacks appear from a defender's perspective.

The project includes:

- Controlled network attack simulation
- Packet capture using **tcpdump**
- Traffic analysis with **Wireshark**
- Custom Python-based detection engineering
- Explainable incident analysis and documentation

Rather than focusing on offensive exploitation, the project emphasizes understanding:

- How attacks manifest in network traffic
- The artifacts they generate
- How defenders can detect and analyze them within a controlled environment

---

## Project Objectives

- Build a reproducible cyber range using virtual machines
- Simulate realistic network attacks in an isolated environment
- Capture and analyze attack traffic
- Develop explainable Python-based detection scripts
- Document detection logic and incident analysis
- Demonstrate practical defensive cybersecurity skills

---

## Architecture

### Lab Architecture

![Lab Architecture](diagrams/lab-architecture.png)

### Project Workflow

![Project Architecture](diagrams/project-workflow.png)

> **Security Note**
>
> - No direct access to the hostel LAN
> - No interaction with public devices
> - All experimentation is confined to an isolated VirtualBox NAT network

---

## Ethical Scope

All experimentation was conducted within an isolated VirtualBox NAT network using virtual machines owned and controlled by the author. No public systems, external networks, or unauthorized devices were targeted. This project is intended solely for cybersecurity education, defensive research, and skill development.