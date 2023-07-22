class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        DIRS = [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1)]
        cache = {}
        
        def combs(r,c,k):
            if (r,c,k) in cache:
                return cache[(r,c,k)]
            if r<0 or r>=n or c<0 or c>=n:
                return 0
            elif k==0:
                return 1
            prob = 0
            for dx,dy in DIRS:
                nr,nc = r+dx,c+dy
                prob += combs(nr,nc,k-1)
            prob/=8
            cache[(r,c,k)] = prob
            return prob
        return combs(row,column,k)
            