from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if len(beginWord) == 1:
            return 2
        count = 1
        queue = deque()
        explored = []

        for word in wordList:
            for i in range(len(word)):
                if beginWord[:i]+beginWord[i+1:] == word[:i]+word[i+1:]:
                    if word == endWord:
                        return 2
                    else:
                        explored.append(word)
                        queue.append(word)

        while queue:
            level_size = len(queue)
            count += 1
            words = list(set(wordList) - set(explored))

            for i in range(level_size):
                print(queue)
                begin = queue.popleft()

                for word in words:
                    for i in range(len(word)):
                        if begin[:i]+begin[i+1:] == word[:i]+word[i+1:]:
                            if word == endWord:
                                return count+1
                            else:
                                explored.append(word)
                                queue.append(word)
        return 0




