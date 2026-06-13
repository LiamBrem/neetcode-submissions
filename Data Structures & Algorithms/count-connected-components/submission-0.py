from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
    
        seen = set()
        res = 0
    
        for start in range(n):
            if start in seen:
                continue
    
            res += 1
            q = deque([start])
    
            while q:
                curr = q.popleft()
    
                if curr in seen:
                    continue
    
                seen.add(curr)
    
                for node in adj[curr]:
                    if node not in seen:
                        q.append(node) 
    
        return res