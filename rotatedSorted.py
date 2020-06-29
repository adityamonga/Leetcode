from typing import List

class Solution:
    # def __init__(self, nums):
    #     self.nums = nums
        # pass

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        self.nums = nums
        if len(self.nums) < 3:
            if target in self.nums:
                return self.nums.index(target)
            else:
                return -1

        return self.search_by_half(0, len(self.nums)-1, target)
    
    def search_by_half(self, low, high, target):
        mid = (low + high) // 2

        if low > high:
            return -1

        if self.nums[mid] == target:
            return mid

        ## if left half is sorted
        if self.nums[low] <= self.nums[mid]:

            ## if key is present in left half
            if self.nums[low] <= target and self.nums[mid] >= target:
                return self.search_by_half(low, mid-1, target)

            ## if key is in right half
            else:
                return self.search_by_half(mid+1, high, target)

        ## if right half is sorted
        else:
            if self.nums[mid] <= target and self.nums[high] >= target:
                return self.search_by_half(mid+1, high, target)
            else:
                return self.search_by_half(low, mid-1, target)


if __name__ == '__main__':
    print(Solution().search([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], 2))
    print(Solution().search([4, 5, 6, 7, 8, 9, 0, 1, 2, 3], 2))
    print(Solution().search([4,5,6,7,0,1,2], 0))
    print(Solution().search([2,3,5,1], 1))
    # print(Solution([3,5,1,2]).rotatePoint(0, 3))

    # print(Solution([1,2,3,4]).binarySearch(0,4,4))