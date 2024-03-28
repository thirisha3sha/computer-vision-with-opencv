#33. Morphological operations based on OpenCV using Morphological Gradient technique
import cv2
import numpy as np
img = cv2.imread(r"C:\desktop\cv lab\dog input.jpeg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Original", img)
cv2.imshow("Gradient", grad)
cv2.waitKey
