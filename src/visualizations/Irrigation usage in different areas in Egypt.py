# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 00:17:38 2021

@author: Mariam
"""
#familiar imports 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc = {'figure.figsize':(28,6)})

#reading the dataset
dataset=pd.read_csv("Irrigation usage in different areas in Egypt.csv")
dataset.describe()
dataset = dataset.dropna(axis=0)
#saving lost values 

olddataset = pd.read_csv("Irrigation usage in different areas in Egypt.csv")
egypt_totalha = olddataset["total (ha)"][27]
total_surfacewater = olddataset["with surface water(ha)"][27]

#plotting the info given
dataset.info()
sns.barplot(y='with surface water(ha)',x='Governorate',data=dataset)
sns.barplot(y='total (ha)',x='Governorate',data=dataset)
#total (ha) against surface water and ground water respectively
sns.barplot(y='with surface water(ha)',x='total (ha)',data=dataset)
sns.barplot(y='with groundwater',x='total (ha)',data=dataset)

dataset.sort_values("Percent area", axis = 0, ascending = False,
                 inplace = True, na_position ='last')
dataset[['Governorate', "Percent area"]]
