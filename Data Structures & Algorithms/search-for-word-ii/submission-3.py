"""
backtracking, keeping track of current word, as long as the next index
still exists in the trie, we continue until the word matches

{A: TrieNode} -> {T: }

"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.map = {}
                self.isTerminal = False

            def hasLetter(self, letter):
                return letter in self.map

            def addLetter(self, letter):
                new = TrieNode()
                self.map[letter] = new
                return new

            def getNext(self, letter):
                return self.map[letter]


        root = TrieNode()

        def addWord(word):
            curr = root

            for letter in word:
                if curr.hasLetter(letter):
                    curr = curr.getNext(letter)
                else:
                    curr = curr.addLetter(letter)
            
            curr.isTerminal = True

        for word in words:
            addWord(word)
        
        # -------------------------- 
        rows, cols = len(board), len(board[0])
        self.res = set()
        self.seen = set()

        def dfs(row, col, currWord, triePointer):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 

            if ((row, col)) in self.seen:
                return 

            nextLetter = board[row][col]

            if not triePointer.hasLetter(nextLetter):
                return

            nextNode = triePointer.getNext(nextLetter)
            nextWord = currWord + nextLetter

            if nextNode.isTerminal:
                self.res.add(nextWord)
                # print(nextWord)

            self.seen.add((row, col))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow, newCol = row + dx, col + dy
                dfs(newRow, newCol, currWord + nextLetter, triePointer.getNext(nextLetter))
            
            self.seen.remove((row, col))


        for row in range(rows):
            for col in range(cols):
                self.seen = set()
                dfs(row, col, "", root)


        return list(self.res)





        