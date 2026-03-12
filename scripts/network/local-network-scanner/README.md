# Local Network Scanner

This script scans a local network to detect reachable devices.

It sends ping requests to all addresses in the specified subnet.

## Features

- Detect active devices
- Scan up to 254 hosts
- Simple command line interface

## Requirements

Python 3

This script uses the built-in system ping command.

## Usage

Run the script:

python network_scanner.py

Enter your base network.

Example:

192.168.1

The script will scan:

192.168.1.1 → 192.168.1.254
