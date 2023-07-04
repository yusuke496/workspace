from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

path=input("Input file name: ")
path = "./" + path
a=os.path.exists(path)
if a==True :
        img = Image.open(path)
        #img.show()
        img_list = np.asarray(img)
        #img_list = np.array(img)
        #print(img_lis)
        plt.imshow(img_list)
        plt.show()
else :
    print("error")
