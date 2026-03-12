# Subnet Calculator

This script calculates subnet information from an IPv4 network.

It helps determine network details such as network address, broadcast address and usable host range.

## Features

- Calculate subnet mask
- Show network and broadcast address
- Display total and usable hosts
- Simple command line usage

## Requirements

Python 3

This script uses the built-in Python `ipaddress` module.

## Usage

Run the script:

python subnet_calculator.py

Enter a network with CIDR notation.

Example:

192.168.1.0/24

## Example Output

Subnet Information
----------------------------

Network Address : 192.168.1.0
Broadcast Address: 192.168.1.255
Subnet Mask     : 255.255.255.0
Total Hosts     : 256
Usable Hosts    : 254
