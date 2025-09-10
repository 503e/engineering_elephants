from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color

# Set up all devices.
prime_hub = PrimeHub()

# The main program starts here.
prime_hub.display.number(99)
wait(1000)
print('Hello, Pybricks!')
def blink_red_light():
	prime_hub.light.blink(Color.RED, [100, 100])

blink_red_light()

wait(10000)