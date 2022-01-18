# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 11:14
# @Author  : Jiangzhesheng
# @File    : q539.py
# @Software: PyCharm
# @Description:
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 24*60=1440
        # ans=min(((a-b) mod 1440),((b-a) mod 1440))
        def int_time(time:str)->int:
            hour=int(time.split(':')[0])
            minute=int(time.split(':')[1])
            return hour*60+minute
        time=sorted([int_time(i) for i in timePoints])

        min_diff=1440
        for i in range(1,len(time)):
            if time[i]-time[i-1]<min_diff:
                min_diff=time[i]-time[i-1]

        min_diff=min((time[0]-time[-1])%1440,min_diff)

        return min_diff

timePoints = ["00:00","23:59","00:00"]
s=Solution().findMinDifference(timePoints)
print(s)