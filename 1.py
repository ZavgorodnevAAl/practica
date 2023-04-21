import cv2
import numpy as np

# загрузка изображений
img1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
mask = cv2.imread('mask.jpg', cv2.IMREAD_GRAYSCALE)
mask = cv2.blur(mask, (100, 100), 0)

a = 0.83
dst = cv2.addWeighted(img1, a,mask,1 - a,0)
cv2.imshow('m1', dst)
cv2.imshow('m2', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()