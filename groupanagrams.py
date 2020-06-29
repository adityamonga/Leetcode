from collections import defaultdict
from functools import reduce

class Solution:
    def groupAnagrams(self, strs):
        unique = defaultdict(list)
        for word in strs:
            unique["".join(sorted(word))].append(word)
        return [item for item in unique.values()]


if __name__ == '__main__':
        # print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        print(Solution().groupAnagrams(["mod","mop","pip","tug","hop","dog","met","zoe","axe","mug","fdr","for","fro","fdr","pap","ray","lop","nth","old","eva","ell","mci","wee","ind","but","all","her","lew","ken","awl","law","rim","zit","did","yam","not","ref","lao","gab","sax","cup","new","job","new","del","gap","win","pot","lam","mgm","yup","hon","khz","sop","has","era","ark"]))
        # print(Solution().groupAnagrams(["pip", "did"]))
