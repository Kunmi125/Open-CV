'''import cv2

image1 = cv2.imread("Lesson 5/gvb.jpg")
new_image = cv2.Canny(image1, 200, 385)
cv2.imshow("One Puncchhhhh!!!!!", image1)
cv2.imshow("Newww Punch!!!!!!", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

image1 = cv2.imread("Lesson 5/gvb.jpg")
HSV_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)                 
cv2.imshow("One Punch!!!", image1)
cv2.imshow("New Punch!!!", HSV_image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


import cv2

image1 = cv2.imread("C:/Users\osuno/Desktop\Open CV/Lesson 5/ncity.jpg")

sp = (320, 0)   
ep = (380, 110)  
color = (125, 125, 255)
line_thickness = 5


sp2 = (380, 110)
ep2 = (440, 0)

final_image = cv2.line(image1, sp, ep, color, line_thickness)
final_image = cv2.line(image1, sp2, ep2, color, line_thickness)

cv2.imshow("Neon City", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()