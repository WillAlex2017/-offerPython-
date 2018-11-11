# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:40:42 2018

@author: willalex
"""
import itertools
class Solution:
    def Permutation(self,ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))
s = Solution()
t = s
print(s == t)
c=s.Permutation('abc')
print(c)