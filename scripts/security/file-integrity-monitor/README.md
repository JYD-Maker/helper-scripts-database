# File Integrity Monitor

This script monitors files for changes using SHA256 hashing.

It creates a baseline of file hashes and later compares them to detect modifications, deletions, or integrity issues.

It is useful for security checks, detecting unauthorized file changes, and understanding file integrity monitoring in practice.

## Features

- Create a baseline of file hashes
- Detect modified files
- Detect deleted files
- Monitor directories recursively
- Simple command line interface

## Requirements

Python 3 must be installed.

Check your Python version:

python --version

## Usage

Run the script:

python file_integrity_monitor.py

Select an option:

1 = Create baseline  
2 = Check integrity  

When creating a baseline, enter a directory path:

Example:

C:\Test

## Example Output

File Integrity Monitor  
Select option: 2  

[OK] C:\Test\file1.txt  
[MODIFIED] C:\Test\file2.txt  
[DELETED] C:\Test\file3.txt  

## Use Cases

- Detect unauthorized file changes
- Monitor system files
- Security auditing
- Learning file integrity concepts
