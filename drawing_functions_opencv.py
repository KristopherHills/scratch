import cv2

img = cv2.imread('lena.jpg', 0)

#color is BGR
img = cv2.line(img, (0,0), (255,255), (255, 0, 0) )

cv2.imshow('image', img)

first, second = "hello"

print(first, second)

cv2.waitKey(0)
cv2.destoryAllWindows()