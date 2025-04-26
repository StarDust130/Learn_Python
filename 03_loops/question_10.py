# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1  # Start with 1 second

for attempt in range(1, 6):  # 5 retries
    print(f"Attempt {attempt}... Waiting {wait_time} seconds before retry.")
    time.sleep(wait_time)
    wait_time *= 2  # Double the wait time
