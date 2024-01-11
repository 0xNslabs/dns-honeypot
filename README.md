# Simple DNS Honeypot Server

## Introduction
This Simple DNS Honeypot Server is a streamlined script designed for cybersecurity enthusiasts and professionals. This Python script, leveraging the Twisted framework, establishes a low-interaction DNS server to log and monitor DNS queries. It serves as an essential instrument for basic network traffic analysis and early detection of potential security threats, making it perfect for entry-level cybersecurity practice and threat awareness.

## Features
- **Low-Interaction Honeypot**: Minimizes complexity and reduces risk.
- **Customizable DNS Server**: Host and port settings are easily configurable.
- **Comprehensive Logging**: Captures DNS query details for analysis.
- **Real-time Monitoring**: Instantly logs DNS queries for security monitoring.
- **Security Research Tool**: Excellent for understanding DNS-based threats and network probing.

## Requirements
- Python 3.x
- Twisted Python library

## Installation
Clone the repository or download the `dns.py` script. Ensure Python and Twisted are installed.

```bash
git clone https://github.com/0xNslabs/dns-honeypot
cd dns-honeypot
pip install twisted
```

## Usage

Execute the script with optional arguments for host and port. Defaults to 0.0.0.0 (all interfaces) and port 5353.


```bash
python3 dns.py --host 0.0.0.0 --port 5353
```

## Logging

Logs are stored in `dns_honeypot.log`, detailing each DNS query received by the server for further scrutiny.

## Simple DNS Honeypot In Action

![Simple DNS Honeypot in Action](https://raw.githubusercontent.com/0xNslabs/dns-honeypot/main/PoC.png)
*The image above captures the Simple DNS Honeypot logging real-time DNS queries*

## Other Simple Honeypot Services

Check out the other honeypot services for monitoring various network protocols:

- [DNS Honeypot](https://github.com/0xNslabs/dns-honeypot) - Monitors DNS interactions.
- [FTP Honeypot](https://github.com/0xNslabs/ftp-honeypot) - Simulates an FTP server.
- [LDAP Honeypot](https://github.com/0xNslabs/ldap-honeypot) - Mimics an LDAP server.
- [NTP Honeypot](https://github.com/0xNslabs/ntp-honeypot) - Monitors Network Time Protocol interactions.
- [PostgreSQL Honeypot](https://github.com/0xNslabs/postgresql-honeypot) - Simulates a PostgreSQL database server.
- [SIP Honeypot](https://github.com/0xNslabs/sip-honeypot) - Monitors SIP (Session Initiation Protocol) interactions.
- [SSH Honeypot](https://github.com/0xNslabs/ssh-honeypot) - Emulates an SSH server.
- [TELNET Honeypot](https://github.com/0xNslabs/telnet-honeypot) - Simulates a TELNET server.

## Security and Compliance
- **Caution**: This server is a honeypot. Employ responsibly in controlled network environments.
- **Compliance**: Adhere to local laws and regulations in deployment.

## License
This project is distributed under the MIT License. See `LICENSE` for more information.