# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:45:19 2024

@author: User
"""
import numpy as np
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

a = np.arange(1, 11)
b = a.reshape(1, 10)
c = a.reshape(2, 5)
d = a.reshape(3,5)
        