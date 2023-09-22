class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        graph = {i:nodes for i,nodes in enumerate(graph)}
        N = len(graph.keys())
        INF = 10**20
        target = (1<<N)-1
        @cache
        def dfs(node,bm,dist):
            if bm == target:
                return dist
            ans = INF
            for nb in graph[node]:
                nxt_state = bm | (1<<nb)
                if (nb,nxt_state) not in visited or ((nb,nxt_state) in visited and visited[(nb,nxt_state)]>dist-1):
                    visited[(nb,nxt_state)]=dist+1
                    ans = min(ans,dfs(nb,nxt_state,dist+1))
            return ans
                 
        ans = INF
        for node in range(N):
            bm = 1<<node
            visited = {}
            visited[(node,bm)]=0
            ans = min(ans,dfs(node,bm,0))
        return ans