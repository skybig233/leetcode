# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 11:18
# @Author  : Jiangzhesheng
# @File    : 1020.py
# @Software: PyCharm
# @Description:
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        ans=0
        direct=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(x,y):
            #为0或者超边界或者已经遍历则跳出
            if x<0 or x>m-1 or y<0 or y>n-1 or grid[x][y]==0 or visited[x][y]==True :
                return
            #为1则深度遍历
            else:
                visited[x][y]=True
                for i,j in direct:
                    dfs(x+i,y+j)

        # 只用深度搜索边界上的1
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(1,m):
            dfs(i,0)
            dfs(i,n-1)

        # 中间没有遍历到的1就需要计数了
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==False:
                    ans+=1

        return ans

grid=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
s=Solution().numEnclaves(grid)
print(s)