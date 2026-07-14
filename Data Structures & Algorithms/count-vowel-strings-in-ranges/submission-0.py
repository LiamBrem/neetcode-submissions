class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        valid = [len(word) > 0 and word[0] in vowels and word[-1] in vowels for word in words]
        pref = [0] * len(valid)
        pref[0] = 1 if valid[0] else 0
        for i in range(1, len(valid)):
            pref[i] = pref[i - 1]
            if valid[i]:
                pref[i] += 1

        print(pref)

        for l, r in queries:
            if l > 0:
                res.append(pref[r] - pref[l - 1])
            else:
                res.append(pref[r])
            
        return res