import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     # Load the cascade
cap = cv2.VideoCapture(0)                                   # To capture video from webcam.

while True:
    _, img = cap.read()                                     # Read the frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)     # Detect the faces
    count = 0                                               # Decalare Face count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle on face
        count += 1                                                  # Increment count

    MSG = "face count => "+ str(count)                      # set MSG with Face count
    print(MSG)                                              # Print Face count MSG on terminal
    cv2.rectangle(img, (0, 0), (250, 35), (0, 0, 0), -1)    # Set black back ground for text
    cv2.putText(                                            # Set MSG on Video
        img=img,
        text=MSG,
        org=(15, 25),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=0.8,
        color=(125, 246, 55),
        thickness=1
    )
    cv2.imshow('img', img)                                  # Display
    k = cv2.waitKey(30) & 0xff                              # Stop if escape key is pressed
    if k == 27:
        break