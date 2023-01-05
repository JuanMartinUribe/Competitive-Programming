class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda f:f[1])
        INF = 10**10
        current = -INF
        total = 0
        for x1,x2 in points:
            if current<x1:
                current = x2
                total+=1
        return total