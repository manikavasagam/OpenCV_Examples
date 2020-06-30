import cv2
import numpy as np

#img = cv2.imread('media/lena.jpg')
img = np.zeros([512, 512, 3], np.uint8)
img_height = img.shape[0]
img_width = img.shape[1]
img_channels = img.shape[2]

cv2.line(img, (0, 0), (255, 255),(255,0,0),5)

#cv2.imwrite('media/out.jpg', img)
cv2.arrowedLine(img, (img_width, img_height), (300, 300),(255,0,0),5)

cv2.rectangle(img, (0,0), (100,100),(0,0,255),3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Hello OpenCV",(10,100),font,2,(100,200,100),3)



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()