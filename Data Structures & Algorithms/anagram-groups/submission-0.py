class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            m = [0] * 26
            for ch in string:
                m[ord(ch) - ord('a')] += 1

            groups[str(m)].append(string)

        res = []

        for key in groups:
            res.append([])
            for string in groups[key]:
                res[-1].append(string)

        return res
            