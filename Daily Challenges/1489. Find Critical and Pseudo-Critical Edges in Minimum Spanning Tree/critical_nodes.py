#LAST MIN SUBMISSION UGLY CODE
# HARD QUESTION
# Minimum Spaning tree variation
class UnionFind():
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.edges = 0
    def union(self,a,b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a!=parent_b:
            self.edges+=1
        self.parents[parent_b] = parent_a
        return self.edges
    def find(self,a):
        while self.parents[a]!=a:
            a = self.parents[a]
        return a
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexes = {tuple(edge):i for i,edge in enumerate(edges)}
        edges.sort(key=lambda triplet:triplet[2])
        min_tree = UnionFind(n)
        min_tree_weight = 0
        cur_edges = 0
        for v1,v2,weight in edges:
            if min_tree.find(v1)!=min_tree.find(v2):
                min_tree.union(v1,v2)
                min_tree_weight += weight
                cur_edges+=1
            if cur_edges == n-1:
                break
        criticals = []
        pseudo_criticals = []
        for cur_edge in edges:
            cur_tree = UnionFind(n)
            cur_edges = 0
            cur_weight = 0
            is_critical = True
            for v1,v2,weight in edges:
                if cur_edge!=[v1,v2,weight] and cur_tree.find(v1)!=cur_tree.find(v2):
                    cur_tree.union(v1,v2)
                    cur_weight += weight
                    cur_edges += 1
                if cur_edges == n-1 and cur_weight==min_tree_weight:
                    is_critical = False
                    break
            
            if is_critical:
                criticals.append(indexes[tuple(cur_edge)])
            else:
                cur_tree = UnionFind(n)
                cur_edges = 1
                cur_weight = cur_edge[2]
                cur_tree.union(cur_edge[0],cur_edge[1])
                for v1,v2,weight in edges:
                    if cur_tree.find(v1)!=cur_tree.find(v2):
                        cur_tree.union(v1,v2)
                        cur_weight += weight
                        cur_edges += 1
                    if cur_edges == n-1 and cur_weight==min_tree_weight:
                        pseudo_criticals.append(indexes[tuple(cur_edge)])
                        break
        return [criticals,pseudo_criticals]


