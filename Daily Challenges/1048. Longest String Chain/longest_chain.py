class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = collections.defaultdict(list)
        def is_pre(w1,w2):
            if len(w2)-len(w1)!=1:
                return False
            mismatches = 0
            j = 0
            for i in range(len(w2)):            
                if i-mismatches<len(w1) and w1[i-mismatches]!=w2[i]:
                    mismatches+=1
                if mismatches>1:
                    return False
            return mismatches<=1
        for w1 in words:
            for w2 in words:
                if is_pre(w1,w2):
                    graph[w1].append(w2)
        @cache
        def dfs(cur):
            cur_l = 0
            for nb in graph[cur]:
                cur_l = max(cur_l,dfs(nb)+1)
            return cur_l
        ans = 0
        for w in words:
            ans = max(ans,dfs(w))
        return ans+1
