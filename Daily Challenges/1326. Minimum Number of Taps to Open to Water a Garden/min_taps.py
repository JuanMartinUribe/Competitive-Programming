class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        N = len(ranges)
        itvls = []
        for i,rang in enumerate(ranges):
            itvl = [max(i-rang,0),min(rang+i,N-1)]
            itvls.append(itvl)
        itvls.sort()

        cur_tap = 0
        cur_i = 0
        ans = 0
        while cur_tap<N-1:
            nxt_itvl = itvls[cur_i]
            while cur_i<N and itvls[cur_i][0]<=cur_tap:
                if itvls[cur_i][1]>nxt_itvl[1]:
                    nxt_itvl = itvls[cur_i]
                cur_i+=1
            if nxt_itvl[0]>cur_tap or nxt_itvl[1]<=cur_tap:
                return -1
            cur_tap = nxt_itvl[1]
            ans+=1
        return ans
            