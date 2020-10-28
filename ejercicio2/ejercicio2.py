# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 01:18:26 2020

@author: SANDRA
"""

import numpy as np
import pandas as pd
matriz =pd.read_csv('datas.csv')
matriz1 =pd.read_csv('data.csv')

media=matriz1['Cholera case fatality rate']
media2=matriz1['Number of reported deaths from cholera']
print(matriz1)


nuevo= matriz['Cholera case fatality rate']
nuevo2=matriz['Number of reported cases of cholera']
nuevo3=matriz['Number of reported deaths from cholera']

#------------------imputer

from sklearn.impute import SimpleImputer
imputacion=SimpleImputer(missing_values=np.nan,strategy="mean")
media=media.values.reshape(-1,1)

print("Cholera case fatality rate")
print(imputacion.fit_transform(media))
media2=media2.values.reshape(-1,1)
print("Number of reported deaths from cholera")
print(imputacion.fit_transform(media2))





#Discretizacion utilizando KBinsDiscretizer
print(matriz)
from sklearn.preprocessing import KBinsDiscretizer
dis=KBinsDiscretizer(n_bins=6,encode='ordinal',strategy='uniform')
nuevo=nuevo.values.reshape(-1,1)

nue=dis.fit(nuevo)

print('------')
print('Discretizacion')

trans=dis.transform(nuevo)


print("Cholera case fatality rate")
print(trans)

dis1=KBinsDiscretizer(n_bins=6,encode='ordinal',strategy='uniform')
nuevo2=nuevo2.values.reshape(-1,1)
nue2=dis1.fit(nuevo2)
print('------')
trans1=dis1.transform(nuevo2)

print("Number of reported cases of cholera")
print(trans1)

dis2=KBinsDiscretizer(n_bins=6,encode='ordinal',strategy='uniform')
nuevo3=nuevo3.values.reshape(-1,1)
nue3=dis2.fit(nuevo3)
print('------')
trans2=dis2.transform(nuevo3)
print("Number of reported deaths from cholera")
print(trans2)

#---------------




