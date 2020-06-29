# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True    

        return Solution.mirror(root.left, root.right)

    @staticmethod
    def mirror(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        outer = Solution.mirror(left.left, right.right)
        inner = Solution.mirror(left.right, right.left)
        return inner and outer


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))