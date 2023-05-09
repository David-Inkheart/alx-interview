#!/usr/bin/python3
"""Log parsing: reads stdin line by line and computes metrics."""
import sys


def print_stats(status, file_size):
    """Print statistics for every 10 lines"""
    print("File size: {}".format(file_size))
    for k in sorted(status.keys()):
        if status[k]:
            print("{}: {}".format(k, status[k]))


status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        # Split the line into words based on space
        words = line.split()

        # Get the file size and status code
        file_size += int(words[-1])
        status_code = words[-2]

        # Check if the status code is valid
        if status_code in status:
            status[status_code] += 1

        # Increment line count
        line_count += 1

        # Print stats for every 10 lines
        if line_count % 10 == 0:
            print_stats(status, file_size)

except KeyboardInterrupt:
    print_stats(status, file_size)
    raise
