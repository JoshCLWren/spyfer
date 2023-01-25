import sys
import time


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def delay_print(*args, delay=0.01, color=None):
    """
    Print to stdout one character at a time like a typewriter with a delay between each character
    in the color specified.
    """
    if color:
        print(color, end="")

    for arg in args:
        for char in arg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    print()
