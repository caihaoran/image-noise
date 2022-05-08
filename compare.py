# import skimage.measure
from skimage.metrics import structural_similarity as ssim
# from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()


# load the images -- the original, the original + contrast,
# and the original + photoshop

original = cv2.imread("qq.jpg")

salt_img_mean = cv2.imread('salt_img_mean.jpg')
salt_img_median = cv2.imread('salt_img_median.jpg')
salt_img_Guassian = cv2.imread('salt_img_Guassian.jpg')
gauss_img_mean = cv2.imread('gauss_img_mean.jpg')
gauss_img_median = cv2.imread('gauss_img_median.jpg')
gauss_img_Guassian = cv2.imread('gauss_img_Guassian.jpg')

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

salt_img_mean = cv2.cvtColor(salt_img_mean, cv2.COLOR_BGR2GRAY)
salt_img_median = cv2.cvtColor(salt_img_median, cv2.COLOR_BGR2GRAY)
salt_img_Guassian = cv2.cvtColor(salt_img_Guassian, cv2.COLOR_BGR2GRAY)
gauss_img_mean = cv2.cvtColor(gauss_img_mean, cv2.COLOR_BGR2GRAY)
gauss_img_median = cv2.cvtColor(gauss_img_median, cv2.COLOR_BGR2GRAY)
gauss_img_Guassian = cv2.cvtColor(gauss_img_Guassian, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("salt_img_mean", salt_img_mean), ("salt_img_median", salt_img_median), (
"salt_img_Guassian", salt_img_Guassian), \
         ("gauss_img_mean", gauss_img_mean), ("gauss_img_median", gauss_img_median), (
         "gauss_img_Guassian", gauss_img_Guassian)
# loop over the images
for (i, (name, image)) in enumerate(images):
    # show the image
    ax = fig.add_subplot(1, 7, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("off")
# show the figure
plt.show()
# compare the images
compare_images(original, salt_img_mean, "Original vs. salt_img_mean")
compare_images(original, salt_img_median, "Original vs. salt_img_median")
compare_images(original, salt_img_Guassian, "Original vs. salt_img_Guassian")
compare_images(original, gauss_img_mean, "Original vs. gauss_img_mean")
compare_images(original, gauss_img_median, "Original vs. gauss_img_median")
compare_images(original, gauss_img_Guassian, "Original vs. gauss_img_Guassian")
