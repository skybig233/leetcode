# -*- coding: utf-8 -*-
# @Time    : 2022/1/23 13:55
# @Author  : Jiangzhesheng
# @File    : q2034.py
# @Software: PyCharm
# @Description:
class StockPrice:
    TIMESTAMP=0
    PRICE=1
    def __init__(self):
        self.d={}
        self._max=(0,0)
        self._min=(0,10**9+1)
        self._current=(0,0)
    def update(self, timestamp: int, price: int) -> None:
        self.d[timestamp]=price
        if timestamp>=self._current[self.TIMESTAMP]:
            self._current=(timestamp,price)

        if price>self.maximum():
            self._max=(timestamp,price)
        elif timestamp==self._max[self.TIMESTAMP]:
            self._max=max(self.d.items(),key=lambda x:x[self.PRICE])

        if price<self.minimum():
            self._min=(timestamp,price)
        elif timestamp==self._min[self.TIMESTAMP]:
            self._min = min(self.d.items(),key=lambda x: x[self.PRICE])

    def current(self) -> int:
        return self._current[self.PRICE]

    def maximum(self) -> int:
        return self._max[self.PRICE]
        # return max(self.d.values())

    def minimum(self) -> int:
        return self._min[self.PRICE]
        # return min(self.d.values())



# l_func=["StockPrice","update","update","current","maximum","update","maximum","update","minimum"]
# l_args=[[],[1,10],[2,5],[],[],[1,3],[],[4,2],[]]

l_func=["StockPrice","update","minimum","update","update","minimum","minimum","update","maximum","update","minimum","current","minimum","update","current","minimum","current","current","update","maximum","maximum","update","minimum","minimum","maximum","maximum","update","maximum","current","maximum","minimum","minimum","update","current"]
l_args=[[],[45,9233],[],[55,9651],[37,3902],[],[],[25,4833],[],[53,4521],[],[],[],[22,1161],[],[],[],[],[55,6897],[],[],[20,5354],[],[],[],[],[30,5623],[],[],[],[],[],[25,2725],[]]

obj = StockPrice()
for i in range(1,len(l_func)):
    func=l_func[i]
    args=l_args[i]

    cmd='obj.'+func+str(tuple(args))
    print(eval(cmd))


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(2,2)
# obj.update(3,10)
# obj.update(1,3)
# obj.update(2,5)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()