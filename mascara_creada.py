# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:47:00 2019

@author: Estudiantes
"""

from PIL import Image
import numpy as np


def aplicar_mascara(data,m,f,c):
    
    for a in range(c-2):
        for b in range(f-2):
    
          
           aux=(data[b:b+3,a:a+3]*m).sum()
           data[b+1,a+1]=aux
                      
           
           
    return data
    







im = Image.open("flor.jpg")
col =  im.size[0]
row=im.size[1]
data = np.zeros((row,col))



pixels =np.array(im)


for i in range(row):
    
    for j in range(col):
        r =  pixels[i,j,0]
      
        data[i,j] = r


mascara=np.array([[0,0,0],[1/3,4/3,1/3],[0,0,0]])



           


im1=Image.fromarray(aplicar_mascara(data,mascara,row,col))    
im1.show()