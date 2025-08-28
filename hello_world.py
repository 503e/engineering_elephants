from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()

# The main program starts here.
prime_hub.display.number(6)
prime_hub.speaker.beep(85, 2000)
prime_hub.speaker.beep(185, 1000)
print('Hello, Pybricks!')
