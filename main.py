import cv2
import numpy as np

# read image
img = cv2.imread("dataset/photo/09203239.jpg")

# convert to LAB and extract L  channel
LAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
L = LAB[:,:,0]

# threshold L channel with triangle method
value, thresh = cv2.threshold(L, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
print(value)

value = value + 10
thresh = cv2.threshold(L, value, 255, cv2.THRESH_BINARY)[1]

# invert threshold and make 3 channels
thresh = 255 - thresh
mask = cv2.merge([thresh, thresh, thresh])

# save result
# cv2.imwrite('mask.jpg', thresh)

mask = cv2.blur(mask, (100, 100), 0)

a = 0.83
res = cv2.addWeighted(img, a,mask,1 - a,0)
cv2.imshow('output', res)
cv2.imshow('input', img)
cv2.imwrite("clear_data/photo/out.jpg", res)

cv2.waitKey(0)
cv2.destroyAllWindows()