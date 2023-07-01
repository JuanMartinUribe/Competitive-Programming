class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def build_matrix(day):
            nonlocal col,row
            matrix = [[0]*col for _ in range(row)]
            for i,(r,c) in enumerate(cells):
                if i<day:
                    matrix[r-1][c-1]=1
                else:
                    return matrix
            return matrix
        
        def dfs(day):
            nonlocal col,row
            matrix = build_matrix(day)
            stack = []
            for c in range(len(matrix[0])):
                if matrix[0][c]==0:
                    stack.append((0,c))
            visited = set()
            DIRS = [(0,1),(1,0),(-1,0),(0,-1)]
            while stack:
                r,c = stack.pop()
                if r == row-1 and matrix[r][c]==0:
                    return True
                if (r,c) in visited: continue
                visited.add((r,c))
                for dx,dy in DIRS:
                    nx,ny = r+dx,c+dy
                    if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited and matrix[nx][ny]==0:
                        stack.append((nx,ny))
            return False
        
        l = 0
        r = len(cells)-1
        while l<=r:
            mid = (l+r+1)//2
            if dfs(mid) and l!=mid:
                l = mid
            else:
                r = mid-1
        return l