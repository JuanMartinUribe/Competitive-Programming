class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1]==1 or grid[0][0]==1: return -1
        visited = set()
        visited.add((0,0))
        N = len(grid)
        DIRS = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        found = False
        
        def bfs(arr):
            new_arr = []
            for (i,j) in arr:
                if i<0 or j<0 or i>=N or j>=N:
                    continue
                if i == N-1 and j == N-1:
                    nonlocal found
                    found = True
                    return 1
                for dx,dy in DIRS:
                    nx,ny = i+dx,j+dy
                    if (nx,ny) not in visited and 0<=nx<N and 0<=ny<N and grid[nx][ny]==0:
                        visited.add((nx,ny))
                        new_arr.append((nx,ny))
            if new_arr:
                return bfs(new_arr)+1
            return 0
        ans = bfs([(0,0)]) 
        return ans if found else -1
