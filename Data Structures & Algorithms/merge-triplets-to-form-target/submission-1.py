class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f1 = f2 = f3 = False
        t1, t2, t3 = target

        for x1, x2, x3 in triplets:
            if x1 > t1 or x2 > t2 or x3 > t3:
                continue

            if x1 == t1:
                f1 = True

            if x2 == t2:
                f2 = True

            if x3 == t3:
                f3 = True

            if f1 and f2 and f3:
                break

        return f1 and f2 and f3
        