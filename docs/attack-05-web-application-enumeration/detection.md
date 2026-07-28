# Attack 05 Detection – Web Application Enumeration Detection

## Overview

This detection identifies web application directory enumeration activity by analyzing HTTP traffic captured previously. The detector inspects HTTP requests and responses within the packet capture to identify characteristics commonly associated with automated directory discovery tools such as Gobuster.

The implementation demonstrates a simple threshold-based approach for detecting high-volume web enumeration behavior.

---

## Detection Objective

Detect web application directory enumeration by identifying excessive HTTP GET requests and large numbers of HTTP 404 responses.

---

## Attack Summary

| Field | Value |
|-------|-------|
| Attack | Web Application Enumeration |
| Tool | Gobuster |
| Attacker | 10.0.2.4 |
| Target | 10.0.2.15 |
| Data Source | HTTP Traffic (PCAP) |

---

## Data Source

**Packet Capture**

```text
captures/phase-2/attack-05/attack-05-web-enumeration.pcap
```

---

## Detection Logic

The detection performs the following steps:

1. Opens the packet capture.
2. Extracts all HTTP traffic.
3. Counts HTTP GET requests.
4. Records each unique requested path.
5. Counts HTTP response status codes.
6. Identifies the number of HTTP 404 responses.
7. Compares the observed activity against configurable thresholds.
8. Generates an alert when excessive enumeration behavior is detected.

---

## Detection Strategy

Automated directory enumeration tools rapidly request large numbers of potential files and directories. Since most requested resources do not exist, the server typically responds with numerous HTTP 404 (Not Found) responses. Monitoring HTTP request volume together with response code distribution provides a simple and explainable method for identifying enumeration activity.

---

## Implementation

Detection script:

```text
detections/python/detect_web_enum.py
```

Example execution:

```bash
python detections/python/detect_web_enum.py captures/phase-2/attack-05/attack-05-web-enumeration.pcap
```

Custom thresholds:

```bash
python detections/python/detect_web_enum.py captures/phase-2/attack-05/attack-05-web-enumeration.pcap --threshold 100 --not-found-threshold 50
```

---

## Validation Results

The detector was validated using the Gobuster-generated packet capture collected previously.

### Detection Summary

| Metric | Value |
|--------|------:|
| Detection Verdict | Potential Web Directory Enumeration |
| Source IP | 10.0.2.4 |
| Target IP | 10.0.2.15 |
| Total HTTP GET Requests | 4615 |
| Unique Requested Paths | 4615 |
| HTTP 404 Responses | 4608 |

The configured thresholds were exceeded, resulting in a successful detection.

---

## Sample Output

```text
============================================================
Web Application Enumeration Detection
============================================================
PCAP File : attack-05-web-enumeration.pcap
GET Request Threshold : 50
HTTP 404 Threshold    : 20

Status              : Detection Complete
Detection Verdict   : Potential Web Directory Enumeration

Traffic Summary
------------------------------------------------------------
Source IP           : 10.0.2.4
Target IP           : 10.0.2.15
Total GET Requests  : 4615
Unique Paths        : 4615
HTTP 404 Responses  : 4608

HTTP Status Code Distribution
------------------------------------------------------------
200  : 2
301  : 1
403  : 4
404  : 4608

============================================================
```

---

## Detection Accuracy

The detector successfully identified the high-volume HTTP GET requests generated during the Gobuster scan and correctly detected the unusually large number of HTTP 404 responses characteristic of directory enumeration activity.

---

## Potential False Positives

Similar HTTP request patterns may also occur during:

- Legitimate website vulnerability assessments.
- Automated web crawlers or search engine indexing.
- Website performance testing.
- Internal application testing or quality assurance activities.

Detection results should be interpreted alongside operational context.

---

## Limitations

This implementation:

- Operates on offline packet captures.
- Uses configurable threshold-based detection.
- Detects only HTTP-based directory enumeration activity.
- Does not analyze HTTPS traffic without prior decryption.
- Does not distinguish between different enumeration tools.

---

## Defender Perspective

Web server traffic provides valuable visibility into reconnaissance activity targeting web applications. Monitoring unusually high volumes of HTTP GET requests together with excessive HTTP 404 responses enables defenders to identify directory enumeration attempts before attackers progress to exploiting discovered resources.

---

## Key Takeaways

- HTTP traffic analysis enables detection of web application reconnaissance.
- Large numbers of HTTP GET requests indicate automated enumeration activity.
- Excessive HTTP 404 responses are a strong indicator of directory discovery attempts.
- Simple threshold-based monitoring provides an effective and explainable detection mechanism for web enumeration attacks.