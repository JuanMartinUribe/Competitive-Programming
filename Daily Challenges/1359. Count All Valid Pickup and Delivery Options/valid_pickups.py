class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def combs(p,d):
            if d == 0:
                return 1
            if p<0 or p>d:
                return 0
            ans = 0
            if p<d:
                ans+=combs(p,d-1)*(d-p)%MOD
            return ans+combs(p-1,d)*p%MOD
        return combs(n,n)%MOD