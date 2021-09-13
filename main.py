#################################################
# Main (Part of PyPiCount)
# Version 0.1.0
# Julie Butler Hartley (Created for Carlos Unda)
# Date Created: September 12, 2021
# Last Modified: September 12, 2021
# Python2 with Tkinter and time packages required
#################################################
#import RPi.GPIO as GPIO
import time
from Tkinter import *

button = 31

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(button, GPIO.IN)

# GPIO.input(channel), GPIO.output(channel, state)

# Counter 1: Add X every second
# Counter 2: Add 1 given input to pin
# GUI with change value of X and reset to zero
# Photo resister and light source


X = 5


root = Tk()
time1 = ''
previousCounter1 = 0
previousCounter2 = 0
clock = Label(root, font=('times', 20, 'bold'), bg='white')
counter1 = Label(root, font=('times', 20, 'bold'), bg='white')
counter2 = Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
counter1.pack(fill=BOTH, expand=1)
counter2.pack(fill=BOTH, expand=1)
 
def tick():
    global time1
    global previousCounter1
    global previousCounter2

    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    #time2 = time.strftime('%S')
    # if time string has changed, update it
    if time2 != time1:
        previoustime = time1
        time1 = time2
        clock.config(text="Current Time: " + time2)
        counter1Value = previousCounter1 + X
        previousCounter1 = counter1Value
        counter1.config(text="Counter 1: " + str(counter1Value))
        if counter1Value % 2 == 0:
        	counter2Value = previousCounter2 + 1
        	previousCounter2 = counter2Value
        	counter2.config(text="Counter 2: " + str(counter2Value))


    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
 
tick()
root.mainloop(  )