from typing import List

class Solution:
    # def countElements(self, arr: List[int]) -> int:
    #     count = 0
    #     for num in arr:
    #         count += 1 if arr.count(num+1) else 0
    #     return count

    # def countElements(self, arr: List[int]) -> int:
    #     sarr = sorted(arr)
    #     for index in range(len(sarr)-1):
    #         sarr[index] = sarr[index+1] - sarr[index]
    #     sarr.pop()
    #     print(sarr)
    #     return sarr.count(1)

    def countElements(self, arr: List[int]) -> int:
        seen = set()
        sarr = sorted(arr, reverse=True)
        count = 0
        for num in sarr:
            if num+1 in seen:
                count += 1
            seen.add(num)
        print(sarr)
        print(seen)
        return count

if __name__ == '__main__':
    print(Solution().countElements([1,3,2,3,5,0]))