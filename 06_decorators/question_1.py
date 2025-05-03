#  Problem: Write a decorator that measures the time a function takes to execute.

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.2f} time")
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)
    print("Done! 🤑")



example_function(3)