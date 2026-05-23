"""
position of ith car
speed of ith car
--
sort by positions

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort()
        times = []

        for position, speed in pairs:
            finish = (target - position) / speed
            times.append(finish)

        res = 0
        fastest = -1
        print(pairs)
        print(times)

        for i in range(len(times) -1, -1, -1):
            # [10, 8, 4, 5, 6]
            if times[i] > fastest:
                res += 1
                fastest = times[i]

        return res
            

        