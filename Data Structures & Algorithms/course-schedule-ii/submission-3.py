class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []
        while queue:
            u = queue.popleft()
            result.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return result if len(result) == numCourses else []