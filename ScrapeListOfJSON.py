# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:53:53 2021

@author: hosam
"""

import requests
import pandas as pd
statesList=requests.get('https://chanakyya.com/Chanakya/states.json').json()
state=[]
for stateName in statesList:
    state.append(stateName['stateName'])
    
state.remove('Jammu&Kashmir') #Data Not AVailable
FinalWeakAndStrong=pd.DataFrame()
booth=[]
for stateName in state:

    a=requests.get('https://chanakyya.com/Chanakya/'+stateName+'/'+stateName+'.json?isNewDataFormat=true').json()
    b=pd.DataFrame.from_dict(a['STRONG_WEAK_BOOTH_DATA'].items())
    b['State']=stateName
    FinalWeakAndStrong=FinalWeakAndStrong.append(b)
    
    
    c=pd.DataFrame.from_dict(a['ASSEMBLY_NAME_DATA'].items())
    for x in c[1]:
        assembly=requests.get('https://chanakyya.com/Chanakya/'+stateName+'/AssemblyData/'+x).json()
        print(assembly['ELECTION_DATA']['boothFileName'])
        booth.append([stateName, x,assembly['ELECTION_DATA']['boothFileName']])
        
    

FinalBooth=pd.DataFrame(booth,columns=['State', 'Assembly','Booth File'])
FinalBooth.to_csv('C:/Users/hosam/Documents/Project/Election Data/Programs/Booth Files Data.csv')
FinalWeakAndStrong.to_csv('C:/Users/hosam/Documents/Project/Election Data/Programs/StrongAndWeakData.csv')
    