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