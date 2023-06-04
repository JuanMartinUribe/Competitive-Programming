class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()

        def dfs(node):
            for edge in graph[node]:
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge)
        provinces = 0
        for node in range(len(isConnected)):
            if node not in visited:
                visited.add(node)
                dfs(node)
                provinces+=1
        return provinces