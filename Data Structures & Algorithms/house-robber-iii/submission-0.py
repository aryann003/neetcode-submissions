# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        @cache
        def dfs(root,flag):
            if not root:
                return 0
            if not flag:
                return dfs(root.left,True) + dfs(root.right,True)
            
            rob = root.val + dfs(root.left,False) + dfs(root.right,False)

            skip = dfs(root.left, True) + dfs(root.right, True)

            return max(rob,skip)

        return dfs(root,True)

