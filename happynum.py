from functools import lru_cache
from math import log10

## For next optimization use set instead of lru_cache
class Solution:
    def isHappy(self, n: int) -> bool:

        while 1:
            n = self.operate(n)

            if self.operate.cache_info().hits:
                self.clear()
                return False

            if (log10(n)).is_integer():
                self.clear()
                return True

    @lru_cache(maxsize=8)
    def operate(self, n):
        n_conv = 0
        while n:
            n_conv += (n%10)**2
            n = int(n/10)
        return n_conv

    def clear(self):
        self.operate.cache_clear()

if __name__ == '__main__':
    print(Solution().isHappy(7))
    print(Solution().isHappy(19))
    print(Solution().isHappy(5232465123))
    # print(Solution().operate(19))
