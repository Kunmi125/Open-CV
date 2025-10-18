import cv2


# Draw Line

image1 = cv2.imread("Lesson 5/city.png") 

#Left line

sp = (320, 0)   # sp = Start Point
ep = (380, 110)  # ep = End Point
color = (125, 125, 255)
line_thickness = 8

# Right line

sp2 = (380, 110)
ep2 = (440, 0)


final_image = cv2.line(image1, sp, ep, color, line_thickness)
final_image = cv2.line(image1, sp2, ep2, color, line_thickness)

cv2.imshow("Gotham City", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Draw rectangle

import cv2

image1 = cv2.imread("Lesson 5/sunflower.png") 

# start and end coordinate

start_coordinate = (20, 80)
end_coordinate = (250, 650)
color = (125, 125, 255)
line_thickness = -4

final_image = cv2.rectangle(image1, start_coordinate, end_coordinate, color, line_thickness)

cv2.imshow("Gotham City", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()