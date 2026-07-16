class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def increment(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1


        for i in range(len(s)):
            l = r = i
            increment(l, r)

            l, r = i, i + 1
            increment(l, r)


        return self.res
