from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


hub = PrimeHub()

mV = hub.battery.voltage()
print("Battery voltage (mV):", mV)
Mv = mV-6400
print("Battery voltage left (Mv):", Mv)
X = Mv/2000
Y = X*100
print(f"Battery percentage: {Y}%")

hub.display.number(Y)
wait(10000)