from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
main_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
robot.use_gyro(True)
robot.turn(35)
main_motor.run_angle(600, -825, then=Stop.HOLD, wait=False)#move attachment down
robot.settings(straight_speed=400,straight_acceleration=300, turn_rate=500, turn_acceleration=350)#adjusts the speed that the robot runs at
robot.arc(radius=1250, angle=-35, wait=True)

robot.turn(-20)
robot.straight(-150,wait=True)
robot.turn(-40)
main_motor.run_angle(600, 825, then=Stop.HOLD, wait=True)
robot.turn(-135)
robot.arc(radius=-1425, angle=-25, wait=True)
robot.turn(70)
robot.straight(-200)
import Menu_Control