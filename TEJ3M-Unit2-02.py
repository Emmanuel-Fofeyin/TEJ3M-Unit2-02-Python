# Copyright(c) 2023 Emmanuel Fofeyin All rights reserved.
# Created by : Emmanuel Fofeyin
# Created on : September 2023
# TEJ3M-Unit2-02.py File.

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

blinkTime = 1

while True:
    led.value = True
    time.sleep(blinkTime)
    led.value = False
    time.sleep(1)
    blinkTime += 1
  
