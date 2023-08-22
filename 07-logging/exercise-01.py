"""
Given file exercise-01.py
    1. Convert all calls to `print()` to proper logging
    2. configure logging to log simultaneously to two files and console, using the following formats and levels:
        1. File A: `timestamp - level - message` level DEBUG
        2. File B: `filename - funcname - line number` level INFO
        3. Console: `asctime [level]: message` level WARN
"""

import time
import random
import functools


def decorate(func):
    def wrapper(*args, **kwargs):
        print("INFO: calling a function")
        return func(*args, *kwargs)

    return wrapper


@decorate
def complex_calculation(a, b):
    print("DEBUG: performing complex calculation")
    result = a + b
    print(f"DEBUG: result={result}")
    return result


if __name__ == "__main__":
    for _ in range(10):
        result = complex_calculation(random.randint(0, 15), random.randint(0, 15))
        if result <= 10:
            print("WARN: a warning")
        elif result <= 20:
            print("ERROR: an error")
        elif result <= 30:
            print("CRITICAL: a critical error")
