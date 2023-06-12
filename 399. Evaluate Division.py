from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph and populate the division values
        graph = defaultdict(dict)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value
        
        # Step 2: Evaluate the queries using DFS
        def dfs(numerator, denominator, visited):
            if numerator not in graph or denominator not in graph:
                return -1.0
            if numerator == denominator:
                return 1.0
            visited.add(numerator)
            for neighbor, value in graph[numerator].items():
                if neighbor not in visited:
                    result = dfs(neighbor, denominator, visited)
                    if result != -1.0:
                        return value * result
            return -1.0
        
        # Step 3: Process each query
        results = []
        for numerator, denominator in queries:
            results.append(dfs(numerator, denominator, set()))
        return results
