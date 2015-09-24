""" Detect motion with an HC-SR501.

rpi     HC-SR501
===     ========
5v0 --- VCC
P24 --- OUT
GND --- GND

Tx to min, Sx to max.
"""
import RPi.GPIO as GPIO

INPUT = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT, GPIO.IN) #, GPIO.PUD_UP)

def _callback(channel):
    print "motion"

try:
    GPIO.add_event_detect(INPUT, GPIO.RISING, callback=_callback, bouncetime=200)
    raw_input("return to quit\n")
finally:
    GPIO.cleanup()
