# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:19:43 2018

@author: willalex
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        s = set(numbers)
        if 2 * len(s) > len(numbers):
            return 0
        else:
             mode = []
             arr_appear = dict((a, numbers.count(a)) for a in numbers)
             for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数  
                 if v == max(arr_appear.values()):  
                     mode.append(k)  
             return mode[0]
L = [1,2,3,2,4,2,5,2,3]
c = Solution()
e = c.MoreThanHalfNum_Solution(L)
    
    