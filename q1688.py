# -*- coding: utf-8 -*-
# @Time    : 2022/1/25 14:07
# @Author  : Jiangzhesheng
# @File    : q1688.py
# @Software: PyCharm
# @Description:
class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        dp[i]表示n=i时，需要匹配的次数，则有
        dp[1]=1
        dp[2]=1

        dp[i]=dp[i/2]+i/2 i为偶数
        dp[i]=dp[(i-1/2)+1]+(i-1)/2 i为奇数
        :param n:
        :return:
        """
        dp=[0]*(n+1)
        for i in range(1,n+1):
            if i%2==0:
                dp[i]=dp[i//2]+i//2
            else:
                dp[i]=dp[(i-1)//2+1]+(i-1)//2
        return dp[n]

s=Solution().numberOfMatches(n=2)
print(s)