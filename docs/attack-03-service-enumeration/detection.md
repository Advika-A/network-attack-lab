# Attack 03 Detection – HTTP Service Enumeration Detection

## Overview

This detection identifies HTTP responses that disclose web server information through the **Server** response header. During service enumeration, attackers often inspect HTTP response headers to identify web server software, version information, and technologies in use. Such information can assist attackers in selecting appropriate exploitation techniques.

This implementation uses Python and PyShark to analyze HTTP traffic captured and identify responses that expose server identification information.

---

## Detection Objective

Detect HTTP responses containing server identification information disclosed through the HTTP **Server** header during web service enumeration.

---

## Attack Summary

| Field | Value |
|-------|-------|
| Attack | Service Enumeration |
| Techniques | HTTP Request, Nmap Version Detection |
| Tools | curl, Nmap |
| Commands | `curl http://10.0.2.15`<br>`sudo nmap -sV 10.0.2.15` |
| Attacker | 10.0.2.4 |
| Target | 10.0.2.15 |
| Data Source | PCAP Capture |

---

## Data Source

**PCAP**

```
captures/phase-2/attack-03/service_enumeration.pcap
```

---

## Detection Logic

The detection performs the following steps:

1. Opens the supplied PCAP file.
2. Filters HTTP traffic using PyShark.
3. Processes HTTP response packets.
4. Checks whether the response contains a **Server** header.
5. Records:
   - Timestamp
   - Server IP
   - Client IP
   - HTTP Status Code
   - Server Header
6. Summarizes:
   - Total HTTP responses
   - Unique server headers observed
   - Distribution of HTTP status codes
7. Reports all detected server information disclosures.

---

## Detection Strategy

Rather than detecting a specific attack signature, this implementation focuses on **information disclosure**.

Many web servers reveal software and version information through the HTTP **Server** header. Attackers performing reconnaissance can use this information to identify vulnerable software versions and plan subsequent attacks.

Monitoring HTTP response headers enables defenders to identify unnecessary information disclosure that may increase an organization's attack surface.

---

## Implementation

Detection script:

```
detections/python/detect_service_enum.py
```

Example execution:

```bash
python detections/python/detect_service_enum.py captures/phase-2/attack-03/service_enumeration.pcap
```

---

## Validation Results

The detection was validated using the service enumeration traffic generated in the pcap.

### Detection Summary

| Metric | Value |
|--------|------:|
| Detection Verdict | Server Information Disclosure Detected |
| HTTP Responses Analysed | 8 |
| Unique Server Headers | 1 |
| HTTP 200 Responses | 4 |
| HTTP 404 Responses | 4 |
| Server Software | Apache/2.4.58 (Ubuntu) |
| Server IP | 10.0.2.15 |
| Client IP | 10.0.2.4 |

The detection successfully identified all HTTP responses exposing server software information within the captured traffic.

---

## Sample Output

```text
============================================================
HTTP Service Enumeration Detection
============================================================
PCAP File : service_enumeration.pcap

Status                 : Detection Complete
Detection Verdict      : Server Information Disclosure Detected
HTTP Responses         : 8
Unique Server Headers  : 1

HTTP Status Summary
------------------------------------------------------------
200 : 4
404 : 4

Detected Services
------------------------------------------------------------
[1]
Server IP     : 10.0.2.15
Client IP     : 10.0.2.4
HTTP Status   : 200
Server Header : Apache/2.4.58 (Ubuntu)

...

============================================================
```

---

## Detection Accuracy

The implementation successfully detected every HTTP response containing a **Server** header within the packet capture.

Validation confirmed that the web server consistently disclosed its software and version information during the service enumeration process.

---

## Potential False Positives

Legitimate HTTP responses commonly include a **Server** header. Similar observations may occur during:

- Normal web browsing
- Health monitoring
- Vulnerability assessments
- Web application testing
- Administrative access

The presence of a Server header alone is not malicious but represents information that attackers may leverage during reconnaissance.

---

## Limitations

This implementation:

- Operates on offline PCAP files.
- Detects only HTTP responses containing a Server header.
- Does not determine whether the disclosed software version is vulnerable.
- Does not analyze HTTPS traffic unless decrypted.
- Does not distinguish between legitimate administrative activity and attacker reconnaissance.

---

## Defender Perspective

Server software identification is often one of the earliest objectives during reconnaissance. Limiting unnecessary information disclosure can reduce the amount of intelligence available to attackers.

Although revealing the server software is not a vulnerability by itself, minimizing exposed version information is considered a security best practice. Monitoring HTTP responses for exposed server details can help defenders identify systems that may benefit from additional hardening.

---

## Key Takeaways

- HTTP response headers may reveal valuable information about web server software.
- The **Server** header can disclose implementation and version details useful during reconnaissance.
- Packet captures provide sufficient visibility to identify information disclosure events.
- PyShark enables efficient inspection of application-layer protocols.
- Simple application-layer detections complement lower-layer network detections in a defensive monitoring strategy.