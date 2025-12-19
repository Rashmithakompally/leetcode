from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        # People who know the secret
        secret = set([0, firstPerson])
        
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            graph = defaultdict(list)
            participants = set()
            
            # Collect all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                participants.add(x)
                participants.add(y)
                i += 1
            
            # BFS only among people who already know the secret
            queue = deque()
            visited = set()
            
            for p in participants:
                if p in secret:
                    queue.append(p)
                    visited.add(p)
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            
            # Add newly informed people
            secret.update(visited)
        
        return list(secret)
