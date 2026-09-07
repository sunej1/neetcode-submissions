class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        memo[len(s)] = True

        def helperMethod(i: int) -> bool:
            if i in memo:
                return memo[i]
            else: 
                for word in wordDict:
                    if word in s and word == s[i:i+len(word)]:
                        memo[i+len(word)] = helperMethod(i + len(word))
                        if memo[i+len(word)]:
                            return True
                return False

        memo[0] = helperMethod(0)
        return memo[0]