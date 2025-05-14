from gpiozero import Servo
from time import sleep

servo = Servo(25)

try:
        while True:
                servo.min()
                sleep(0.5)
                .mid()
                sleep(0.5)
                .max()
                sleep(0.5)
except KeyboardInterrupt:
        print("Program stopped")