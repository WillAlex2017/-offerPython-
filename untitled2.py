# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:39:15 2018

@author: willalex
"""

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        cumsum = []
        array = list(array)
        for i in array:
            cumsum[i] = sum(array[:i])
        maxvalue = max(cumsum)
        return maxvalue

c = Solution()
gdg=c.FindGreatestSumOfSubArray(L)