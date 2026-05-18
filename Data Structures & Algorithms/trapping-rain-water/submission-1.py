"""
max water at an index:
  = min(highest to left, highest to right)
  - height of current index



"""

class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0] * len(height)
        suff = [0] * len(height)

        for i in range(len(height)):
            j = len(height) - i - 1

            if i == 0:
                pref[i] = height[i]
                suff[j] = height[j]

            else:  
                pref[i] = max(pref[i - 1], height[i])
                suff[j] = max(suff[j + 1], height[j])


        total = 0

        for i in range(len(height)):
            total += min(pref[i], suff[i]) - height[i]
        


        return total
