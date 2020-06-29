from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            node = TreeNode(postorder.pop())
            node_index = inorder.index(node.val)
            
            lin = inorder[:node_index]
            rin = inorder[node_index+1:]
            node.left = self.buildTree(lin, [i for i in postorder if i in lin])
            node.right = self.buildTree(rin, [i for i in postorder if i in rin])
            
            return node

if __name__ == '__main__':
    Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
