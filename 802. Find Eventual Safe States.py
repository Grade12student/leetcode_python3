class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0]*n     # 0: not visited, 1: visiting, 2: visited
        safe = []
        def isSafe(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            
            visited[node]=1
            for nextnode in graph[node]:
                if not isSafe(nextnode):
                    return False
            visited[node]=2
            return True

        for i in range(n):
            if isSafe(i):
                safe.append(i)
        return safe