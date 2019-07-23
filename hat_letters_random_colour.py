#!/usr/bin/env/python
#this script will disply letters with random colors on the Pi HAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# assign a random integer between 0 and 255 to a variable named r
r = random.randint(0,255)
print("the random number is"), r, ("this time")

sense.show_letter("h", (r, 0, 0))
time.sleep(1)
sense.show_letter("i", (0, r, 0))
time.sleep(1)
sense.show_letter("!", (0, 0, r))
time.sleep(1)
sense.clear()

