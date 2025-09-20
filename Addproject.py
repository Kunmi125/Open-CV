'''import cv2

#Addition of images (COMBINATION)

image1 = cv2.imread("images/ruins.jpg")
image2 = cv2.imread("images/galaxy.jpg")
Combined_image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
cv2.imshow("Ruins", image1)
cv2.waitKey(0)
cv2.imshow("Galaxies", image2)
cv2.waitKey(0)
cv2.imshow("Combined Image...", Combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


import cv2

#Subtraction of images (COMBINATION)

image1 = cv2.imread("images/star.jpg")
image2 = cv2.imread("images/diamondot.jpg")
Combined_image = cv2.subtract(image1, image2 )
cv2.imshow("Diamond", image1)
cv2.waitKey(0)
cv2.imshow("Star", image2)
cv2.waitKey(0)
cv2.imshow("Subtracted Image...", Combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()