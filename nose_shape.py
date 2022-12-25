import cv2
import face_shape

def getNoseShape(img, nose, lips):
     bottom_to_lips = face_shape.findDistance(nose[-2], lips[3])
     top_to_lips = face_shape.findDistance(nose[0], lips[3])
     if(bottom_to_lips / top_to_lips < 0.2):
          print("Nose: Lowered")
          return 1
     elif(bottom_to_lips / top_to_lips > 0.22):
          print("Nose: Raised")
          return 2
     else:
          print("Nose: Straight")
          return 3
     pass
