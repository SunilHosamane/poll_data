# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:31:16 2021

@author: hosam
"""

import requests
import json
import pandas as pd
import time
import os
a=pd.read_csv('C:/Users/hosam/Documents/Project/Election Data/Programs/Booth.csv')
a=a.dropna()
for x, row in a.iterrows():
    if row[3]!=0:
        print(row[3])
        c=requests.get('https://chanakyya.com/Chanakya/'+row['State']+'/BoothData/'+str(row[3])).json()
        with open ('C:/Users/hosam/Documents/Project/Election Data/Output/Booth Level/'+row['State']+'/'+row[2],'w') as f:
            json.dump(c,f)