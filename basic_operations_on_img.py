import cv2

img = cv2.imread('media/messi5.jpg')
img2 = cv2.imread('media/lena.jpg')

print(img.shape)
print(img.size)
print(img.dtype)


b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))


ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

dst = cv2.addWeighted(img, .5, img2, .5, 0)

cv2.imshow("messi", dst)

cv2.waitKey()
cv2.destroyAllWindows()