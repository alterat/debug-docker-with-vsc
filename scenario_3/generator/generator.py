import redis
import random
import os
import time

BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = int(os.environ.get("BROKER_PORT"))
BROKER_DB =   int(os.environ.get("BROKER_DB"))

r = redis.Redis(host=BROKER_HOST,
                port=BROKER_PORT,
                db=BROKER_DB)

WAIT_TIME = int(os.getenv("WAIT_TIME"))

if __name__ == "__main__":
    print("*** Start generating ***")
    while True:
        level = random.randint(1,10)
        print("Level: ", level)
        r.lpush('generator', level)
        time.sleep(WAIT_TIME)