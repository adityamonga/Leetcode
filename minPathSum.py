from typing import List

class Node:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value
        self.down = None
        self.right = None

                        
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.grid = grid
        self.goal = (len(self.grid)-1, len(self.grid[0])-1)
        print("Making Tree")
        root = self.makeTree()

        return self.findMin(root)


    def findMin(self, node):
        if node.pos == self.goal:
            return node.value

        cost = node.value

        next_nodes = [i for i in (node.down, node.right) if i is not None]

        if next_nodes:
            cost += min(map(lambda x: self.findMin(x), next_nodes))

        return cost

    def makeTree(self):
        root = Node((0,0), self.grid[0][0])
        q = [root]

        while q:
            node = q.pop()
            i,j = node.pos[0], node.pos[1]
            if i + 1 < len(self.grid):
                node.down = Node((i+1, j), self.grid[i+1][j])
                q.append(node.down)

            if j + 1 < len(self.grid[0]):
                node.right = Node((i, j+1), self.grid[i][j+1])
                q.append(node.right)

        print("root::", root.value)
        return root



if __name__ == '__main__':
    print(Solution().minPathSum([
                                [1,3,1],
                                [1,5,1],
                                [4,2,1]
                                ]))
