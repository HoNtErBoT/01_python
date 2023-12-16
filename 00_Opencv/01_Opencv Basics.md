# Install opencv

Open Source Computer Vision Library, is an open-source computer vision and machine learning software library. It was originally developed by Intel in 1999 and has since become one of the most widely used libraries in the field of computer vision. OpenCV is written in C and C++, but it provides interfaces for Python, Java, and other languages. The library is designed to provide a common infrastructure for computer vision applications and to accelerate the development of real-time applications. OpenCV offers a wide range of functionalities related to image and video processing. To install Opencv we have to use the folloeing commands

```diff

pip install opencv-python          # installs the main OpenCV package
pip install opencv-contrib-python  # installs additional contributions that are not included in the main package

```
![image](https://github.com/HoNtErBoT/01_python/assets/109785046/70a8eb08-03f6-4f4b-a6b9-ac743810b40d)

# Reading images 

```diff

import cv2                          # import opencv Library
img = cv2.imread('img/1.jpg')       # Read image from the folder
cv2.imshow('car', img)              # Display the image
cv2.waitKey(0)                      # Wait till a key press

```

In the above Python code using the OpenCV library, the first line imports the OpenCV library, which is used for computer vision tasks. The second line reads an image ('1.jpg') from a folder called 'img.' The third line displays the image with the window title 'car' using the cv2.imshow function.

The cv2.waitKey(0) function in the provided code is a command that makes the program wait indefinitely for a keyboard event. In simple terms, it pauses the execution of the script at this point and keeps the window displaying the image open until a key on the keyboard is pressed. The argument '0' specifies that the program will wait for an indefinite amount of time for a key press. Once a key is pressed, the program proceeds to the next line of code and closes the image window. This functionality is commonly used to view an image or video and allows the user to keep the window open until they decide to close it by pressing a key.

![image](https://github.com/HoNtErBoT/01_python/assets/109785046/caecd907-dc1b-4093-b33f-3ef710c3dc8c)

# Reading Video

```diff

import cv2
video_path = 'img/car.mp4'
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
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


Here's a brief summary of your code:

1 - Open the video file using cv2.VideoCapture.
2 - Check if the video file opened successfully.
3 - Retrieve and print the video resolution and frames per second.
4 - Set the desired width and height for the displayed video frames.
5 - Enter a loop to read and display each frame.
6 - Resize each frame to the desired width and height.
7 - Display the resized frame using cv2.imshow.
8 - Break the loop if the 'q' key is pressed.
9 - Release the video capture object and close the display window when the loop ends.

```

![ezgif com-video-to-gif-converted](https://github.com/HoNtErBoT/01_python/assets/109785046/a2a3ac33-7c15-4fd3-90a5-375083165c48)


