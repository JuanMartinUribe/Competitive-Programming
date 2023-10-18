class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(set)
        depends_on = collections.defaultdict(set)

        for pre,course in relations:
            graph[pre].add(course)
            depends_on[course].add(pre)
        
        ans = 0
        can_take = [course for course in range(1,n+1) if course not in depends_on]
        max_dep = {node:0 for node in range(1,n+1)}

        while can_take:
            nxt_can_take = []
            for course in can_take:
                for nxt in graph[course]:
                    depends_on[nxt].remove(course)
                    max_dep[nxt] = max(max_dep[nxt],time[course-1])
                    if not depends_on[nxt]:
                        nxt_can_take.append(nxt)
                        time[nxt-1]+=max_dep[nxt]
            can_take = nxt_can_take
            
        return max(time)
