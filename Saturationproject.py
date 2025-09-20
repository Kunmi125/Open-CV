import cv2

image1 = cv2.imread("images/goku.webp", 1)
b, g, r = cv2.split(image1)
cv2.imshow("Goku!!!", image1)
cv2.waitKey(0)

cv2.imshow("Blue Saturation!!!", b)
cv2.waitKey(0)

cv2.imshow("Green Saturation!!!", g)
cv2.waitKey(0)

cv2.imshow("Red Saturation!!!", r)
cv2.waitKey(0)
cv2.destroyAllWindows()