# -*- coding: utf-8 -*-
# @Time    : 2022/1/15 12:51
# @Author  : Jiangzhesheng
# @File    : q1716.py
# @Software: PyCharm
# @Description:
class Solution:
    def totalMoney(self, n: int) -> int:
        """
        n/7=a余b，
        ans=（1+2+3+4+5+6+7）*a+（a-1）*7+
        :param n:
        :return:
        """