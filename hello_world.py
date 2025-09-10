from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()

# The main program starts here.
prime_hub.display.number(99)
wait(1000)
print('Hello, Pybricks!')
def blink_red_light():
	prime_hub.light.blink(Color.RED, [100, 100])

blink_red_light()

# Initialize the motors connected to Port A and Port B
# Adjust Direction.CLOCKWISE or Direction.COUNTERCLOCKWISE based on your robot's build
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE")

# Initialize the drive base
# Parameters: left_motor, right_motor, wheel_diameter (mm), axle_track (mm)
# You will need to measure your robot's wheel diameter and axle track
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# 1. Drive forward for a certain distance
robot.drive(5000, 500) # Drive 200 mm forward


wait(10000)

