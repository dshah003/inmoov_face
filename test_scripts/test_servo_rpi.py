import sys
import RPi.GPIO as GPIO
from time import sleep

args = sys.argv

# Check if at least two arguments are provided (including the script name)
if len(args) >= 2:
    pin_number = int(args[1])  # Get the first argument (Pin number)
    angle = int(args[2])   # Get the second argument (angle)

    print("Rotating Servo attached at BOARD pin: " + str(pin_number) +" by angle : " + str(angle))
else:
    print("Please provide Pin number and angle as command-line arguments.")
    print("Example usage: python3 test_servo_rpi.py 11 90")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.OUT)
pwm=GPIO.PWM(pin_number, 50)
pwm.start(7.5)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(pin_number, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(pin_number, False)
	pwm.ChangeDutyCycle(0)

SetAngle(angle)
pwm.stop()

GPIO.cleanup()


