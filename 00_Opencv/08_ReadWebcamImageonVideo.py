import cv2


text = "Press q key to exit"
position = (50, 50)  # Bottom-left corner of the text (x, y)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 255, 0)  # Green color in BGR
thickness = 2
line_type = cv2.LINE_AA

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv2.putText(img, text, position, font, font_scale, color, thickness, line_type)
    cv2.imshow('OUTPUT', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
