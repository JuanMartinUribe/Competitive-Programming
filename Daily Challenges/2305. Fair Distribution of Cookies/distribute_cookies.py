class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = 10**8 
        @cache
        def combs(i,arr):
            if i==len(cookies):
                nonlocal ans
                ans = min(max(arr),ans)
                return
            elif max(arr)>=ans:
                return
            aux = list(arr)
            for child in range(k):
                aux[child]+=cookies[i]
                combs(i+1,tuple(aux))
                aux[child]-=cookies[i]
            return
        cookies.sort(reverse=True)
        arr = tuple([0]*k)
        combs(0,arr)
        return ans