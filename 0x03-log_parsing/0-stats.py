#!/usr/bin/python3

import sys
import signal
import re

# Regular expression to match the log format
log_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')

# Initialize variables for statistics
total_file_size = 0
status_code_count = {}

# Function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Function to print statistics
def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")

# Register SIGINT (Ctrl+C) signal handler
signal.signal(signal.SIGINT, signal_handler)

# Process stdin line by line
try:
    for line in sys.stdin:
        line = line.strip()
        # Match line with the log pattern
        match = log_pattern.match(line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))
            # Update total file size
            total_file_size += file_size
            # Update status code count
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            else:
                status_code_count[status_code] = 1
        # Print statistics every 10 lines
        if len(status_code_count) > 0 and len(status_code_count) % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Print final statistics upon receiving KeyboardInterrupt
    print_statistics()
    sys.exit(0)

