from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController
main_motor2 = Motor(Port.E, Direction.CLOCKWISE)
main_motor2.run_angle(10000, 55, then=Stop.HOLD, wait=True)
main_motor2.run_angle(10000, -55, then=Stop.HOLD, wait=True)
main_motor2.run_angle(10000, 55, then=Stop.HOLD, wait=True)
main_motor2.run_angle(10000, -55, then=Stop.HOLD, wait=True)
main_motor2.run_angle(10000, 55, then=Stop.HOLD, wait=True)
main_motor2.run_angle(10000, -55, then=Stop.HOLD, wait=True)