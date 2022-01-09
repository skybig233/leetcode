# Definition for a binary tree node.
from leetcode_class import TreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif isinstance(root,TreeNode):
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        else:
            return 1

tree= TreeNode.deserialize(str([1,2,3,4,5,6]))
s=Solution().countNodes(tree)