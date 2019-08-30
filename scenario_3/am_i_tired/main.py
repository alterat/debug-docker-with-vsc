import os
import time
import random
import redis

print("Starting Python code")

BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = int(os.environ.get("BROKER_PORT"))
BROKER_DB =   int(os.environ.get("BROKER_DB"))

r = redis.Redis(host=BROKER_HOST, 
                port=BROKER_PORT, 
                db=BROKER_DB)

def am_i_tired(level):
    if level > 5:
        return "Yes, I am very tired"
    return "No, I am not tired"

if __name__ == "__main__":
    while True:
        try:
            name, mess = r.brpop('generator', timeout=1)
            if mess:
                level = int(mess)
                print(am_i_tired(level))
        except TypeError:
            pass