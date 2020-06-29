class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        turn = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[turn], nums[index] = nums[index], nums[turn]
                turn += 1
        return nums

if __name__ == '__main__':
    # print(Solution().moveZeroes([1,0,2,0,3]))
    print(Solution().moveZeroes([0,0,1]))
