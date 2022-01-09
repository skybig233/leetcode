# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 14:01
# @Author  : Jiangzhesheng
# @File    : q1629.py
# @Software: PyCharm

from typing import List
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time=releaseTimes[0]
        ans=keysPressed[0]
        for i in range(1,len(releaseTimes)):
            current_time=releaseTimes[i]-releaseTimes[i-1]
            if current_time>max_time:
                max_time=current_time
                ans = keysPressed[i]
            elif current_time==max_time:
                ans=keysPressed[i] if keysPressed[i]>ans else ans
        return ans

releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"

s=Solution().slowestKey(releaseTimes,keysPressed)
print(s)