from buildhat import DistanceSensor

left = DistanceSensor('A', threshold_distance=200)
right = DistanceSensor('B', threshold_distance=200)

def GetWallError():
    ldist = left.get_distance()
    rdist = right.get_distance()
    ldist = 2000 if ldist == -1 else ldist
    rdist = 2000 if rdist == -1 else rdist
    return (rdist-ldist)/900

def IsTurning():
    ldist = left.get_distance()
    rdist = right.get_distance()
    if ldist == -1 and rdist != -1:
        return -1
    elif rdist == -1 and ldist != -1:
        return 1
    elif rdist != -1 and ldist != -1:
        return 42
    return 0
    
