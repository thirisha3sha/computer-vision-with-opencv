import cv2
import numpy as np
img = cv2.imread(r"C:\desktop\cv lab\dog input.jpeg")
blurred_img = cv2.GaussianBlur(img, (3, 3), 0)
laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)
laplacian = cv2.filter2D(blurred_img, -1, laplacian_kernel)
k = 1.5  
sharpened_img = img + k * laplacian
sharpened_img = np.clip(sharpened_img, 0, 255)
sharpened_img = np.uint8(sharpened_img)
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
