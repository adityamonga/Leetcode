class Solution:
    def checkValidString(self, s: str) -> bool:
        curr = []
        wild = []

        for index, char in enumerate(s):
            if char == '(':
                curr.append(index)
            elif char == ')':
                if curr:
                    curr.pop()
                elif wild:
                    wild.pop()
                else:
                    return False
            if char == '*':
                wild.append(index)
    
        i = 0
        while curr and wild and i < len(wild):
            if curr[0] < wild[i]:
                curr.pop(0)
                wild.pop(i)
            else:
                i += 1

        return not curr

    ### extremely optimized solution by some fucking genuis
    # def checkValidString(self, s: str) -> bool:
    #     lo = 0
    #     hi = 0
    #     for c in s:
    #         lo += 1 if c == '(' else -1
    #         hi += 1 if c != ')' else -1
    #         if (hi < 0) :
    #             break
    #         lo = max(lo, 0);
        
    #     return lo == 0;

if __name__ == '__main__':
    print(Solution().checkValidString('(*)'))
    print(Solution().checkValidString('(*))'))
    print(Solution().checkValidString('()'))
    print(Solution().checkValidString("(*()"))
    print(Solution().checkValidString("(((******))"))
    print(Solution().checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)"))
    print(Solution().checkValidString("(())(())(((()*()()()))()((()()(*()())))(((*)()"))


    # print(Solution().checkValidString("""
    #                                   (())
    #                                   (
    #                                   (())()()(*)
    #                                   (*()(())())()
    #                                   )
    #                                   ()()
    #                                   (
    #                                   (()())
    #                                   ((()))
    #                                   (*
    #                                   """))

