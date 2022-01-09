from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n==len(original):
            ans=[[0 for j in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    ans[i][j]=original[i*n+j]
            return ans
        else:
            return []

original = [1,2,3]
m = 1
n = 3
s=Solution().construct2DArray(original,m,n)
print(s)