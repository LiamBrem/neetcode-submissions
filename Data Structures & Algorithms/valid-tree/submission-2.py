"""
no cycles (no repeats on dfs)

"""
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for t, f in edges:
            adj[t].append(f)
            adj[f].append(t)

        self.seen = set()

        def dfs(curr, prev):
            self.seen.add(curr)

            for neighbor in adj[curr]:
                if neighbor not in self.seen:
                    if dfs(neighbor, curr):
                        return True

                elif neighbor != prev:
                    return True

            return False
                

        self.seen = set()

        if dfs(0, -1):
            return False

        if len(self.seen) != n:
            return False


        return True
        