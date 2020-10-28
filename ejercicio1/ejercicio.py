# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:13:50 2020

@author: SANDRA
"""
#import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode
datos=[]
edad=[]
cont=0
with open('datos.csv', encoding='utf-8-sig') as f:
   # reader= csv.reader(f, delimiter=";")
    linea=f.read().splitlines()
    linea.pop(0)
   # for row in reader:
    #    print("ci: {0},nombre: {1},sexo: {2},departamento: {3},nota: {4},edad: {5}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    for l in linea:
        linea = l.split(';')
        cont=cont+1
        datos.append(float(linea[4]))
        edad.append(int(linea[5]))
print(datos)

print(cont)

#Edad media de los estudiantes
#media=round(sum(datos)/cont)
media=(sum(datos)/cont)
print("la media es: ")
print(media)

#desviacion estandar
suma=0
for v in datos:
    nue=v
    nue=nue-media
    nue=nue**2
    suma = suma + nue
    
sumas=(suma/(cont-1))
print(sumas)
print("la desviacion estandar:")
desviacion=(sumas**(1/2))
print(desviacion)

#ejercicio b
print("------------EJERCICIO B-------------")
print("NUMPY")
mediaN=np.mean(datos)
print("la media es: ")
print(mediaN)
desviacionN=np.std(datos)
print("la desviacion estandar:")
print(desviacionN)
print("moda")
print(mode(datos))
#--------pandas
print("PANDAS")
df=pd.DataFrame(datos)
mediaP=df.mean()
print("la media es: ")
print(mediaP)
desviacionP=df.std()
print("la desviacion estandar:")
print(desviacionP)
#--------------EJERCICIO C
print("--------------EJERCICIO C--------------")
#mientras una persona va creciendo disminuye el nivel de aprendizaje

x=edad
y=datos
plt.plot(x,y,'ro')
plt.show()
        
