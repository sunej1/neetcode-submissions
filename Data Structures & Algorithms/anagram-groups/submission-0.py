class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        sol = []
        for words in groups:
            sol.append(groups[words])
        return sol

