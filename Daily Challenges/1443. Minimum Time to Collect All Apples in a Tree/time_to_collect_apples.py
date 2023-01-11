class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        time = 0 
        tree = collections.defaultdict(list)
        for parent,child in edges:
            tree[parent].append(child)
            tree[child].append(parent)
        path_has_apple = [False for _ in range(n)]
        visited = set()
        def dfs(node):
            visited.add(node)
            nonlocal path_has_apple
            is_apple = True if hasApple[node] else False
            childs_have_apple = False
            for child in tree[node]:
                if child not in visited:
                    childs_have_apple |= dfs(child)
            path_has_apple[node] = childs_have_apple or is_apple
            return path_has_apple[node]
        dfs(0)
        visited = set()
        def count_time(node):
            time = 0
            visited.add(node)
            for child in tree[node]:
                if child not in visited and path_has_apple[child]:
                    time+=count_time(child)+1
            return time+1
        return count_time(0)-1