import cv2
from matplotlib import pyplot as plt

img = cv2.imread('media/lena.jpg', -1)
#cv2.imshow("img", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#to hide the x and y axis labels
#plt.xticks([]), plt.yticks([])

plt.imshow(img)
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()