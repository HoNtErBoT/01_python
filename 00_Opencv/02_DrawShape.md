# Custom Rectangle Box

During this journey of learning OpenCV in Python, I have realised that we have to do some special signatures in all our codes, so I decided to create a custom detection rectangle box to use whenever I need face detection, recognition, or custom object detection. For that, I realise I have to learn how to draw basic shapes in an open CV. While drawing a rectangle and straight line, I assume I can achieve my goal.

![image](https://github.com/HoNtErBoT/01_python/assets/109785046/6deb08ad-0a89-4246-83c4-d1d3ef27339c)

# Draw straight line 

```diff

# Read Image
import cv2                           # import opencv Library
img = cv2.imread('img/op.png')       # Read image from the folder


# Get Image Dimensions
image_height, image_width, _ = img.shape
print(f"Image Size: {image_width} x {image_height}")

# Draw a straight line
start_point = (100, 100)
end_point   = (400, 400)
color_front = (0, 0, 255)
cv2.line(img, start_point, end_point, color_front, thickness=5)

cv2.imshow('HoNtEr OUTPUT Window', img)               # Display the image
cv2.waitKey(0)                      # Wait till a key press

```

- **cv2:** This refers to the OpenCV library.
- **line:** This is the function in OpenCV used to draw a line on an image.
- **img:** This is the image on which the line will be drawn. It's the target image.
- **start_point:** This is a tuple specifying the starting coordinates (x, y) of the line.
- **end_point:** This is a tuple specifying the ending coordinates (x, y) of the line.
- **color_front:** This is a tuple representing the color of the line in BGR (Blue, Green, Red) format. Each color component is an integer ranging from 0 to 255.
- **thickness:**This is an optional parameter that sets the thickness of the line. In the provided example, the thickness is set to 5 pixels.
### OUTPUT 

![image](https://github.com/HoNtErBoT/01_python/assets/109785046/954e5ddd-3687-48a5-a51e-ac91e73df92a)
