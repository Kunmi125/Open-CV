'''import cv2

# Resizing images

image1 = cv2.imread("Lesson 3/penguin.png")
image2 = cv2.resize(image1, (200, 300)) # 1) A tuple is the purple bracket which the computer alr knows is a tuple  2) Values are width and height inside the bracket
cv2.imshow("Original Penguin!!!", image1) 
cv2.waitKey(0)
cv2.imshow("Resized Penguin!!!", image2) 
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Eroding images

image1 = cv2.imread("Lesson 3/penguin.png", 1)
kernel = np.ones((5, 5), np.uint8)
new_image = cv2.erode(image1, kernel)
cv2.imshow("Eroded Penguin", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


import cv2

# Blurred image - Gaussian Blur

image1 = cv2.imread("Lesson 3/penguin.png", 1)
g_blur = cv2.GaussianBlur(image1, (7, 7), 0) # Tuple values can only be in odd numbers
cv2.imshow("Gaussian Blur", g_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Blurred image - Median Blur 

image2 = cv2.imread("Lesson 3/penguin.png", 1)
m_blur = cv2.medianBlur(image2, 5) 
cv2.imshow("Median Blur", m_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Blurred image - Bilature Blur 

image3 = cv2.imread("Lesson 3/penguin.png", 1)
b_blur = cv2.bilateralFilter(image3, 9, 75, 75) # To tell the computer how much of the image should be filtered
cv2.imshow("Bilature Blur", b_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()