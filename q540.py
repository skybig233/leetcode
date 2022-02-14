# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 14:18
# @Author  : Jiangzhesheng
# @File    : q540.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            n=right-left+1
            mid=(left+right)//2
            if n%4==1:
                #与左边相同，则在左
                if nums[mid]==nums[mid-1]:
                    right=mid-2
                elif nums[mid]==nums[mid+1]:
                    left=mid+2
                else:
                    return nums[mid]
            elif n%4==3:
                if nums[mid]==nums[mid-1]:
                    left=mid+1
                elif nums[mid]==nums[mid+1]:
                    right=mid-1
                else:
                    return nums[mid]
        return nums[left]

nums = [1,1,2,2,3,3,4,4,11,8,8]
# nums=[1,2,2,4,4]
# nums=[1,2,2]
s=Solution().singleNonDuplicate(nums)
print(s)