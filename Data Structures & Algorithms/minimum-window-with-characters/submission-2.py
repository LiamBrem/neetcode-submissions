"""
Brute force:
- counter of t
- for every substring in s:
    - for each char in substring, minus count from t counter
    - if t counter has none remaining -> good
    - keep track of minimum

Optimal:
- 

"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        total = len(t)
        l = 0
        res = ""
        resLen = float('inf')

        for r in range(len(s)):
            if s[r] in tCounter:
                if tCounter[s[r]] > 0:
                    total -= 1
                tCounter[s[r]] -= 1

            while total == 0:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]

                if s[l] in tCounter:
                    tCounter[s[l]] += 1
                    if tCounter[s[l]] > 0:
                        total += 1

                l += 1

            print(s[l: r+ 1])


        return res



            

            

            
        