from typing import List
from dsalgo.weighted_quick_union import UnionFind

class Solution:
    ## Optimized. Didn't need sets.
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.grid = grid
        self.rows, self.cols = len(self.grid), len(self.grid[0])
        islands = 0
        for rindex in range(self.rows):
            for cindex in range(self.cols):
                if self.grid[rindex][cindex] == "1":
                    self.findNeighbours(rindex, cindex)
                    islands += 1
        return islands

    def findNeighbours(self, rindex, cindex):

        if rindex < 0 or rindex >= self.rows\
        or cindex < 0 or cindex >= self.cols\
        or self.grid[rindex][cindex] == "0":
            return

        self.grid[rindex][cindex] = "0"
        self.findNeighbours(rindex-1, cindex)
        self.findNeighbours(rindex+1, cindex)
        self.findNeighbours(rindex, cindex-1)
        self.findNeighbours(rindex, cindex+1)

        return

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #     self.grid = grid
    #     self.rows, self.cols = len(self.grid), len(self.grid[0])
    #     islands = 0
    #     self.global_set = set()
    #     for rindex, row in enumerate(self.grid):
    #         for cindex, col in enumerate(row):
    #             if (rindex, cindex) not in self.global_set and self.grid[rindex][cindex] == "1":
    #                 self.global_set |= self.findNeighbours(rindex, cindex) or set()
    #                 islands += 1
    #     return islands

    # def findNeighbours(self, rindex, cindex):

    #     if rindex < 0 or rindex >= self.rows\
    #     or cindex < 0 or cindex >= self.cols\
    #     or self.grid[rindex][cindex] == "0"\
    #     or (rindex, cindex) in self.global_set:
    #         return

    #     self.global_set.add((rindex, cindex))
    #     self.global_set |= self.findNeighbours(rindex-1, cindex) or set()
    #     self.global_set |= self.findNeighbours(rindex+1, cindex) or set()
    #     self.global_set |= self.findNeighbours(rindex, cindex-1) or set()
    #     self.global_set |= self.findNeighbours(rindex, cindex+1) or set()

    #     return


if __name__ == '__main__':
    # pass
    print(Solution().numIslands([
                                ['1', '1', '1', '1', '0'], 
                                ['1', '1', '0', '1', '0'], 
                                ['1', '1', '0', '0', '0'], 
                                ['0', '0', '0', '0', '1']
                                ]
                                ))