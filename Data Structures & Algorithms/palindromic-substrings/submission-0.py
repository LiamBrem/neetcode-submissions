class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def isSubstring(st):
            l, r = 0, len(st) - 1

            while l < r:
                if st[l] != st[r]:
                    return False

                l += 1
                r -= 1

            return True


        for i in range(len(s)):
            for j in range(i, len(s)):
                if isSubstring(s[i:j + 1]):
                    res += 1


        return res
