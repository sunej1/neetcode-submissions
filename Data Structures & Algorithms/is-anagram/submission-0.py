class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = dict()
        count2 = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count1[s[i]] = 1 if s[i] not in count1 else count1[s[i]]+1
            count2[t[i]] = 1 if t[i] not in count2 else count2[t[i]]+1
        return count1 == count2
            
        
