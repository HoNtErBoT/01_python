import cv2


image_path = r'D:\00_Project\03_Project 24-25\01_Software Code R&D\01_Python\01_EMBEDDED Course\RES\JEEP.jpg'


def readImg(file=r'D:\00_Project\03_Project 24-25\01_Software Code R&D\01_Python\01_EMBEDDED Course\RES\HUSKEY.jpg'):
    print(f'Reading image from a {file}')
    image = cv2.imread(file)
    if image is None:
        print("Error: Could not load image.")
    else:
        cv2.imshow('Loaded Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()