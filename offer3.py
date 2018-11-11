# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:28:40 2018

@author: Administrator
"""

# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    
    def printListFromTailToHead(self, listNode):
         # write code here
        l = []
        head = listNode
        while head:
            l.insert(0, head.val) #0表示每次插在列表的第一位，这样最后一个插入的在list第一个位置，第一个插入的在list最后一个未知
            head = head.next
        return l
