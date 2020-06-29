class Solution:
    # def backspaceCompare(self, S: str, T: str) -> bool:

    #     def render(s):
    #         if not s:
    #             return []
            
    #         s = list(s)
    #         rendered = []
    #         for char in s:
    #             if char != '#':
    #                 rendered.append(char)
    #                 continue

    #             elif rendered:
    #                 rendered.pop()

    #         return rendered

    #     return render(S) == render(T)

    def backspaceCompare(self, S: str, T: str) -> bool:
        def render(s):
            if not s:
                return []

            s = list(s)
            index=0
            while True:
                if index == len(s):
                    break

                if s[index] == '#':
                    if index != 0:
                        s.pop(index)
                        index -= 1
                    s.pop(index)
                    continue
                index += 1
            return s

        return render(S) == render(T)

if __name__ == '__main__':
    print(Solution().backspaceCompare("ab#c##", "aa#c###"))