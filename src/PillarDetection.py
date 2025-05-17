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

img = cv2.cvtColor(MakeImg(), cv2.COLOR_RGB2HSV)
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
lwrGreen = np.array([40,50,50])
lwrGreen = np.array([40,50,50])
lwrGreen = np.array([40,50,50])
lwrGreen = np.array([40,50,50])
'''
green_mask = cv2.inRange(img, lwrGreen, upprGreen)
green_masked = cv2.bitwise_and(img,img, mask=green_mask)
'''
green_contour, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in green_contour:
    if cv2.contourArea(cnt) > 500:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x-w, y), (x, y + h), (0, 255, 0), 3)
        cv2.polylines(img, [approx], True, (0,0,255), 3)
   '''         
cv2.imshow("asd", cv2.cvtColor(green_masked, cv2.COLOR_HSV2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()