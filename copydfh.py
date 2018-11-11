# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:47:51 2018

@author: willalex
"""

def get_mode(arr):  
    mode = [];  
    arr_appear = dict((a, arr.count(a)) for a in arr);  # 统计各个元素出现的次数  
    if max(arr_appear.values()) == 1:  # 如果最大的出现为1  
        return;  # 则没有众数  
    else:  
        for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数  
            if v == max(arr_appear.values()):  
                mode.append(k);  
    return mode;  
  
arr = [1, 2, 3, 2, 3, 1, 4];  
print(get_mode(arr))
    
    