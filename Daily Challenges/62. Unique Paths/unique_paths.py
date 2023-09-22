class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i,j):
            if i == m-1 and j==n-1:
                return 1
            elif not(0<=i<m and 0<=j<n):
                return 0
            return dp(i+1,j)+dp(i,j+1)
        return dp(0,0)