import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def classifyColor(rgb):
     colors = ["Dark", "Tan", "Average", "Light", "Pale"]
     dark = (141, 85, 36)
     tan = (198, 134, 66)
     avg = (224, 172, 105)
     light = (241, 194, 125)
     pale = (255, 219, 172)

     # Find vector distance to provided image and find minimum distance
     distances = []
     d_dark = math.sqrt(((dark[0]-rgb[0])*0.3)**2 + ((dark[1]-rgb[1])*0.59)**2 + ((dark[2]-rgb[2])*0.11)**2)
     distances.append(d_dark)
     d_tan = math.sqrt(((tan[0]-rgb[0])*0.3)**2 + ((tan[1]-rgb[1])*0.59)**2 + ((tan[2]-rgb[2])*0.11)**2)
     distances.append(d_tan)
     d_avg = math.sqrt(((avg[0]-rgb[0])*0.3)**2 + ((avg[1]-rgb[1])*0.59)**2 + ((avg[2]-rgb[2])*0.11)**2)
     distances.append(d_avg)
     d_light = math.sqrt(((light[0]-rgb[0])*0.3)**2 + ((light[1]-rgb[1])*0.59)**2 + ((light[2]-rgb[2])*0.11)**2)
     distances.append(d_light)
     d_pale = math.sqrt(((pale[0]-rgb[0])*0.3)**2 + ((pale[1]-rgb[1])*0.59)**2 + ((pale[2]-rgb[2])*0.11)**2)
     distances.append(d_pale)

     min_num = distances[0]
     min_ind = 0
     for i in range(len(distances)):
          if(distances[i] < min_num):
               min_num = distances[i]
               min_ind = i

     print("Skin Tone:", colors[min_ind])
     return min_ind

def getSkinColor(img, eye, nose):
     # Segment area above eyebrows
     eye_max_y = eye[0][1]
     eye_ind = 0
     for i in range(len(eye)):
          if(eye_max_y < eye[i][1]):
               eye_max_y = eye[i][1]
               eye_ind = i

     nose_min_x = nose[0][0]
     nose_ind = 0
     for i in range(len(nose)):
          if(nose_min_x > nose[i][0]):
               nose_min_x = nose[i][0]
               nose_ind = i

     cropped = img[eye[eye_ind][1] : nose[nose_ind][1], eye[eye_ind][0] : nose[nose_ind][0]]

     # cv2.imshow(winname="Face", mat=cropped)
     # cv2.waitKey(delay=0)
     # cv2.destroyAllWindows()

     # Find most occuring color
     temp = cropped.copy()
     unique, counts = np.unique(temp.reshape(-1, 3), axis=0, return_counts=True)
     temp[:,:,0], temp[:,:,1], temp[:,:,2] = unique[np.argmax(counts)]
     im_rgb = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)

     # Find closest color to most occuring color
     im_color = classifyColor(im_rgb[0][0])

     colors = [
          (141, 85, 36),
          (198, 134, 66),
          (224, 172, 105),
          (241, 194, 125),
          (255, 219, 172)
     ]

     # Save color to texture
     process = cropped.copy()
     unique, counts = np.unique(process.reshape(-1, 3), axis=0, return_counts=True)
     process[:,:,0], process[:,:,1], process[:,:,2] = colors[im_color]
     im_bgr = cv2.cvtColor(process, cv2.COLOR_RGB2BGR)
     # Convert to RGB
     cv2.imwrite("/Users/xocoo/Desktop/Projects/AvatarCreator/avatar/texture.png", im_bgr)

     return im_color

