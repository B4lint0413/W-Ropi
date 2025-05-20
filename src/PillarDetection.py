from picamera2 import Picamera2
import time
import numpy as np
import cv2

def MakeImg():
    cam = Picamera2()
    config = cam.create_still_configuration(main={"format": "RGB888", "size": (640, 480)})
    cam.configure(config)
    cam.start()
    time.sleep(2)
    img = cam.capture_array("main")
    cam.stop()
    return img

# The coordinates of the pillar's point to the left (as we bypass on the left)
def LeftEnd(points):
    leftmost = points[0]
    for point in points:
        if point[0][0] < leftmost[0][0]:
            leftmost = point
    return leftmost[0]

img = cv2.cvtColor(MakeImg, cv2.COLOR_RGB2HSV)

'''
cv2.imshow("asd", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
'''

# Define color ranges
lwrGreen = np.array([35,100,50])
upprGreen = np.array([90,255,255])
'''
lwrRed = np.array([40,50,50])
upprRed = np.array([40,50,50])
'''
#green_masked = cv2.bitwise_and(img,img, mask=green_mask)

# Mask the image and find contours
green_mask = cv2.inRange(img, lwrGreen, upprGreen)
green_contour, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Identify the pillars from the contours
pillars = []
for cnt in green_contour:
    area = cv2.contourArea(cnt)
    if area > 1500:
        approx = cv2.approxPolyDP(cnt, 0.05 * cv2.arcLength(cnt, True), True)
        cv2.polylines(img, [approx], True, (0,0,255), 3)
        pillars.append({"point": LeftEnd(approx), "area": area})

# cv2.imshow("asd", cv2.cvtColor(green_masked, cv2.COLOR_HSV2RGB))
print("Pillars detected: ", pillars)
cv2.imshow("Green pilars detected", cv2.cvtColor(img, cv2.COLOR_HSV2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()