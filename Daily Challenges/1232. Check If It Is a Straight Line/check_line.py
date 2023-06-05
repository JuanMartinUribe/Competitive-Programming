class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        INF = 10**20
        slope = (y2-y1)/(x2-x1) if x2-x1!=0 else INF
        for x2,y2 in coordinates[2:]:
            new_slope = (y2-y1)/(x2-x1) if x2-x1!=0 else INF
            if new_slope!=slope:
                return False
        return True
        