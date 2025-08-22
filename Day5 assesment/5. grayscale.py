import cv2
image = cv2.imread('images.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_images.jpg',gray_image)