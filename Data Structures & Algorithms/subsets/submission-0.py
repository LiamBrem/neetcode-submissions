class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(currList, i):
            if not self.res or currList != self.res[-1]:
                self.res.append(currList)

            if i >= len(nums):
                return


            dfs(currList, i + 1)
            dfs(currList + [nums[i]], i + 1)



        dfs([], 0)

        return self.res
        