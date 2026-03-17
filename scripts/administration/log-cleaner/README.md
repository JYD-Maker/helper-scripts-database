Log-File Cleaner

This script helps with system administration by automatically removing old log files to free up disk space.
It is useful for maintaining server health and preventing storage issues caused by runaway log growth.

Features

Scan a specified directory for files with the .log extension

Custom age threshold for deletion (in days)

Simple command line interface

Safety feedback in the console showing deleted files

Requirements

Python 3

Usage

Run the script:

python log_cleaner.py


Then follow the prompts to enter the path and the age threshold.

Example Output

--- Log-File Cleaner (Python 3) ---
Path to log folder: C:\Server\Logs
Delete files older than (days): 30

Searching for .log files in C:\Server\Logs...
Deleted: access_old.log
Deleted: error_january.log
Total cleanup finished.


Use Cases

Automated server maintenance

Freeing up disk space on production systems

Managing application logs during development
