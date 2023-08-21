# HARD QUESTION
# Variation of topological sorting 
class Solution:
    def topo_sort(self,graph):
        nodes = set(graph.keys())
        for n in graph:
            for nb in graph[n]:
                nodes.add(nb)
        arr = []
        
        visited = set()
        while len(arr)!=len(nodes):
            cant_visit = set()
            for node in nodes:
                if node not in visited:
                    for nb in graph[node]:
                        cant_visit.add(nb)
            can_visit = nodes-cant_visit-visited
            visited|=can_visit
            if not can_visit:
                return []
            arr+=list(can_visit)
        return arr
    def sortItems(self, n: int, m: int, group: List[int], before_items: List[List[int]]) -> List[int]:
        groups = collections.defaultdict(list)
        belongs_to = collections.defaultdict(int)
        groups_graph = collections.defaultdict(list)
        items_graph = collections.defaultdict(lambda:collections.defaultdict(list))

        for i,g in enumerate(group):
            if g!=-1:
                cur_group = g
            else:
                cur_group = i+m
            groups[cur_group].append(i)
            belongs_to[i] = cur_group
            items_graph[cur_group][i] = []

        for i,items in enumerate(before_items):
            for dependency in items:
                g1 = belongs_to[dependency]
                g2 = belongs_to[i]
                if g1!=g2:
                    if g2 not in groups_graph[g1]:
                        groups_graph[g1].append(g2)
                else:
                    items_graph[g1][dependency].append(i)
        for g in groups:
            if g not in groups_graph:
                groups_graph[g] = []

        sorted_groups = self.topo_sort(groups_graph)

        if not sorted_groups: 
            return []

        ans = []
        for g in sorted_groups:
            if len(groups[g])==1:
                ans.append(groups[g][0])
                continue
            sorted_g = self.topo_sort(items_graph[g])
            if not sorted_g: return []
            ans+=sorted_g
        return ans

            