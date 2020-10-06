import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def equalization(array_img, M, N):
    # find the minimum of the CDF
    sort_img = sorted(array_img)
    cdMin = sort_img[0]

    den = M * N - cdMin  # denominator

    cd = np.zeros(256)
    # calc frequency
    for i in range(len(array_img)):
        cd[array_img[i]] += 1

    # calc cdf
    for i in range(1, 256):
        cd[i] += cd[i-1]

    # equalize by equaltion
    for i in range(len(array_img)):
        array_img[i] = round((cd[array_img[i]] - cdMin)/den*255)

    return array_img


def histogram(img, path):
    plt.hist(img, bins=250)  # draw histogram
    plt.savefig(path)    # save histogram
    plt.clf()


def main():
    src_path = '.\img'
    target_path = '.\img\hist_equal_img'
    extension = ['.tiff', '.jpg', 'jpeg']
    for f in os.listdir(src_path):
        for e in extension:
            if f.endswith(e):
                gray_img = cv.imread(os.path.join(
                    src_path, f), cv.IMREAD_GRAYSCALE)
                gray_img = np.asarray(gray_img)
                M, N = gray_img.shape
                hist_name = f.split('.')[0] + '.png'

                flat_img = gray_img.flatten()  # convert to 1-D
                # draw the origin histogram
                histogram(flat_img, os.path.join(
                    target_path, f'terry_gray_{hist_name}'))

                # do equalization function
                eq_img = equalization(flat_img, M, N)
                # draw the equalization histogram
                histogram(eq_img, os.path.join(
                    target_path, f'terry_hist_{hist_name}'))

                # save the equalization image
                eq_img = np.reshape(eq_img, (M, N))
                cv.imwrite(os.path.join(
                    target_path, f'terry_equal_{hist_name}'), eq_img)


if __name__ == '__main__':
    if not os.path.exists('.\img\hist_equal_img'):
        os.mkdir('.\img\hist_equal_img')
    main()
