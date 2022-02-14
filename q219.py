# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 10:13
# @Author  : Jiangzhesheng
# @File    : q219.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d and abs(d[nums[i]]-i)<=k:
                return True
            else:
                d[nums[i]] = i
        return False
nums=[1,2,3,1,2,3]
s=Solution().containsNearbyDuplicate(nums,3)
print(s)