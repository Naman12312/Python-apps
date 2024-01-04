import cv2
# img = cv2.imread("/home/goldarmgang/Downloads/f28.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("/home/goldarmgang/Downloads/f28.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("f28gray.png", img)
imgcropped = img[0:244, 344:987]
cv2.imshow("Hello", imgcropped)
cv2.waitKey(0)