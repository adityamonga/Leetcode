from typing import List
import sys

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        while len(self.stones) > 1:
            (first, first_index), (second, second_index) = self.max_two()
            debris = first - second

            if debris == 0:
                self.stones.remove(first)
            else:
                self.stones[first_index] = debris

            self.stones.remove(second)
        return self.stones[0] if self.stones else 0


    def max_two(self):
        first = second = -sys.maxsize
        first_index = second_index = None

        for index, weight in enumerate(self.stones):
            if weight > first and weight > second:
                second = first
                second_index = first_index

                first = weight
                first_index = index
            
            elif weight > second and weight <= first:
                second = weight
                second_index = index

        return (first, first_index), (second, second_index)

if __name__ == '__main__':
    # print(Solution().lastStoneWeight([6,0,1,2,3]))
    # print(Solution().lastStoneWeight([2,7,4,1,8,1]))
    print(Solution().lastStoneWeight([2,2]))
