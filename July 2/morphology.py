#code for opening and closing

import cv2
import numpy as np
import matplotlib.pyplot as plt



def dilate(image, kernel):
    output = np.zeros_like(image)
    pad_height = kernel.shape[0] // 2
    pad_width = kernel.shape[1] // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            output[i, j] = np.max(region * kernel)
    
    return output

def erode(image, kernel):
    output = np.zeros_like(image)
    pad_height = kernel.shape[0] // 2
    pad_width = kernel.shape[1] // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=1)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            output[i, j] = np.min(region * kernel)
    
    return output


def apply_closing(image, kernel):
    dilated = dilate(image, kernel)
    closed = erode(dilated, kernel)
    return closed


def apply_opening(image, kernel):
    erosion = erode(image, kernel)
    open = dilate(erosion, kernel)
    return open


def main():
    image_path = 'lena.png'
    
    color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((5, 5), np.uint8)

    dilated_image = dilate(grayscale_image,kernel)
    eroded_image = erode(grayscale_image,kernel)
    
    closed_image = apply_closing(eroded_image, kernel)

    cv2.imshow('Eroded Image', closed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # display_image(color_image, title="Original Color Image")
    # display_image(grayscale_image, title="Grayscale Image")
    # display_image(closed_image, title="Closed Image")

if __name__ == '__main__':
    main()



