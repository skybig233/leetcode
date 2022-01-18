# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 12:26
# @Author  : Jiangzhesheng
# @File    : q373.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans=[]
        i=0
        while i*(i+1)/2<k:
            # i=1 k=1
            # i=2 k=2,3
            # i=3 k=4,5,6
            i+=1
            tmp=[[nums1[j],nums2[i-1-j]] for j in range(i)]#副对角线元素列
            tmp.sort(key=lambda x:x[0]+x[1])
            ans+=tmp
        # ans中会多出一部分，要删掉
        # k=5时ans中6个值，del=1
        delete=int(i*(i+1)/2)-k
        return ans[:-delete] if delete!=0 else ans
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 6
s=Solution().kSmallestPairs(nums1,nums2,k)
print(s)