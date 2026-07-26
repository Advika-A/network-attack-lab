# Attack 06 Detection – Web Authentication Detection

## Overview

This detection identifies repeated web authentication attempts by analyzing HTTP POST requests captured during Phase 2. The detector examines HTTP traffic to identify repeated submissions to the DVWA login page, providing a simple method for detecting suspicious authentication activity.

The implementation demonstrates a threshold-based approach for identifying repeated login attempts against a web application.

---

## Detection Objective

Detect repeated web authentication attempts by monitoring HTTP POST requests sent to the web application's login endpoint.

---

## Attack Summary

| Field | Value |
|-------|-------|
| Attack | Web Authentication |
| Application | Damn Vulnerable Web Application (DVWA) |
| Tool | Web Browser (via Burp Suite) |
| Attacker | 10.0.2.4 |
| Target | 10.0.2.15 |
| Data Source | HTTP Traffic (PCAP) |

---

## Data Source

**Packet Capture**

```text
captures/phase-2/attack-06/attack-06-web-authentication.pcap
```

---

## Detection Logic

The detection performs the following steps:

1. Opens the packet capture.
2. Filters HTTP POST requests.
3. Extracts:
   - Source IP
   - Target IP
   - Login endpoint
4. Groups authentication attempts by source IP.
5. Counts the number of HTTP POST requests.
6. Compares the observed activity against a configurable threshold.
7. Generates an alert for sources exceeding the threshold.

---

## Detection Strategy

Web application authentication typically involves HTTP POST requests submitted to a login endpoint. Repeated POST requests originating from the same source within a short period may indicate password guessing, credential stuffing, or brute-force activity. By monitoring the frequency of login attempts, defenders can identify suspicious authentication behavior before unauthorized access is achieved.

---

## Implementation

Detection script:

```text
detections/python/detect_web_auth.py
```

Example execution:

```bash
python detections/python/detect_web_auth.py captures/phase-2/attack-06/attack-06-web-authentication.pcap
```

Custom threshold:

```bash
python detections/python/detect_web_auth.py captures/phase-2/attack-06/attack-06-web-authentication.pcap --threshold 5
```

---

## Validation Results

The detector was validated using the HTTP authentication traffic generated during Phase 2.

### Detection Summary

| Metric | Value |
|--------|------:|
| Detection Verdict | Potential Repeated Web Authentication Attempts |
| Login Attempts | 2 |
| Suspicious Sources | 1 |
| Source IP | 10.0.2.4 |
| Login Endpoint | /dvwa/login.php |

The configured threshold was exceeded, resulting in a successful detection.

---

## Sample Output

```text
============================================================
Web Authentication Detection
============================================================
PCAP File : attack-06-web-authentication.pcap
Threshold : 2 login attempts

Status              : Detection Complete
Detection Verdict   : Potential Repeated Web Authentication Attempts
Suspicious Sources  : 1

Detected Sources
------------------------------------------------------------
[1]
Source IP       : 10.0.2.4
Target IP       : 10.0.2.15
Login Endpoint  : /dvwa/login.php
POST Requests   : 2

============================================================
```

---

## Detection Accuracy

The detector successfully identified all HTTP POST requests directed to the DVWA login endpoint and correctly grouped repeated authentication attempts by source IP.

---

## Potential False Positives

Repeated login attempts may also occur during:

- Legitimate users entering incorrect credentials.
- User account testing during application development.
- Security assessments and penetration testing.
- Automated application testing or quality assurance activities.

Detection results should be interpreted alongside operational context.

---

## Limitations

This implementation:

- Operates on offline packet captures.
- Uses a configurable threshold-based approach.
- Detects repeated HTTP POST requests only.
- Does not determine whether authentication succeeded or failed.
- Does not inspect encrypted HTTPS traffic.
- Does not correlate authentication attempts across multiple applications or systems.

---

## Defender Perspective

Monitoring HTTP authentication traffic provides valuable visibility into web application login activity. Repeated login attempts directed at authentication endpoints may indicate password guessing or brute-force attacks. Simple threshold-based monitoring enables defenders to detect suspicious authentication behavior and investigate potential unauthorized access attempts.

---

## Key Takeaways

- HTTP POST requests provide visibility into web authentication activity.
- Repeated login attempts from the same source can indicate password guessing or brute-force attacks.
- Threshold-based monitoring offers a simple and explainable method for detecting suspicious authentication behavior.
- Application-layer monitoring complements network and host-based detection within a layered defense strategy.