# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:57:27 2018

@author: Administrator
"""
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20') #直接调用str的replace方法
    def replaceSpace2(self, s):
        # write code here
        s = list(s) #'str' object does not support item assignment
        for i in range(0,len(s)):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)
#入口程序用来测试    
if __name__ == "__main__":
        so = Solution()
        s1 = "We are Happy"
        s2 = so.replaceSpace(s1)
    