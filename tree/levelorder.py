from queue import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.appendleft(root)
        data = []
        
        while q:
            row = []
            children = []
            for node in q:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
                row.append(node.val)

                q = deque(children)
            data.append(row)
        return data
