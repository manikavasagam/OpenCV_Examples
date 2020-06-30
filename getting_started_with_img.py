import cv2

img = cv2.imread('media/lena.jpg',  0)

#print(img)

cv2.imshow( "image", img)
key = cv2.waitKey(5000)

if key == 27 :
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena.png', img)
    cv2.destroyAllWindows()
