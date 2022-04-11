# https://www.instructables.com/Interfacing-Ultrasonic-Sensor-Using-Raspberry-Pi-P/
# Created by: Daria Bernice Calitsi
# Created on: March 2022
# It detects the distance through the Ultrasonic Distance Sensor.

# Imports Pin and utime
from machine import Pin
import utime

# Sets the pins for trigger and echo
trigger = Pin(13, Pin.OUT)
echo = Pin(14, Pin.IN)

# Main function
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()

   while echo.value() == 0:
       signaloff = utime.ticks_us()

   while echo.value() == 1:
       signalon = utime.ticks_us()

   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("Distance: ", distance, "cm")

# Runs the code indefinitely
while True:
   ultra()
   utime.sleep(1)
"""
This one might be the right code...

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP14)

while True:
    print((sonar.distance,))
    time.sleep(0.1)
    
"""
