# Log parsing

Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
  - Total file size: `File size: <total size>`
  - where `<total size>` is the sum of all previous `<file size>` (see input format above)
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order
**Warning:** In this sample, you will have random value - it’s normal to not have the same output as this one.
```
alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
```

### **General Approach/Logic I used to solve this:**

- The general concept behind solving this problem is to read input from stdin line by line, parse each line to extract the file size and status code, and then compute metrics based on the accumulated data.

- Specifically, I kept track of the total file size and the number of occurrences for each status code (200, 301, 400, 401, 403, 404, 405, 500). I also printed statistics every 10 lines and handled keyboard interrupts (CTRL+C).

- To accomplish this, I used a dictionary `status` to store the number of occurrences for each status code, an integer `file_size` to keep track of the total file size, and an integer `line_count` to count the number of lines processed so far.

- I then looped through each line of input, split it into words based on space, extracted the file size and status code, and updated the `status` and `file_size` variables accordingly.

- Every 10 lines or when a keyboard interrupt is detected, I call the `print_stats` function to print out the accumulated statistics. The `print_stats` function takes the `status` and `file_size` variables as inputs and prints out the total file size and the number of occurrences for each status code in ascending order.

- The solution involves parsing input, updating state variables, and printing statistics at regular intervals. 