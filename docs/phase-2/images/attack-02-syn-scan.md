## Packet Analysis

The following Wireshark capture illustrates the behavior of a TCP SYN scan. Closed ports respond with `RST, ACK`, while the open HTTP service (TCP port 80) responds with `SYN, ACK`. Nmap then sends a `RST` packet instead of completing the TCP handshake.

![alt text](<attack-02.png>)