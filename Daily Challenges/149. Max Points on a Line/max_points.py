class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = collections.defaultdict(set)
        INF =10**10
        def lineq(x1,x2,y1,y2):
            slope = (y2-y1)/(x2-x1) if x2-x1!=0  else INF
            
            # y = mx+b
            # b = y - mx
            yint = y1-slope*x1
            return (slope,yint)
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                slope = lineq(x1,x2,y1,y2)
                slopes[slope].add((x1,y1))
                slopes[slope].add((x2,y2))
        print(slopes)
        return len(max(slopes.values(),key=lambda f:len(f))) if slopes else 1
