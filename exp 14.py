import cv2
import numpy as np
im_src=cv2.imread(r"C:\desktop\cv lab\dog input.jpeg")
pts_src=np.array([[141,131],[480,159],[493,630],[64,60]])
im_dst=cv2.imread(r"C:\desktop\cv lab\dog input.jpeg")
pts_dst=np.array([[318,256],[534,372],[316,670],[73,473]])
h,status=cv2.findHomography(pts_src,pts_dst)
im_out=cv2.warpPerspective(im_src,h,(im_dst.shape[1],im_dst.shape[0]))
cv2.imshow("source image",im_src)
cv2.imshow("destination image",im_dst)
cv2.imshow("warped source image",im_out)
