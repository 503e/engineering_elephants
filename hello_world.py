from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Port


# Set up all devices.
prime_hub = PrimeHub()

# Initialize a motor on Port A
my_motor = Motor(Port.A)
lg_motor = Motor(Port.C)

# The main program starts here.
prime_hub.display.number(6)
prime_hub.speaker.beep(85, 2000)
prime_hub.speaker.beep(185, 1000)

my_motor.run_time(500, 2000)
lg_motor.run(1000)
wait(3000)
lg_motor.stop()



print('Hello, Pybricks!')
