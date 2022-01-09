# -*- coding: utf-8 -*-
# @Time : 2020/11/11 17:26
# @Author : Jiangzhesheng
# @File : q514.py
# @Software: PyCharm
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # 子问题1：（0~n-1）n个数围成一个圈，i和j的最短距离是多少？
        def compute_dist(i: int, j: int, n: int) -> int:
            return min(abs(i - j), abs(n - abs(i - j)))

        # 子问题2：如何找到一个index到另一个char的最短位置？
        # 将ring遍历，记录每个char的index
        # 计算所有cur_index到char_index的值，找出最小的
        # d={}
        # for i in range(len(ring)):
        #     if ring[i] in d:
        #         d[ring[i]].append(i)
        #     else:
        #         d[ring[i]]=[i]

        # def find_min_dist(cur_idx:int,char:str)->int:
        #     for char_idx in d[char]:
        #         tmp_dist=compute_dist(cur_idx,char_idx,len(ring))
        #         if tmp_dist<min_dist:
        #             min_dist=tmp_dist
        #             min_idx=char_idx
        #     return min_dist,min_idx

        # cur_idx=0
        # sum_op=0

        # print (d)
        # for i in key:
        #     dist,cur_idx=find_min_dist(cur_idx,i)
        #     print(dist,cur_idx)
        #     sum_op+=dist+1
        # return sum_op

        # 本题不能用贪心算法，用动态规划
        m = len(ring)
        n = len(key)
        dp = [[100] * m for i in range(n)]
        cur_compute_idx, dist_list ,pre_compute_idx= [], [],[]
        for i in range(m):
            if ring[i] == key[0]:
                dp[0][i]=compute_dist(0,i,m)
                pre_compute_idx.append(i)

        for i in range(1,n):
            cur_compute_idx = []
            for j in range(m):
                if ring[j] == key[i]:
                    cur_compute_idx.append(j)
                    for idx in pre_compute_idx:
                        dist_list.append(dp[i - 1][idx] + compute_dist(idx, j,m))
                    dp[i][j] = min(dist_list)
                    dist_list=[]
            pre_compute_idx = cur_compute_idx
        return min(dp[-1])+n

s=Solution()
ring="xrrakuulnczywjs"
key="jrlucwzakzussrlckyjjsuwkuarnaluxnyzcnrxxwruyr"
print(s.findRotateSteps(ring,key))