class Solution:
    def maxSubArray(self, nums) -> int:
        max_till_here = nums[0]
        max_all_time = nums[0]

        for i in range(1, len(nums)):
            max_till_here = max(nums[i], nums[i]+max_till_here)
            max_all_time = max(max_all_time, max_till_here)
        return max_all_time

if __name__ == '__main__':
    # print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    # print(Solution().maxSubArray([-1,0,1,2,3,-10,10]))
    print(Solution().maxSubArray([1,-3,2,1,-1]))
