class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_most_valid = 0
        longest = 0
        last_seen = {}

        for i, letter in enumerate(s):
            if letter in last_seen:
                left_most_valid = max(left_most_valid, last_seen[letter]+1)
            last_seen[letter] = 1
            longest = max(longest, i - left_most_valid + 1)
        return longest

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) < 2:
#             return len(s)
#         curr = set()
#         subs = 0
#         for trav in range(len(s)):
#             subs = max(subs, len("".join(curr)))
#             curr = set()
#             for char in s[trav:]:
#                 if char in curr:
#                     # subs = max(subs, len("".join(curr)))
#                     # curr = set()
#                     continue
#                 curr.add(char)
#             print(curr)
#         return max(subs, len(curr))

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("asjrgapa"))
    print(Solution().lengthOfLongestSubstring("au"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
