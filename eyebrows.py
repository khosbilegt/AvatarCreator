import numpy as np
# Use sum of angles between points to classify eyebrows

def findAngle(p1, p2):
     ang1 = np.arctan2(*p1[::-1])
     ang2 = np.arctan2(*p2[::-1])
     return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def classifyEyebrows(points):
     # Check if Downward
     if(points[4][1] < points[3][1]):
          print("Eyebrows: Downward")
          return
     # Find Sum of Angles to detect others
     sum = 0
     for i in range(len(points) - 1):
          sum = sum + findAngle(points[i], points[i + 1])
          pass
     if(sum < 300):
          print("Eyebrows: Straight")
          return 1
     elif(sum > 300 and sum < 500):
          print("Eyebrows: Curved")
          return 2
     elif(sum > 500 and sum < 1000):
          print("Eyebrows: Hard-Angled")
          return 3
     elif(sum > 1000):
          print("Eyebrows: High-Arched")
          return 4