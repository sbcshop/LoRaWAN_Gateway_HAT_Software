import RPi.GPIO as GPIO
import time

# BCM pin numbering
BUTTON1 = 27  # Physical pin 13
BUTTON2 = 22  # Physical pin 15
LED1 = 23     # Physical pin 16
LED2 = 24     # Physical pin 18

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

def blink_leds(times=3, interval=0.2):
    for _ in range(times):
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(interval)

try:
    print("Press button 13 or 15 to blink LEDs.")
    while True:
        val1 = GPIO.input(BUTTON1)
        val2 = GPIO.input(BUTTON2)
        if GPIO.input(BUTTON1) == GPIO.LOW or GPIO.input(BUTTON2) == GPIO.LOW:
            print("Button 1:",val1)
            print("Button 2:",val2)
            blink_leds()
            
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
