import os
import numpy as np
import cv2


def color2gray(path, name):
    img = cv2.imread(os.path.join(path, name))
    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]  # get value of RGB
    w, h = img.shape[:2]  # the height and width of image

    # create a new img
    # initial the color of the new image(it's black)
    new_img = np.zeros((w, h, 1))
    for i in range(w):
        for j in range(h):
            # translate with equation
            new_img[i][j][0] = np.array(
                [r[i][j] * 0.299 + g[i][j] * 0.587 + b[i][j] * 0.114], dtype=float)

    new_name = name.split('.')[0] + '.png'
    cv2.imwrite(os.path.join('.\img\gray_img', f'terry_{new_name}'),
                new_img)  # store the new photo


def main():
    path = '.\img'
    extension = ['.jpeg', '.tiff', '.jpg']
    for f in os.listdir(path):
        for e in extension:
            if f.endswith(e):
                color2gray(path, f)



if __name__ == '__main__':
    if not os.path.exists('.\img\gray_img'):
        os.mkdir('.\img\gray_img')
    main()
