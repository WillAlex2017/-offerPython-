# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:43:17 2018

@author: willalex
"""

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        else:
            return sorted(set(tinput))[:k]