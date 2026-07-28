class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        m = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def dfs(s, i):
            if i >= len(digits):
                self.res.append(s)
                return

            for c in m[digits[i]]:
                dfs(s + c, i + 1)

            
        dfs("", 0)
        return self.res if self.res[0] != "" else []
        