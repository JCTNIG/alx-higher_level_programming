#!/usr/bin/python3

"""Reads from standard input and computes metrics.
   For each ten lines or the input of a keyboard interruption (CTRL + C),
   Returns these statistics:
    a, Total file size up to that point.
    b, Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for lines in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            lines = lines.split()

            try:
                size += int(lines[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lines[-2] in valid_codes:
                    if status_codes.get(lines[-2], -1) == -1:
                        status_codes[lines[-2]] = 1
                    else:
                        status_codes[lines[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
