from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()

# The main program starts here.
prime_hub.display.number(11)
prime_hub.speaker.beep(150, 1250)
wait(1000)
print('Hello, Pybricks!')
