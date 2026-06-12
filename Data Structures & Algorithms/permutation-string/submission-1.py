from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def isPermutation(s1, s2):
            return Counter(s1) == Counter(s2)

        for i in range(len(s2) - len(s1) + 1):
            if isPermutation(s2[i: i + len(s1)], s1):
                return True

        return False