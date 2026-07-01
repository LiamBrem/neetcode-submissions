class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxFreq = 0
        count = {}

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            
            if count[s[r]] > maxFreq:
                maxFreq = count[s[r]]

            
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)


        return res



        