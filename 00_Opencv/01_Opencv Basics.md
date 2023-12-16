# Install Opencv

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

![image](https://github.com/HoNtErBoT/01_python/assets/109785046/caecd907-dc1b-4093-b33f-3ef710c3dc8c)



