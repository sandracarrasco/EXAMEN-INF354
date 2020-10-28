# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 04:14:20 2020

@author: SANDRA
"""

import numpy as np
import pandas as pd

data =pd.read_csv('data.csv')
from sklearn.tree import DesicionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import graphviz
 
dat=data.dropna()
data.dtypes
data.describe()
prediccion= data(['Number of reported cases of cholera','Number of reported deaths from cholera','Cholera case fatality rate'])