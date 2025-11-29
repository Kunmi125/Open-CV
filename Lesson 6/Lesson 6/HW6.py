import cv2

image = cv2.imread("C:/Users/osuno/Desktop/Open CV/Lesson 6/people.jpg")

# HOG Person Detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Perform detection
(rects, weights) = hog.detectMultiScale(image, winStride= (8, 8), padding = (8 ,8), scale = 1.05)

print("The number of persons detected are ", len(rects))

for  (x,y,w,h) in rects:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("HOG + SVM People Detector", image)
cv2.waitKey(0)
cv2.destroyAllWindows()