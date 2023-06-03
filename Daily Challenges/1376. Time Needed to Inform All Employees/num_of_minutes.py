class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = collections.defaultdict(list)
        time = collections.defaultdict(int)
        for i in range(len(manager)):
            if manager[i]!=-1:
                tree[manager[i]].append(i)
        for i,inf_time in enumerate(informTime):
            time[i] = inf_time
        
        def dfs(node):
            max_time = 0
            for child in tree[node]:
                max_time = max(max_time,dfs(child)+time[node])
            return max_time
            
        return dfs(headID)