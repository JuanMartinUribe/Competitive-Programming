class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        deque = collections.deque()
        INF = 10**20
        ans = [[0 if num==0 else INF for num in row] for row in mat]
        DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(R):
            for j in range(C):
                if mat[i][j]==0:
                    deque.append([i,j])
        while deque:
            i,j = deque.popleft()
            for dx,dy in DIRS:
                nx,ny = i+dx,j+dy
                if 0<=nx<R and 0<=ny<C and ans[nx][ny]==INF:
                    ans[nx][ny]=ans[i][j]+1
                    deque.append([nx,ny])
        return ans