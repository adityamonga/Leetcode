# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.answer = float('-inf')
        return self.findDepth(root, 0)
    
    def findDepth(self, node, depth):
        if not node:
            return self.answer
        self.answer = max(
            self.findDepth(node.left, depth+1),
            self.findDepth(node.right, depth+1),
            depth+1
        )
        return self.answer
        