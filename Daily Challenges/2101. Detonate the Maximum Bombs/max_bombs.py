class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)

        for i,(x1,y1,r1) in enumerate(bombs):
            for j,(x2,y2,r2) in enumerate(bombs):
                if i!=j:
                    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
                    if dist<=r1:
                        graph[i].append(j)
        def bfs(arr,visited):
            new_arr = []
            for bomb in arr:
                for nxt_bomb in graph[bomb]:
                    if nxt_bomb not in visited:
                        visited.add(nxt_bomb)
                        new_arr.append(nxt_bomb)
            if new_arr:
                return bfs(new_arr,visited)+len(new_arr)
            else:
                return 0
        ans = 0
        for i in range(len(bombs)):
            visited = set()
            visited.add(i)
            exploded = bfs([i],visited)
            ans = max(ans,exploded+1)
        return ans