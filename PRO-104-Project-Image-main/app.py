import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
cv2.putText(img, "Mercury", (100,150), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv2.putText(img, "Venus", (200,150), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
cv2.putText(img, "Earth", (300,150), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)



cv2.imshow("output", img)
cv2.waitKey(3000)

