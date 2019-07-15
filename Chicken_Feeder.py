#This program will controll the feeders in the chicken run.

import datetime, os, schedule, RPi.GPIO as gpio

Sunrise = gpio.input(25, gpio.high)

global TIME
date = datetime.datetime.now()
while True:
        Feed_Chickens()



def Feed_Chickens():
    global TIME
    gpio.output(18, gpio.high)
    time.sleep(10)
    gpio.output(18, gpio.low)
    return;
