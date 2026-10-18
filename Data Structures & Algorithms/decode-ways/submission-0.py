class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def helperMethod(ss: str) -> int:
            if len(ss) == 0 or ss[0] == "0":
                memo[ss] = 0
            elif len(ss) == 1:
                memo[ss] = 1
            elif len(ss) == 2:
                if int(ss) == 10 or int(ss) > 26:
                    memo[ss] = 1
                else:
                    memo[ss] = 2
                

            if ss in memo:
                return memo[ss]
            memo[ss] = helperMethod(ss[1:])
            if len(ss) >= 2 and int(ss[0:2]) <= 26:
                memo[ss] += helperMethod(ss[2:])
            return memo[ss]

        helperMethod(s)
        print(memo)
        return memo[s]