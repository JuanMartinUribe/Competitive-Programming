class Solution:
    def eventualSafeNodes(self, arr: List[List[int]]) -> List[int]:

        graph = collections.defaultdict(list)
        for i,nbs in enumerate(arr):
            for nb in nbs:
                graph[i].append(nb)
        visited = collections.defaultdict(bool,key = lambda f:False)
        ans = []

        def dfs(node):
            if node in visited:
                return visited[node]
            if not graph[node]:
                ans.append(node)
                visited[node] = True
                return True
            else:
                visited[node] = False
                is_safe = True
                for nb in graph[node]:
                    is_safe &= dfs(nb)
                visited[node]=is_safe
                if is_safe:
                    ans.append(node)
                return is_safe
        for node in range(len(arr)):
            dfs(node)
        return sorted(ans)    
        