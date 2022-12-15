import cv2
import sys
import dlib
import eyebrows as eb
import glasses
import skin
import avatar
import face_shape

def cropFace(path):
     detector = dlib.get_frontal_face_detector()
     img = cv2.imread(path)
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     # Use detector to find landmarks
     faces = detector(gray)

     for face in faces:
          x1 = face.left()
          y1 = face.top()
          x2 = face.right() 
          y2 = face.bottom() 
     
     cropped = img[y1 : y2, x1 : x2]
     return cropped

# FACIAL_LANDMARKS_IDXS = OrderedDict([
# 	("mouth", (48, 68)),
# 	("right_eyebrow", (17, 22)),
# 	("left_eyebrow", (22, 27)),
# 	("right_eye", (36, 42)),
# 	("left_eye", (42, 48)),
# 	("nose", (27, 35)),
# 	("jaw", (0, 17))
# ])


def findFeatures(img, path):
     detector = dlib.get_frontal_face_detector()
     predictor = dlib.shape_predictor("predictor.dat")
     gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
     faces = detector(gray)
     # Iterate through detected faces
     for face in faces:
          x1 = face.left()
          y1 = face.top()
          x2 = face.right() 
          y2 = face.bottom()

          # Create landmark object
          landmarks = predictor(image=gray, box=face)
          
          # Facial Shape
          jaw = []
          for n in range(0, 17):
               temp = []
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               temp.append(x)
               temp.append(y)
               jaw.append(temp)
          face_type = face_shape.getFaceShape(img, jaw)

          # Eyebrows
          right_eyebrow = []
          for n in range(17, 22):
               temp = []
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               temp.append(x)
               temp.append(y)
               right_eyebrow.append(temp)
          eyebrowType = eb.classifyEyebrows(right_eyebrow)
          
          # Glasses
          nose = []
          for n in range(27, 35):
               temp = []
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               temp.append(x)
               temp.append(y)
               nose.append(temp)
          hasGlasses = glasses.findGlasses(img, nose)
          
          #Skin Color
          eye = []
          for n in range(36, 42):
               temp = []
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               temp.append(x)
               temp.append(y)
               eye.append(temp)
          skin_tone = skin.getSkinColor(img, eye, nose)

          old_x = 0
          old_y = 0
          for n in range(0, 67):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               # Draw a circle
               cv2.line(img, (old_x, old_y), (x, y), (0, 255, 0), thickness = 1)
               cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
               old_x = x
               old_y = y

          avatar.createAvatar("male", hasGlasses, eyebrowType, skin_tone)
     pass

# Input
imagePath = "/Users/xocoo/Desktop/Projects/AvatarCreator/images/dark.jpg"
predictorPath = "/Users/xocoo/Desktop/Projects/AvatarCreator/predictor.dat"
cropped = cropFace(imagePath)
findFeatures(cropped, predictorPath)

# cv2.imshow(winname="Face", mat=cropped)
# cv2.waitKey(delay=0)
# cv2.destroyAllWindows()