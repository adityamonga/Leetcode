class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = 0
        while 1:
            num = sum([int(i)**2 for i in str(n)])

            if num in seen:
                seen = set()
                return False

            if num == 1:
                return True

            seen.add(num)
            n = num

if __name__ == '__main__':
    print(Solution().isHappy(7))