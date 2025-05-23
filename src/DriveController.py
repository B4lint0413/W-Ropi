from buildhat import Motor
from WallDistance import GetWallError, IsTurning
import time
import math

steering = Motor('D')
drive = Motor('C')
wheel_rotation_distance = 17.6 #distance traveled by one rotation of the wheel
def getOrientation(previous, angle, distance):
    if angle == 0: # prevent zero division
        return 0
    
    steering_rad = math.radians(angle)
    wheelbase = 18.4 # space between the axles in cm
    turning_rad = wheelbase/math.tan(steering_rad)
    orientation = math.degrees(distance/turning_rad)
    current = previous + orientation
    if current > 90: # cos function changes sign above 90 and below -90
        return current-90
    elif current < -90:
        return current+90
    return current
'''
steering.run_to_position(30)
previous_orientation = 0
for i in range(3):
    pos = drive.get_position()
    drive.run_for_seconds(1)
    traveled = (drive.get_position() - pos)/360*wheel_rotation_distance
    orientation = getOrientation(previous_orientation, 30, traveled)
    print(orientation)
    time.sleep(5)
    previous_orientation = orientation
'''
pid = {"wall": {"p": 3, "i": 0.01, "d": 4.3}}
drive.start(40)
errorSum = 0
lastError = 0
start = time.time()
drive_rotation = drive.get_position()
previous_orientation = 0
degree = 0
steering.run_to_position(0,100)
while time.time()-start<6:
    distance = (drive.get_position()-drive_rotation)/360*wheel_rotation_distance
    drive_rotation = drive.get_position()
    orientation = getOrientation(previous_orientation, steering.get_aposition(), distance)
    error = GetWallError()*13*math.cos(math.radians(orientation)) # multiply by cos to get the actual distance from wall
    orientation_error = -orientation*0.5 # prevent perpendicularity with the wall 
    degree = error*pid["wall"]["p"]+errorSum*pid["wall"]["i"]+(error-lastError)*pid["wall"]["d"]+orientation_error
    print(degree)
    steering.run_to_position(degree, speed=100, blocking=True)
    errorSum += error
    lastError = error
    previous_orientation = orientation
drive.stop()
steering.stop()