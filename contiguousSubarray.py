from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        maxsize = 0
        accum = {0:[-1]}

        for i in range(len(nums)):
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1

            if balance in accum:
                accum[balance].append(i)
            else:
                accum[balance] = [i]

        for k,v in accum.items():
            if v[-1] - v[0] > maxsize:
                maxsize = v[-1] - v[0]

        return maxsize

    # def findMaxLength(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     maxsize = -1
    #     count = 0
    #     sumleft = []
    #     for num in nums:
    #         count = 1 if num == 1 else -1
    #         if not sumleft:
    #             sumleft.append(count)
    #         else:
    #             sumleft.append(sumleft[-1] + count)

    #     indices = {i:None for i in range(min(sumleft),max(sumleft)+1)}
    #     last_zero = -1
    #     for index, diff in enumerate(sumleft):
    #         if indices.get(diff) == None:
    #             indices[diff] = index
    #         else:
    #             maxsize = max(maxsize, index - indices[diff])

    #         if diff == 0:
    #             last_zero = index

    #     return max(maxsize,last_zero+1)



if __name__ == '__main__':
    print(Solution().findMaxLength([]))
    print(Solution().findMaxLength([0,1,0,1]))
    print(Solution().findMaxLength([0,0,1,1]))
    print(Solution().findMaxLength([0,1,0,1,0,0,0,1,1]))
    print(Solution().findMaxLength([0,1,0,1,0,0,0,1,1,1]))
