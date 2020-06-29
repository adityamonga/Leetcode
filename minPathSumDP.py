from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.grid = grid
        self.m, self.n = len(self.grid), len(self.grid[0])

        self.cost = [[0 for i in range(self.n)] for j in range(self.m)]

        ## Fill first row and column
        self.cost[0][0] = self.grid[0][0]

        for i in range(1, self.m):
            self.cost[i][0] = self.cost[i-1][0] + self.grid[i][0]

        for i in range(1, self.n):
            self.cost[0][i] = self.cost[0][i-1] + self.grid[0][i]
        
        # Fill the cost matrix
        for i in range(1, self.m):
            for j in range(1, self.n):
                self.cost[i][j] = self.grid[i][j] + min(self.cost[i-1][j], self.cost[i][j-1])

        return self.cost[self.m - 1][self.n - 1]


if __name__ == '__main__':
    print(Solution().minPathSum([
                                [1,3,1],
                                [1,5,1],
                                [4,2,1]
                                ]))
