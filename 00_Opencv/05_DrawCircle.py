import cv2

center = (280, 150)     # Center coordinates of the circle
radius = 100            # Radius of the circle
color = (0, 0, 255)     # Red color in BGR
thickness = 2           # Thickness of the circle outline (use -1 for a filled circle)


img = cv2.imread('RES/HUSKEY.jpg')
img = cv2.circle(img, center, radius, color, thickness)
cv2.imshow('OUTPUT', img)
cv2.waitKey(0)
