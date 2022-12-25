import re
import vedo

def createAvatar(gender, glasses, eyebrows, skin_tone):
     # Naming Convention
     # {Gender}_{Glasses}_{Eyebrows}
     file_name = ""
     if(gender == "male"):
          file_name = file_name + "M_"
     else:
          file_name = file_name + "F_"
     
     if(glasses == False):
          file_name = file_name + "G0_"
     else:
          file_name = file_name + "G1_"
     
     if(eyebrows == 1):
          file_name = file_name + "E1"
     elif(eyebrows == 2):
          file_name = file_name + "E2"
     elif(eyebrows == 3):
          file_name = file_name + "E3"
     elif(eyebrows == 4):
          file_name = file_name + "E4"
     pass

     path = "/Users/xocoo/Desktop/Projects/AvatarCreator/avatar/"
     path = path + file_name + ".obj"
     mesh = vedo.Mesh(path,)
     mesh.texture("/Users/xocoo/Desktop/Projects/AvatarCreator/avatar/texture.png", scale=0.1)
     #mesh.show()

     print(file_name)