class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd
            size = 1
            while i - size >= 0 and i + size < len(s) and s[i - size] == s[i + size]:
                size += 1

            if (size - 1) * 2 + 1 > resLen:
                resLen = (size - 1) * 2 + 1
                res = s[i - size + 1: i + size]


            # even - going left
            size = 1
            while i - size >= 0 and i + size - 1 < len(s) and s[i - size] == s[i + size - 1]:
                size += 1

            if (size - 1) * 2 > resLen:
                resLen = (size - 1) * 2
                res = s[i - size + 1: i + size - 1]


        return res
        