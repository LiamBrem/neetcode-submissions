"""
all unique combinations of candidates that sum to target

"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.seen = set()

        
        def dfs(i, currSum, currList):
            if currSum == target:
                self.res.append(currList[:])

            if i >= len(candidates) or currSum >= target:
                return


            currList.append(candidates[i])
            dfs(i + 1, currSum + candidates[i], currList)
            currList.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            dfs(i + 1, currSum, currList)

        dfs(0, 0, [])
        return list(self.res)