# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:45:19 2024

@author: User
"""
import numpy as np
import pandas as pd
"""countries = {'th':'Thailand','jp':'Japan','kr':'Korea'}
# info = {'name': 'john','age':30,'hight':180.2,'single':True}
# ranges = {'odd':[1,3,5,7,9],'even':[2,4,6,8,10]}

# for key in countries.keys():
    # print(key)
    
# for value in countries.values():
    # print(value)
    
Dict_Key = countries.keys()
print(*Dict_Key)

Dict_value = countries.values()
for v in Dict_value:
    print(v)
    
Dict_item = countries.items()
for (k,v) in Dict_item:
      print(f'{k} - {v}')    
     """
"""a = np.array([[2,4,6],[3,5,7]])
b = np.array(range(1,11))
c = np.array((1,2,3,4))
d = np.array([3*x for x in range(1,6)])
 
# index slicing    """

# a = np.arange(1, 11)
# b = a.reshape(1, 10)
# c = a.reshape(2, 5)
# d = a.reshape(3,5)
# !git pull origin main
# !git add .
# !git commit -m "Resolved merge conflicts"
# !git push origin main
# !git push origin main --force


# data = [[10,50,80,567],[5,25,75,432],[]]
# data = {'age':[30,40,50,60],
        # 'H':[175,150,154,180],
        # 'w':[80,12,45,78]}
# df = pd.DataFrame(data,index=['p1','p2','p3','p4'])
# d = df.age[2]
# a = df.iloc[1:2, 2:3]


data = {'One':np.random.randint(100,1000,10),
        'Two':np.random.randint(1,10,10),
        'Three':np.random.randint(10),
        'Four':np.random.randint(1,100,10),
        'One':np.random.randint(-10,10,10),
        }
df = pd.DataFrame(data)
a = df.sum()
b = df.sum()['One']
c = df.max()['One']