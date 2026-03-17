# Password Audit

This script analyzes a list of passwords and evaluates their strength.

It helps identify weak passwords and improve overall password security.

It is useful for security audits, password policy checks, and learning password strength evaluation.

## Features

- Analyze multiple passwords from a file
- Detect weak, medium, and strong passwords
- Uses length, uppercase, lowercase, digits, and special characters
- Simple command line interface

## Requirements

Python 3 must be installed.

Check your Python version:

python --version

## Usage

Create a text file with passwords (one per line).

Run the script:

python password_audit.py

Enter the file path when prompted.

Example:

passwords.txt

## Example Output

Password Audit Tool  
Enter password list file: passwords.txt  

123456 → Weak ❌  
Password1 → Medium ⚠️  
SecurePass!123 → Strong 🔥  

## Use Cases

- Identifying weak passwords
- Improving password security
- Security audits
- Learning password strength evaluation
