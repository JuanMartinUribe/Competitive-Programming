class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []
        for i in range(num_rows):
            cur = []
            for j in range(i+1):           
                if triangle and triangle[-1] and j>0 and j<len(triangle[-1]):
                    cur.append(triangle[-1][j-1]+triangle[-1][j])
                else:
                    cur.append(1)
            triangle.append(cur)
        return triangle