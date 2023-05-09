#!/usr/bin/python3
"""Log parsing: reads stdin line by line and computes metrics."""
import sys


def print_stats(file_size, status_codes):
    """Prints the statistics."""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    count = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()
            if len(split_line) == 9:
                if split_line[8].isdigit():
                    file_size += int(split_line[8])
                if split_line[7] in status_codes:
                    status_codes[split_line[7]] += 1
            if count % 10 == 0:
                print_stats(file_size, status_codes)
        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
