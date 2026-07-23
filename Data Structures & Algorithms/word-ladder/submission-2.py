"""
- transform beginword to endword in minimum step
- path of words through wordList
- one step = same word in wordList with 1 different char
- bfs through graph to find shortest path
- adj list: 
    - word: [all words 1 away]
- how to calculate words 1 away:


"""
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        wordList = [beginWord] + wordList
        n, m = len(wordList), len(wordList[0])
        adj = defaultdict(list)

        def differsByOne(w1, w2):
            count = 0
            for i in range(m):
                if w1[i] != w2[i]:
                    count += 1
            
            return count == 1


        for i in range(n):
            for j in range(i + 1, n):
                w1, w2 = wordList[i], wordList[j]
                if differsByOne(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)

        
        q = deque([(beginWord, 0)])
        seen = set()


        while q:
            currWord, level = q.popleft()
            
            if currWord == endWord:
                return level + 1

            seen.add(currWord)

            for nextWord in adj[currWord]:
                if nextWord not in seen: 
                    q.append((nextWord, level + 1))


        return 0
                

        
                    
        