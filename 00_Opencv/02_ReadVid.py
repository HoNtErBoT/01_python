import cv2
video_path = 'RES/VID.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Video Resolution: {width} x {height}")
print(f"Frames Per Second: {fps}")
desired_width, desired_height = 640, 320
while True:
    ret, frame = cap.read()
    if not ret:
        print("Video playback complete.")
        break
    frame = cv2.resize(frame, (desired_width, desired_height))
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', frame)
    cv2.imshow('GRAY IMAGE', gray_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
