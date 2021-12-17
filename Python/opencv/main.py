import cv2
import random

img = cv2.imread('assets/girl.jpg', -1)

for i in range(100):
    for j in range(img.shape[1]):
        #print(img[i][j])
        img[i][j] = [random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)]

# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv2.imwrite('assets/new_img.jpg',img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
