# -*- coding: utf-8 -*-
# @Time : 2020/11/17 15:23
# @Author : Jiangzhesheng
# @File : 1030.py
# @Software: PyCharm
from typing import List
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans=[[i,j] for i in range(R) for j in range(C)]
        ans.sort(key=lambda x:abs(x[0]-r0)+abs(x[1]-c0))
        return ans

R=1
C=2
r0=0
c0=0
s=Solution().allCellsDistOrder(R,C,r0,c0)
print(s)