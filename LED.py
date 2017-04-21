import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
for i in range(1,10):
	print 'LED ON'
	GPIO.output(4,GPIO.HIGH)
	time.sleep(1)
	print 'LED OFF'
	GPIO.output(4,GPIO.LOW)
	time.sleep(1)
