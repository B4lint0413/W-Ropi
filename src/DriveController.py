from buildhat import Motor
from WallDistance import GetWallError, IsTurning
import time
import math

steering = Motor('D')
drive = Motor('C')
pid = {"wall": {"p": 2, "i": 0.5, "d": 2.5}}
drive.start(30)
errorSum = 0
lastError = 0
start = time.time()
while time.time()-start<8:
    error = GetWallError()*15
    degree = error*pid["wall"]["p"]+errorSum*pid["wall"]["i"]+(error-lastError)*pid["wall"]["d"]
    print(degree)
    steering.run_to_position(degree, 100)
    errorSum += error
    lastError = error
drive.stop()
steering.stop()
'''