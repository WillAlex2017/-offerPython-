# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:40:58 2018

@author: WillAlex
"""
import numpy as np
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array) - 1
        col = len(array[0]) - 1
        i = row
        j = 0
        while(j <= col and i >=0):
            if target > array[i][j]:
                j += 1
            elif target < array[i][j]:
                i -= 1
            else:
                return True
        return False

if __name__ == "__main__":
    so = Solution()
    t = 3
    arr = np.array([[1,2],[3,4]])
    b = so.Find(t, arr)
    print(b)
    
#从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。
#于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。 


                
        
