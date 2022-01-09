import math
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==1:
            return [0,1]
        else:
            left=self.grayCode(n-1)
            # right=[left[i]+int(math.pow(2,n-1)) for i in range(len(left)-1,-1,-1)]
            right = [i+ int(math.pow(2, n - 1)) for i in left[::-1]]
            # right=[]
            # for i in range(len(left)-1,0,-1):
            #     right.append(left[i]+math.pow(2,n-1))
            return left+right

n=10
s=Solution().grayCode(n)
print(s)
