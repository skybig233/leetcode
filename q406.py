# -*- coding: utf-8 -*-
# @Time : 2020/11/16 13:29
# @Author : Jiangzhesheng
# @File : q406.py
# @Software: PyCharm
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i in people:
            res.insert(i[1], i)
        return res
people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s=Solution().reconstructQueue(people)
print(s)