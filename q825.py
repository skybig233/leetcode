from typing import List
from collections import OrderedDict

MAX_AGE=120
class Solution:
    """
    每个人不会向比自己大的发好友，也不会比自己小太多的发好友
    年龄状态数120较少
    用户2*10^4较多，重复年龄较多
    考虑ordered_dict，年龄作为key，遍历年龄计算每个年龄的阈值，再相加。
    """
    def numFriendRequests(self, ages: List[int]) -> int:
        d=OrderedDict()
        for age in ages:
            d[age]=d.get(age,0)+1 #统计，无key设为0
        ans=0
        for i in d.keys():

            min_age=i//2+7 + 1 #最小向上取整
            max_age=i #最大不超过自身

            for j in range(min_age,max_age+1):
                if j==i: #A i 2
                    ans+=d.get(j,0)*(d.get(i,0)-1)
                else:
                    ans+=d.get(j,0)*d.get(i,0)

        return ans

ages=[20,30,100,110,120]
s=Solution().numFriendRequests(ages=ages)
print(s)