# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 10:12
# @Author  : Jiangzhesheng
# @File    : q747.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        TOP-K问题，K=2
        :param nums:
        :return:
        """
        if len(nums)==1:
            return 0
        if len(nums)>=2:
            if nums[0]>nums[1]:
                top1_idx,top2_idx=0,1
            else:
                top1_idx, top2_idx = 1, 0
        for i in range(2,len(nums)):
            if nums[i]>nums[top1_idx]:
                top2_idx=top1_idx
                top1_idx=i
            elif nums[i]>nums[top2_idx]:
                top2_idx=i

        if nums[top1_idx]>=2*nums[top2_idx]:
            return top1_idx
        else:
            return -1
a = [3,6,1,0]
b=[1,2,3,4]
c=[1,0]
s=Solution().dominantIndex(nums=a)
print(s)