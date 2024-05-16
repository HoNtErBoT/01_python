import cv2


def drawRect(x1, y1, x2, y2):
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)
    x = x2-x1
    y = y2-y1
    x = int(0.2 * x)
    y = int(0.2 * y)

    cv2.line(img, (x1, y1), (x1+x, y1), (224, 25, 184), thickness=4)
    cv2.line(img, (x1, y1), (x1, y1 + y), (224, 25, 184), thickness=4)

    cv2.line(img, (x2, y1), (x2 - x, y1), (224, 25, 184), thickness=4)
    cv2.line(img, (x2, y1), (x2, y1 + y), (224, 25, 184), thickness=4)

    cv2.line(img, (x1, y2), (x1, y2 - y), (224, 25, 184), thickness=4)
    cv2.line(img, (x1, y2), (x1 + x, y2), (224, 25, 184), thickness=4)

    cv2.line(img, (x2, y2), (x2 - x, y2), (224, 25, 184), thickness=4)
    cv2.line(img, (x2, y2), (x2, y2 - y), (224, 25, 184), thickness=4)


img = cv2.imread('RES/HUSKEY.jpg')
drawRect(80, 80, 180, 200)
cv2.imshow('OUTPUT', img)
cv2.waitKey(0)
