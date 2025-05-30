from buildhat import Motor
from WallDistance import GetWallError, IsTurning
import math

steering = Motor('D')
drive = Motor('C')
wheel_rotation_distance = 17.6 #distance traveled by one rotation of the wheel
def getOrientation(previous, angle, distance):
    if angle == 0: # prevent zero division
        return previous
    
    steering_rad = math.radians(angle)
    wheelbase = 18.4 # space between the axles in cm
    turning_rad = wheelbase/math.tan(steering_rad)
    orientation = math.degrees(distance/turning_rad)
    current = previous + orientation
    if current > 50: # cos function changes sign above 90 and below -90
        return current-90
    elif current < -50:
        return current+90
    return current
try:
    pid = {"wall": {"p": 3, "i": 0.01, "d": 4.3}}
    drive.run_for_seconds(18, speed=30, blocking=False)
    errorSum = 0
    lastError = 0
    drive_rotation = drive.get_position()
    previous_orientation = 0
    orientation = 0
    degree = 0
    still_turning = 0
    steering.run_to_position(0,100)
    while drive.get_speed()>10:
        try:
            distance = (drive.get_position()-drive_rotation)/360*wheel_rotation_distance
            drive_rotation = drive.get_position()
            '''
            if IsTurning() == -1:
                still_turning += 1
                if still_turning == 3:
                    orientation += 90
            elif IsTurning() == 42:
                still_turning = 0
            '''
            orientation = getOrientation(previous_orientation, steering.get_aposition(), distance)
            print(orientation)
            error = GetWallError()*16*math.cos(math.radians(orientation)) # multiply by cos to get the actual distance from wall
            orientation_error = -orientation*0.5#**3*(0.5*(10**-4)) # prevent perpendicularity with the wall 
            degree = error*pid["wall"]["p"]+errorSum*pid["wall"]["i"]+(error-lastError)*pid["wall"]["d"]+orientation_error
            degree = 90 if degree>90 else degree
            degree = -90 if degree<-90 else degree
            steering.run_to_position(degree, speed=100, blocking=True)
            errorSum += error
            lastError = error
            previous_orientation = orientation
        except:
            continue
    drive.stop()
    steering.stop()
except Exception as e:
    print(e)
    drive.stop()
    steering.stop()