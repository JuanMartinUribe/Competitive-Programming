class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        freqs = collections.defaultdict(int)
        s = list(set(s))
        for w in s:
            freqs[cnt[w]]+=1
        ans = 0
        for w in s:
            if freqs[cnt[w]]>1:
                cur_freq = cnt[w]
                freqs[cur_freq]-=1
                while cur_freq in freqs:
                    cur_freq-=1
                    ans+=1
                if cur_freq>0:
                    freqs[cur_freq]+=1
        return ans