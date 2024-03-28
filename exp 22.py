#. Perform Sharpening of Image using Laplacian
#mask k with positive center coefficient
import cv2
import numpy as np
img=cv2.imread(r"C:\desktop\cv lab\dog input.jpeg")
img=cv2.resize(img,(255,255))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpened=cv2.filter2D(gray,-1,kernel)
sharpened=cv2.cvtColor(sharpened,cv2.COLOR_GRAY2BGR)
cv2.imshow("original",img)
cv2.imshow("sharpened",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
