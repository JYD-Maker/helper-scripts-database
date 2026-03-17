# Password Bruteforce Simulator

This script simulates a password bruteforce attack using a wordlist.

It compares hashed passwords against a target hash to find matches.

It is useful for learning how password attacks work and understanding the importance of strong passwords.

## Features

- Simulate bruteforce attacks using a wordlist
- SHA256 hash comparison
- Detect matching passwords
- Simple command line interface

## Requirements

Python 3 must be installed.

Check your Python version:

python --version

## Usage

Create a wordlist file (one password per line).

Run the script:

python password_bruteforce.py

Enter:

Target hash  
Wordlist file  

## Example Output

Password Bruteforce Simulator  
Enter target hash: ecd718...  

[FOUND] Password: test123  

## Use Cases

- Learning password cracking concepts
- Security training
- Understanding password strength importance
- Testing weak passwords
