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

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
robot.use_gyro(True)
robot.straight(distance=730, then=Stop.HOLD, wait=True) #drive forward on approach to 3 bolders
robot.arc(radius=-100, angle=95, wait=True) # arched movement to activate bolder fall and table flip
robot.turn(-90, wait=True) # left turn to align for movement around mission 9 obstacle
robot.straight(distance=100, then=Stop.HOLD, wait=True) # straight approach to mission 9
robot.arc(radius=240, angle=55, wait=True) #circle to sweep across the "whats on sale" portion of mission 9
robot.straight(distance=225, then=Stop.HOLD, wait=True) #straight movement to activate the dropping of the scale table
robot.arc(radius=250, angle=190, wait=True) #arch approach to align for the push on obstacle 9
robot.turn(75, wait=True) #final turn prior to pushing of the plate on obstacle 9
robot.straight(distance=190, then=Stop.HOLD, wait=True) # push movement to raise the bed on obstacle 9 and drop the bucket on obstacle 10
robot.straight(distance=-250, then=Stop.HOLD, wait=True) #reverse to leave obstacles 9 and 10
robot.turn(55, wait=True) #right turn to begin approach for final pull on back of obstacle 10
robot.straight(distance=455, then=Stop.HOLD, wait=True) #straight approach to position toward the back of obstacle 10
robot.turn(-80, wait=True) #turn to align hook to pull loop from obstacle 10
robot.straight(distance=125, then=Stop.HOLD, wait=True) #small movement forward to engage hook and loop
robot.turn(30, wait=True)#right turm to pull loop on obsticle 10
robot.arc(angle=50, radius=-900)#returm home with obsticle 10
