import cv2


def drawRect(x1, y1, x2, y2):
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)


img = cv2.imread('RES/HUSKEY.jpg')
drawRect(80, 80, 180, 200)
cv2.imshow('OUTPUT', img)
cv2.waitKey(0)
