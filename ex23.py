#Create a simple countdown timer using a while loop.
#Write a code to create a simple countdown timer of 5 seconds using a while loop.
#Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

import time 

def set_countdown(sec):
    while sec > 0:
        print(f"time remaining: {sec}")
        time.sleep(1)
        sec -= 1
    print("time's up")

user_time = int(input("countdown time: "))
set_countdown(user_time)
