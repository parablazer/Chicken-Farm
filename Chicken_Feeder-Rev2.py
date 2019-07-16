#This program will controll the feeders in the chicken run.

import time, datetime, schedule,  os, RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
x = gpio.input(3, gpio.high)

def Release_chickens():
    gpio.output(12, 1)
    time.sleep(10)
    gpio.output(12, 0)
    return

def Feed_Chickens():
    gpio.output(16, 1)
    #sleep acts as safety if logic gate or limit switch fail
    time.sleep(10)
    gpio.output(16, 0)
    return

schedule.every().day.at("6:00").do(Release_chickens)
schedule.every().day.at("6:10").do(Feed_Chickens)
schedule.every().day.at("12:00").do(Feed_Chickens)

schedule.every(gpio.input(3, 1)).do(Release_chickens)

while True:
    schedule.run_pending()
    time.sleep(43200)
