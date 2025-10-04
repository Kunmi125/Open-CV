import cv2

# Turning images into grayscale

image1 = cv2.imread("lesson 4/penguin.png")
cv2.imshow("Penguin", image1)
cv2.waitKey(0)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey penguin", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

image1 = cv2.imread("lesson 4/penguin.png")
(rows, columns) = image1.shape[:2]
r = cv2.getRotationMatrix2D((columns / 2, rows / 2), 45, 1)
result = cv2.warpAffine(image1, r, (columns, rows))
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()