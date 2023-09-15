class UnionFind:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    def union(self,a,b):
        par_a = self.find(a)
        par_b = self.find(b)
        self.parents[par_b]=par_a
    def find(self,a):
        while self.parents[a]!=a:
            a = self.parents[a]
        return a


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return 0
        edges = []
        for i,(x1,y1) in enumerate(points):
            for j,(x2,y2) in enumerate(points):
                if i!=j:
                    dist = abs(x2-x1)+abs(y2-y1)
                    edges.append([i,j,dist])
        edges.sort(key=lambda x:x[2])
        
        cost = 0
        cur_edges = 0
        uf = UnionFind(len(edges))
        for v1,v2,weight in edges:
            if uf.find(v1)!=uf.find(v2):
                uf.union(v1,v2)
                cost+=weight
                cur_edges+=1
            if cur_edges == len(points)-1:
                return cost
        

        