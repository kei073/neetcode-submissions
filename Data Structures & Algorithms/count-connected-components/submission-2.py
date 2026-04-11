class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        def dfs(v):
            visited[v] = True
            for nv in graph[v]:
                if visited[nv]:
                    continue
                dfs(nv)
        
        res = 0
        for v in range(n):
            if visited[v]:
                continue
            dfs(v)
            res += 1
        
        return res

