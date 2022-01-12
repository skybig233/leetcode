# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 12:56
# @Author  : Jiangzhesheng
# @File    : q300.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        贪心解法，没有二分
        :param nums:
        :return:
        """
        a=[nums[0]]# a数组记录ijk的值
        for i in range(1,len(nums)):
            #如果比当前记录的最后一个指针要大，则最长长度延长
            if nums[i]>a[-1]:
                a.append(nums[i])
            else:
                for j in range(len(a)):
                    if nums[i]<a[j]:
                        if j==0 or a[j-1]<nums[i]:
                            a[j]=nums[i]
                            break
        return len(a)

a=[1,5,10,2,3,4]
b=[2,1,5,0,4,6]
c=[1,2,1,2,1,2,1,2,1,2,1,2]
d=[20,100,10,12,5,13]
s=Solution().lengthOfLIS(nums=d)
print(s)
