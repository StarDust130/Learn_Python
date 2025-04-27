#   Problem: Write a generator function that yields even numbers up to a specified limit.

def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num  # Yield even numbers one by one
        num += 2   # Increment by 2 to get the next even number


# Example usage:
for even in even_numbers(10):
    print(even)
