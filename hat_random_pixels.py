#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

rn = random.randint(0,7)
r = random.randint(0,255)

sense.set_pixel(rn, rn, (r, 0, 0))
time.sleep(1)
sense.clear()
sense.set_pixel(rn, rn, (0, r, 0))
time.sleep(1)
sense.clear()
sense.set_pixel(rn, rn, (0, 0, r))

time.sleep(1)
sense.clear()

