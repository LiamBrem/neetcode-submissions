"""
- basically: bigger, smaller, bigger, smaller, bigger, smaller...
2,4,3,2,2,5,1,4
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res = 1
        prev = ""

        while r < len(arr):
            if arr[r] > arr[r - 1] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"

            elif arr[r] < arr[r - 1] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"

            else:
                if arr[r] == arr[r - 1]:
                    r += 1
                
                l = r - 1
                prev = ""

        return res
       