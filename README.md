# Python Port Scanner

A simple TCP port scanner written in Python as my second python project.  
It scans a user-defined port range on a target IPv4 address, checks host availability, identifies common services, and attempts basic banner grabbing.

**Educational use only. Scan only systems you own or have permission to test.**

## Features
- IPv4 validation with regex
- Custom port range scanning
- TCP connect scanning with timeouts
- Host availability check (ping)
- Basic banner grabbing
- Common service identification
- Cross-platform (Windows / Linux)

## Follow the prompts to enter:

-Target IPv4 address
-Base port (beggining of port scan range eg. 8078)
-End port (end of the port scan range eg. 8082)

## Limitations

-Sequential scanning (no threading)
-Basic service detection
-No UDP or CIDR scanning

## Purpose

--Built as a learning project to practice Python networking, sockets, input validation, and OS-level interactions.

# Clone
```bash
git clone https://github.com/dzenan-dzizic/port-scanner.git
```

## Usage
```bash
python3 port_scanner.py
```
