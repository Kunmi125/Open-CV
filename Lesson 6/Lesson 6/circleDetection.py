import cv2
import numpy as np

# The HoughCircles function is used to detect circles in an image using the Hough Circle transform algorithm
# This alsgorithm is particularly effective in detecting circular shapes even in the presence of noise or partial occlusion

eye = cv2.imread("Lesson 6/eye.jpg")

# convert to grayscale
gscale = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

# Why grayscale -> HoughCircle needs single channel intensity (single color) instead of 3 colors e.g bgr


# Blurring the image
blurred = cv2.blur(gscale,(3,3))

# Blurring reduces noise and small details so the Hough algorithm is less sensitive to spurios edges


# Detect the circle - (Hough Circles)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 50, minRadius = 1, maxRadius= 40)



# Parameters above:
# Blurred - > image

# cv2.HOUGH_GRADIENT -> Uses a modified Hough transformation where the image gradient is used to detect circles

# dp = 1: This parameter is the inverse ratio of the accumulator resolution to the image resolution

# - For example if dp = 1, the accumulator has the same resolution as the input gradient
# - If dp = 2, the accumulator has half th resolution of the input image

# minDistance = 20 -> Minimum distance between the centers of the detected circles
# - If the distance between the two centres is less than this value, only the stringer one is returned


'''param1: Gradient value used in the edge detction process
This parameter depends on the method used for circle detection
param2: Accumulaor threshhold value. It determines the minimum number of votes 
required for a candidate circle to be considered a circle '''

# minRadius -> 1 to 40. Minimum radius of the circles to be detected


# detecting whether the circles are found
if circles is not None:       #(If there are circles)
    circles = np.uint16(np.around(circles))  # (Rounds the value)

# Draw a circle
for i in circles[0,:]:
    a,b,r = i[0], i[1], i[2]
    cv2.circle(eye, (a,b), r, (0,0, 255), 2) # Drawing the detected circle
    cv2.circle(eye, (a,b), 1, (0,0, 255), 2)
    cv2.imshow("eye", eye)

cv2.waitKey(0)
cv2.destroyAllWindows()


