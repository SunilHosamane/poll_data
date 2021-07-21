# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 07:53:03 2021

@author: hosam
"""

import requests
import pandas as pd
import json

a=pd.read_csv('C:/Users/hosam/Documents/Project/Election Data/Programs/StrongAndWeakData.csv')
for index, row in a.iterrows():
    b=requests.get('https://chanakyya.com/Chanakya/'+row[3]+'/AssemblyLevelAnalytics/'+row[2]+'?isNewDataFormat=true').json()
    with open ('C:/Users/hosam/Documents/Project/Election Data/Output/StrongAndWeak/'+row[3]+row[1]+'.json','w') as f:
        json.dump(b,f)
    