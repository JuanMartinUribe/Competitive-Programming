class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def combs(cur):
            nonlocal k
            if len(cur) == k:
                nonlocal ans
                ans.append(cur)
            else:
                last = cur[-1] if cur else -1
                for num in range(1,n+1):
                    if num not in cur and n-last>=k-len(cur) and num>last:
                        cur.append(num)
                        combs(cur[:])
                        cur.pop()
            return
        combs([])
        return ans
