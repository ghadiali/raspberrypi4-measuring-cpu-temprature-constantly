#Python Code to Measure Cpu Temprature in Raspberry Pi4 using vcgencmd function.

import os
import time
os.system('clear')
def measure_temp():
    temp= os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=", ""))

while True:
    os.system('clear')
    print("The Current CPU Temprature is:")
    print(measure_temp())
    time.sleep(1)

