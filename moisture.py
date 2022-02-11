import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("dry", GPIO.IN)
    else:
        print("wet!", GPIO.IN)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=1)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    time.sleep(1)