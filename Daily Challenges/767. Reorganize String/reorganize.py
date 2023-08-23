class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        ans = []
        INF = 10**20
        for _ in range(len(s)):
            nxt = ""
            cur_amt = -INF
            for w,amt in cnt.items():
                if amt>0 and amt>=cur_amt and(not ans or ans[-1]!=w):
                    nxt = w
                    cur_amt = amt
            cnt[nxt]-=1
            ans.append(nxt)
            if not nxt:
                return ""
        return "".join(ans)
        