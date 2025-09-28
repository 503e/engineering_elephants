from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

hub = PrimeHub()
controller = XboxController()

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

while True:
    # Get the joystick values from the Xbox controller
    steering_input = controller.joystick_left()[0]  # Left joystick X-axis
    throttle_input = controller.joystick_left()[1]  # Left joystick Y-axis
    

    robot.drive(throttle_input, steering_input)

    wait(10)  # Small delay to prevent overwhelming the CPU