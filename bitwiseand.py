class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ## keep dividing by 2 till they become same. 
        ## add the number of divides as padding to the right
        s = 0
        while not m == n:
            m = m >> 1
            n = n >> 1
            s += 1
            print(bin(m), bin(n), s)
        return m << s

if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(503215,503200))