class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for size in asteroids:
            if size < 0:
                while s and s[-1] < abs(size) and s[-1] > 0:
                    s.pop()
                
                if not s or s[-1] < 0:
                    s.append(size)

                elif s and s[-1] == abs(size):
                    s.pop()


                
            else:
                s.append(size)

        return s
                
        