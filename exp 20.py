#. Perform Sharpening of Image using Laplacian
#mask with negative center coefficient.
import cv2
import numpy as np
img=cv2.imread(r"C:\desktop\cv lab\dog input.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel=np.array([[0,1,0],[1,-8,1],[0,1,0]])
sharpened=cv2.filter2D(gray,-1,kernel)
cv2.imshow("original",gray)
cv2.imshow("sharpened",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
