class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        R = len(obstacle_grid)
        C = len(obstacle_grid[0])
        @cache
        def paths(i,j):
            if i<0 or i==R or j<0 or j==C or obstacle_grid[i][j]==1:
                return 0
            elif i==R-1 and j==C-1:
                return 1
            else:
                return paths(i+1,j)+paths(i,j+1)
        return paths(0,0)
            