# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 12:28
# @Author  : Jiangzhesheng
# @File    : q334.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        改题解法是300题leetcode贪心+二分的提示
        将i,j,k三个元组改为k个元组就能想到贪心解法
        即尽量使前k-1个小
        进一步求出LIS长度
        :param nums:
        :return:
        """
        a=[nums[0]]# a数组记录ijk的值
        for i in range(1,len(nums)):
            #提前跳出，不用遍历所有nums
            if len(a)>=3:
                return True
            #如果比当前记录的最后一个指针要大，则最长长度延长
            if nums[i]>a[-1]:
                a.append(nums[i])
            else:
                for j in range(len(a)):
                    if nums[i]<a[j]:
                        if j==0 or a[j-1]<nums[i]:
                            a[j]=nums[i]
                            break
        return len(a)>=3
a=[1,5,10,2,3,4]
b=[2,1,5,0,4,6]
c=[1,2,1,2,1,2,1,2,1,2,1,2]
d=[20,100,10,12,5,13]
s=Solution().increasingTriplet(nums=c)
print(s)
