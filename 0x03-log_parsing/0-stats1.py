#!/usr/bin/python3
import sys

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
            print("File size: {}".format(file_size))
            for key in sorted(status_codes):
                if status_codes[key] != 0:
                    print("{}: {}".format(key, status_codes[key]))
        sys.stdout.flush()

except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))
    raise
