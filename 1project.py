'''import cv2


# Colured Image
image1 = cv2.imread("images/pikacoat.png", cv2.IMREAD_COLOR) # 1 the same as cv.2_IMREAD_COLOR
cv2.imshow("Pika!!", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1 = cv2.imread("images/pikacoat.png", 1)
cv2.imshow("Pika!!", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()




#Black And White Image
image2 = cv2.imread("images/pikacoat.png", cv2.IMREAD_GRAYSCALE) # 0 the same as cv.2_IMREAD_GRAYSCALE
cv2.imshow("Pika!!", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread("images/pikacoat.png", 0)
cv2.imshow("Pika!!", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Unchanged Image
image2 = cv2.imread("images/pikacoat.png", cv2.IMREAD_UNCHANGED)
cv2.imshow("Pika!!", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread("images/pikacoat.png", -1) # -1 the same as cv.2_IMREAD_UNCHANGED
cv2.imshow("Pika!!", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



import cv2
import os

saved_directory = "C:\\Users\\osuno\\Desktop\\Open CV\\images"



# Colured Image
image1 = cv2.imread("images/pikacoat.png", 0) 
cv2.imshow("Pika!!", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

os.chdir(saved_directory)  # Change directory function
cv2.imwrite("Pikachublackandwhite.png", image1)
print("Saved Successfully!")
