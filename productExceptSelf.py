from typing import List

class Solution:
    ## Time O(n) ; Space O(n)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     output = [0 for i in range(len(nums))]

    #     prefix = [0 for i in range(len(nums))]
    #     prefix[0] = 1

    #     suffix = [0 for i in range(len(nums))]
    #     suffix[-1] = 1
        
    #     for index in range(1, len(nums)):
    #         prefix[index] = prefix[index-1] * nums[index-1]
    #         output[index] = 
        
    #     for index in range(len(nums)-2, -1, -1):
    #         suffix[index] = suffix[index+1] * nums[index+1]

    #     for index in range(len(nums)):
    #         output[index] = prefix[index] * suffix[index]

    #     return output

    ## Time O(n); Space O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1 for i in range(length)]
        temp = 1

        for index in range(length):
            output[index] = temp
            temp *= nums[index]

        temp = 1

        for index in range(length-1, -1, -1):
            output[index] *= temp
            temp *= nums[index]

        return output


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))