# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @staticmethod

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def depth(node):
            nonlocal diameter

            if not node:
                return 0

            lHeight = depth(node.left)
            rHeight = depth(node.right)

            diameter = max(diameter, lHeight+rHeight)

            return 1 + max(lHeight, rHeight)

        depth(root)
        return diameter
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # print(Solution().height(root))
    print(Solution().diameterOfBinaryTree(root))