class Solution:
    def bestClosingTime(self, customers: str) -> int:
        INF = 10**20
        ans = 0
        penalty = INF
        N = len(customers)
        total_y = customers.count("Y")
        cur_y = 0
        cur_n = 0
        for i in range(N+1):
            cur_penalty = cur_n + total_y-cur_y
            if cur_penalty<penalty:
                penalty = cur_penalty
                ans = i
            if i==N:
                return ans
            if customers[i]=="Y":
                cur_y+=1
            else:
                cur_n+=1
