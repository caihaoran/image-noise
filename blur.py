import cv2

# 读取图像
img = cv2.imread('./salt.jpg')
print(img.shape)

# 对图像进行均值滤波
img_mean = cv2.blur(img, (5, 5))

# 对图像进行中值滤波
img_median = cv2.medianBlur(img, 5)

# 对图像进行高斯滤波
img_Guassian = cv2.GaussianBlur(img, (5, 5), 0)

# 图像显示
cv2.imshow("img", img)

cv2.imwrite('salt_img_mean.jpg', img_mean)
cv2.imwrite('salt_img_median.jpg', img_median)
cv2.imwrite('salt_img_Guassian.jpg', img_Guassian)

cv2.putText(img_mean, "img_mean", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
cv2.putText(img_median, "img_median", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
cv2.putText(img_Guassian, "img_Guassian", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)

cv2.imshow("img_mean", img_mean)
cv2.imshow("img_median", img_median)
cv2.imshow("img_Guassian", img_Guassian)

img = cv2.imread('./gauss.jpg')
print(img.shape)

# 对图像进行均值滤波
img_mean = cv2.blur(img, (5, 5))

# 对图像进行中值滤波
img_median = cv2.medianBlur(img, 5)

# 对图像进行高斯滤波
img_Guassian = cv2.GaussianBlur(img, (5, 5), 0)

# 图像显示
cv2.imshow("img", img)
cv2.imwrite('gauss_img_mean.jpg', img_mean)
cv2.imwrite('gauss_img_median.jpg', img_median)
cv2.imwrite('gauss_img_Guassian.jpg', img_Guassian)

cv2.putText(img_mean, "img_mean", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
cv2.putText(img_median, "img_median", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
cv2.putText(img_Guassian, "img_Guassian", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)

cv2.imshow("img_mean", img_mean)
cv2.imshow("img_median", img_median)
cv2.imshow("img_Guassian", img_Guassian)


cv2.waitKey(0)
cv2.destroyAllWindows()
