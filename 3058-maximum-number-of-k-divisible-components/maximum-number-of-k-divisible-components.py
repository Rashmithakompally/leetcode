class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        self.components = 0
        
        def dfs(node):
            visited[node] = True
            total = values[node]
            
            for nei in graph[node]:
                if not visited[nei]:
                    child_sum = dfs(nei)
                    total += child_sum
            
            # If the subtree sum is divisible by k → this is one full component
            if total % k == 0:
                self.components += 1
                return 0  # cut here → return 0 upward
            
            return total
        
        dfs(0)
        return self.components
