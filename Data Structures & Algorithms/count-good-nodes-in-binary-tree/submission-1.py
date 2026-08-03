# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxValue = float('-inf')

        def dfs(root,maxValue):
            if not root:
                return 0
            cnt = 0
            if root.val >= maxValue:
                cnt += 1
            maxValue = max(maxValue,root.val)

            return cnt + dfs(root.left,maxValue) + dfs(root.right,maxValue)

        return dfs(root,maxValue)

            
        