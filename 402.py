
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def remove_index(num:str,idx:int)->str:
            tmp_list=list(num)
            tmp_list.pop(i)
            ans=''.join(tmp_list)
            return ans
        if len(num)==k:
            return '0'
        while k>0:
            for i in range(1,len(num)-1):
                if num[i]>num[i-1] and num[i]>=num[i+1]:
                    print(num)
                    num=remove_index(num,i)
                    k-=1
                    break
        return num

test_str="1432219"
k=3
s=Solution().removeKdigits(test_str,k)