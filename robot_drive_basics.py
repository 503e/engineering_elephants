from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the hub
hub = PrimeHub()

# Initialize the motors connected to Port A and Port B
# Adjust Direction.CLOCKWISE or Direction.COUNTERCLOCKWISE based on your robot's build
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

# Initialize the drive base
# Parameters: left_motor, right_motor, wheel_diameter (mm), axle_track (mm)
# You will need to measure your robot's wheel diameter and axle track
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Initialize a color sensor if used, e.g., on Port C
# color_sensor = ColorSensor(Port.C)

# --- Robot Control Examples ---

# 1. Drive forward for a certain distance
robot.drive(5000, 500) # Drive 200 mm forward
wait(1000) # Wait for 1 second after the action completes

# 2. Turn in place for a certain angle
robot.turn(90) # Turn 90 degrees clockwise
wait(1000)

# 3. Drive at a continuous speed and turn rate
robot.drive(speed=100, turn_rate=0) # Drive straight at 100 mm/s
wait(2000) # Drive for 2 seconds

robot.drive(speed=100, turn_rate=30) # Drive forward while turning at 30 deg/s
wait(2000)

robot.stop() # Stop the drive base

# 4. Control individual motors
left_motor.run_angle(500, 360) # Run left motor at 500 deg/s for 360 degrees
right_motor.run_time(200, 3000) # Run right motor at 200 deg/s for 3000 milliseconds

# 5. Using sensors (example with ColorSensor, uncomment if used)
# while True:
#     reflection = color_sensor.reflection()
#     print(f"Reflection: {reflection}")
#     if reflection < 20: # Example: stop if reflection is below 20
#         robot.stop()
#         break
#     wait(100) # Wait for a short duration before checking again