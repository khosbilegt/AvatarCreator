# Detect glasses frame from nose area after Gaussian Blur and Thresholding.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def findGlasses(img, nose):
     max_x = nose[0][0]
     min_x = nose[0][0]
     max_y = nose[0][1]
     min_y = nose[0][1]
     for i in range(len(nose)):
          if(nose[i][0] > max_x):
               max_x = nose[i][0]
          if(nose[i][0] < min_x):
               min_x = nose[i][0]
          if(nose[i][1] > max_y):
               max_y = nose[i][1]
          if(nose[i][1] < min_y):
               min_y = nose[i][1]
     pass

     cropped = img[min_y : max_y, min_x : max_x]
     blur = cv2.GaussianBlur(np.array(cropped),(3,3), sigmaX=0, sigmaY=0)
     edges = cv2.Canny(image =blur, threshold1=100, threshold2=200)
     edges_center = edges.T[(int(len(edges.T)/2))]
     
     # cv2.imshow(winname="Face", mat=edges)
     # cv2.waitKey(delay=0)
     # cv2.destroyAllWindows()
     
     # If threshold detects glasses
     if 255 in edges_center:
          print("Glasses: Present")
          return True
     else:
          print("Glasses: None")
          return False
     pass