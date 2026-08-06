class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexMap = {}
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i

        self.preIndex = 0

        def build(left, right):

            if left > right:
                return None

            value = preorder[self.preIndex]
            self.preIndex += 1

            root = TreeNode(value)

            index = indexMap[value]

            root.left = build(left, index - 1)
            root.right = build(index + 1, right)

            return root

        return build(0, len(inorder) - 1)