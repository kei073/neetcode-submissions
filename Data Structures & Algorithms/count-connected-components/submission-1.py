class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.par = [x for x in range(n)]
    
    def find(self, x: int) -> int:
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        self.par[x] = y
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        
        root_set = set()
        for x in range(n):
            root_set.add(uf.find(x))
        
        return len(root_set)

