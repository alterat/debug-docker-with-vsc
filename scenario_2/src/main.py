import os
import time
import random

print("Starting Python code")

REFRESH_RATE = os.getenv('REFRESH_RATE')

try:
    REFRESH_RATE = int(REFRESH_RATE)
except ValueError:
    print("Invalid REFRESH_RATE. Setting default = 5.")
    REFRESH_RATE = 5

def am_i_tired():
    if random.randint(1,10) > 5:
        return "Yes, I am very tired"
    return "No, I am not tired"

if __name__ == "__main__":
    while True:
        print(am_i_tired())
        time.sleep(REFRESH_RATE)