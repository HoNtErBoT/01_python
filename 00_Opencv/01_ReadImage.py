import cv2


image_path = r'D:\00_Project\03_Project 24-25\01_Software Code R&D\01_Python\01_EMBEDDED Course\RES\JEEP.jpg'


def readImg(file=r'D:\00_Project\03_Project 24-25\01_Software Code R&D\01_Python\01_EMBEDDED Course\RES\HUSKEY.jpg'):
    print(f'Reading image from a {file}')
    image = cv2.imread(file)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('HSV IMAGE', hsv_image)
    cv2.imshow('GRAY IMAGE', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    readImg()

