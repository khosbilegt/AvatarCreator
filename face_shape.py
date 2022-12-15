import cv2
import math

def findDistance(p1, p2):
     d = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
     return d

def getFaceShape(img, jaw):
     # # Square on Face
     # p1 = jaw[0]
     # p2 = (jaw[len(jaw) - 1][0], jaw[len(jaw) - 7][1])
     # cv2.rectangle(img, p1, p2, (255, 255, 255), 2)

     # # Round on Face
     # round_x = (jaw[2][0] + jaw[len(jaw) - 2][0]) / 2
     # round_y = (jaw[2][1] + jaw[len(jaw) - 2][1]) / 2
     # radius = int((jaw[len(jaw) - 1][0] - jaw[0][0]) / 2)
     # center = (int(round_x), int(round_y))
     # cv2.circle(img, center, radius, (0, 0, 0), 2)

     # Check Round
     above_cheek = findDistance(jaw[1], jaw[-2])
     below_cheek = findDistance(jaw[3], jaw[-4])

     if(above_cheek < below_cheek * 1.05):
          print("Face Shape: Round")
          return 1

     if(abs(above_cheek - below_cheek) < below_cheek * 0.1):
          print("Face Shape: Square")
          return 2

     print("Face Shape: Oval")
     return 3

     pass

# Face 
# [, [40, 254], [51, 344],
#  [66, 428], [95, 503], [141, 565], 
#  [195, 616], [258, 650], [333, 657], 
#  [405, 645], [465, 607], [518, 554], 
#  [560, 491], [589, 417], [605, 336], 
#  [617, 248], 

# Round
# [[7, 74], [6, 99], [6, 125], 
# [10, 152], [21, 176], [42, 195], 
# [68, 209], [95, 218], [121, 219], 
# [145, 213], [166, 199], [186, 183], 
# [202, 163], [209, 138], [211, 112], 
# [210, 85], [207, 59]]

