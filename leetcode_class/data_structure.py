# -*- coding: utf-8 -*-
# @Time : 2020/11/13 9:46
# @Author : Jiangzhesheng
# @File : data_structure.py
# @Software: PyCharm
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __len__(self):

    def __repr__(self) -> str:
        s = ''
        while self:
            s = s + str(self.val) + '->'
            self = self.next
        s += 'None'
        return s

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def serialize(cls,root):
        if not root: return "[]"
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(node.val)
            else:
                res.append(None)
        while res[-1] == None: res.pop()
        return str(res)

    @classmethod
    def deserialize(cls, data):
        if data == '[]': return None
        li = data[1:-1].split(',')
        queue = collections.deque()
        root = TreeNode(int(li[0]))
        queue.append(root)
        counter = 0
        for v in li[1:]:
            if counter == 0:
                parent = queue.popleft()
            if v.strip() != 'None':
                cur = TreeNode(int(v))
                queue.append(cur)
                if counter == 0:
                    parent.left = cur
                else:
                    parent.right = cur
            counter ^= 1
        return root