#first project
#blinked leds

from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led= True
    time.sleep(.5)
    cp.red_led= False
    time.sleep(.5)
    #neopixels time!
    cp.pixels[0] = (0, 255, 0) #green
    time.sleep(.5)
    cp.pixels[0] = (0, 0, 0) #all off
    time.sleep(.5)
    cp.pixels[1] = (0, 0, 255) #green
    time.sleep(.5)
    cp.pixels[1] = (0, 0, 0) #all off
    time.sleep(.5)
