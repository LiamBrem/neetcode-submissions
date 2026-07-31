"""
initial = array same size as target with all 0s

1 opeation:
    - any subarray from initial and increment each value by 1

minimum number of operations from initial -> target
---
Greedy: want to increase as many elements at a time at the start

"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
    
        for i in range(1, len(target)):
            ans += max(0, target[i] - target[i-1])

        return ans