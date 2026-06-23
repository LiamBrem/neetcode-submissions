"""
return k (bananas per hour)

upper bound: max(piles)
lower bound: <- answer

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        # minimum val where totalTime < h

        def timeTaken(k):
            return sum([math.ceil(size/k) for size in piles])

        res = r
        while l <= r:
            k = (l + r) // 2

            # too long
            if timeTaken(k) > h:
                l = k + 1
            # too short
            else:
                res = k
                r = k - 1

        return res





        