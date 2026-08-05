# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        def same(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            elif root.val != subRoot.val:
                return False
            return same(root.left,subRoot.left) and same(root.right,subRoot.right)

        def dfs(root):
            if not root:
                return False

            if same(root,subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)


        
































