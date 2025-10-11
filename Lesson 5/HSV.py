import cv2

# Turning BGR image into HSV
# BGR is normal image format
# HSV stands for Hue Saturation View

image1 = cv2.imread("Lesson 5/opm.jpg")
new_image = cv2.Canny(image1, 210, 245) # First number is lower value for the lower edges and second number is the higher value for the higher edges
cv2.imshow("One Punch!!!", image1)
cv2.imshow("New Punch!!!", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Format Change

import cv2

image1 = cv2.imread("Lesson 5/opm.jpg")
HSV_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)                 # cvtColor means convert color
cv2.imshow("One Punch!!!", image1)
cv2.imshow("New Punch!!!", HSV_image)
cv2.waitKey(0)
cv2.destroyAllWindows()