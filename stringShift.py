from typing import List
from collections import deque

class Solution:
    # def stringShift(self, s: str, shift: List[List[int]]) -> str:
    #     self.l = list(s)
    #     for row in shift:
    #         side, amount = row[0], row[1]
    #         self.shift(side, amount)
    #     return "".join(self.l)


    # def shift(self, side, amount):
    #     if side == 0:
    #         for i in range(amount):
    #             self.l.append(self.l.pop(0))
    #     elif side == 1:
    #         for i in range(amount):
    #             self.l.insert(0, self.l.pop())

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        self.q = deque(s)
        for row in shift:
            side, amount = row[0], row[1]
            rotate = ((-1) ** (side+1)) * amount
            self.q.rotate(rotate)
        return "".join(self.q)

if __name__ == '__main__':
    print(Solution().stringShift('abc', [[0,1],[1,2]]))
    print(Solution().stringShift('abcdefg', [[1,1],[1,1],[0,2],[1,3]]))
