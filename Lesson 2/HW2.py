import cv2


# Addition


image1 = cv2.imread("images/beautisky.jpg")
image2 = cv2.imread("images/sunrocks.jpg")
combined_image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
cv2.imshow("Beautiful Sky", image1)
cv2.waitKey(0)
cv2.imshow("Beautiful Landscape", image2)
cv2.waitKey(0)
cv2.imshow("Combined Image....", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2

# Subtraction

image1 = cv2.imread("images/star3.jpg")
image2 = cv2.imread("images/star2.jpg")
combined_image = cv2.subtract(image1, image2)
cv2.imshow("A star!", image1)
cv2.waitKey(0)
cv2.imshow("A star!!!", image2)
cv2.waitKey(0)
cv2.imshow("subtracted!!!", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2

# Saturation

image1 = cv2.imread("images/sss.jpg", 1)
b, g, r = cv2.split(image1)
cv2.imshow("Super Saiyan Brawlll!!!!", image1)
cv2.waitKey(0)


cv2.imshow("Blue Saturation", b)
cv2.waitKey(0)

cv2.imshow("Green Saturation", g)
cv2.waitKey(0)

cv2.imshow("Red Saturation", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

