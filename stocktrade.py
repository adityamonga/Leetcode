class Solution:
    def maxProfit(self, prices) -> int:
        days = len(prices)
        if not prices:
            return 0

        profit = 0
        for i in range(1, days):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit+= diff
        return profit

if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([1,9,6,9,1,7,1,1,5,9,9,9]))
