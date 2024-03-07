import numpy as np
import cv2

def lbp_pixel(img, center, x, y):
    value = 0
    if img[x][y] >= center:
        value = 1
    return value

def lbp_calculated_pixel(img, x, y):
    center = img[x][y]
    val_ar = []
    val_ar.append(lbp_pixel(img, center, x-1, y+1))     
    val_ar.append(lbp_pixel(img, center, x, y+1))       
    val_ar.append(lbp_pixel(img, center, x+1, y+1))     
    val_ar.append(lbp_pixel(img, center, x+1, y))       
    val_ar.append(lbp_pixel(img, center, x+1, y-1))     
    val_ar.append(lbp_pixel(img, center, x, y-1))       
    val_ar.append(lbp_pixel(img, center, x-1, y-1))     
    val_ar.append(lbp_pixel(img, center, x-1, y))       
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    return val

def lbp_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img_gray.shape
    img_lbp = np.zeros((height, width), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
    return img_lbp

image_path = "path_to_your_image.jpg"
img = cv2.imread(image_path)
lbp_result = lbp_image(img)
