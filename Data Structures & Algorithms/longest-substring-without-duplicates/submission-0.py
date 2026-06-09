class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0
        l = 0
        for r, char in enumerate(s):
            while char in chars:
                chars.remove(s[l])
                l += 1

            chars.add(char)
            res = max(res, r - l + 1)

        return res

