# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 12:00
# @Author  : Jiangzhesheng
# @File    : q1220.py
# @Software: PyCharm
# @Description:

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        VOWEL=5
        A,E,I,O,U=0,1,2,3,4
        dp=[[0 for j in range(VOWEL)] for i in range(n)]
        dp[0]=[1,1,1,1,1]
        for i in range(1,n):
            for j in range(VOWEL):
                #新一轮结尾为a的，前面一轮应该为e、i、u
                dp[i][A]=dp[i-1][E]+dp[i-1][I]+dp[i-1][U]
                #新一轮结尾为e的，前一轮为a、i
                dp[i][E]=dp[i-1][A]+dp[i-1][I]
                # 新一轮结尾为i的，前一轮为e、o
                dp[i][I] = dp[i - 1][E] + dp[i - 1][O]
                # 新一轮结尾为o的，前一轮为i
                dp[i][O] =  dp[i - 1][I]
                # 新一轮结尾为u的，前一轮为i、o
                dp[i][U] = dp[i - 1][I] + dp[i - 1][O]
        return sum((dp[-1]))%(10**9+7)

s=Solution().countVowelPermutation(n=144)
print(s)