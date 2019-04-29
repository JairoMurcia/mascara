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
    for a in range(c-2):
        aux=(data[0:3,a:a+3]*m).sum()
        data[0,a]=aux;     
    aux=(data[0:3,c-3:c]*m).sum()
    data[0,c-1]=aux;       
    
    aux=(data[f-3:f,c-3:c]*m).sum()
    data[f-1,c-1]=aux;
    
    for a in range(1,f-2):
         aux=(data[a:a+3,0:3]*m).sum()
         data[a,0]=aux; 
         aux=aux=(data[f-3:f,c-3:c]*m).sum()
         data[a,c-1]=aux;
    
    aux=aux=(data[f-3:f,0:3]*m).sum()
    data[f-2,0]=aux;
    
    
    aux=aux=(data[f-3:f,c-3:c]).sum()
    data[f-2,c-1]=aux;
    return data
    

#pix = np.arange(160*160).reshape(160,160)

#pix[:]=pic.getdata()






im = Image.open("foto.jpg")
col =  im.size[0]
row=im.size[1]
data = np.zeros((row,col))



pixels =np.array(im)
print(pixels.shape)

for i in range(row):
    
    for j in range(col):
        r,g,b =  pixels[i,j]
      
        data[i,j] = r


mascara=np.full((3,3),1/9) 




           


im1=Image.fromarray(aplicar_mascara(data,mascara,row,col))    
im1.show()
