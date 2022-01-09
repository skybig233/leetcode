# from typing import List
# class Solution:
#     """
#
#     """
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         sort_list=sorted(words,key=lambda x:len(x))
#         n=len(words)
#         dp=[[0 for i in range(n)] for j in range(n)]
#         dp[0]=sort_list
#         for i in range(1,n):
#             for j in range(n):
#                 dp[i][j]=string_minus(dp[i-1][j],sort_list[i-1])
#         return sort_list
# def string_minus(a:str,b:str)->str:
#     if a[:len(b)]==b:
#         return a[len(b):]
#     else:return a
# words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# s=Solution().findAllConcatenatedWordsInADict(words)
# print(s)