# do ratunkowego, ale ie testowalismy
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setuo(16, GPIO.OUT)
# while 1:
# 	GPIO.output(16, 1)
# 	time.sleep(1)
# 	GPIO.output(16, 0)
# 	time.sleep(1)

# open wrt

# dzialajace gpioled1
import gpiod
import time

chip = gpiod.Chip('gpiochip0')
prt = chip.get_lines([40])
prt.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

for i in range(10):
	prt.set_values([1])
	time.sleep(1)
	prt.set_values([0])
	time.sleep(1)

# dzialajace gpioled2
# import gpiod
# import time
# import math

# chip = gpiod.Chip('gpiochip0')
# prt = chip.get_lines([16])
# prt.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

# tmp = 1/10**3
# x = 0
# while x<20:
# 	prt.set_values([0])
# 	time.sleep((math.sin(x)+1)/2*tmp)
# 	prt.set_values([1])
# 	time.sleep((1 - (math.sin(x)+1)/2)*tmp)
# 	x += tmp*2
