import cv2

center = (300, 250)         # Center coordinates of the ellipse
axes = (150, 100)           # Length of the major and minor axes
angle = 30                  # Angle of rotation of the ellipse in degrees
startAngle = 0              # Starting angle of the elliptic arc in degrees
endAngle = 360              # Ending angle of the elliptic arc in degrees
color = (255, 0, 0)         # Blue color in BGR
thickness = 2               # Thickness of the ellipse outline (use -1 for a filled ellipse)

img = cv2.imread('RES/HUSKEY.jpg')
img = cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
cv2.imshow('OUTPUT', img)
cv2.waitKey(0)
