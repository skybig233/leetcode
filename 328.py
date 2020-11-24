# -*- coding: utf-8 -*-
# @Time : 2020/11/13 9:44
# @Author : Jiangzhesheng
# @File : 328.py
# @Software: PyCharm
# Definition for singly-linked list.
from leetcode_class import ListNode
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            return head
        pre=head
        cnt=1
        while pre.next:
            pre=pre.next
            cnt+=1
        if cnt<3:
            return head

        cur = head.next
        tail=pre
        pre=head
        loop=int(cnt / 2)
        for i in range(loop):
            pre.next=cur.next
            cur.next=None
            tail.next=cur
            tail=tail.next
            pre=pre.next
            cur=pre.next
        return head
# head=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8))))))))
head=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
tmp=head.next
head,tmp=tmp,head
s=Solution().oddEvenList(head)