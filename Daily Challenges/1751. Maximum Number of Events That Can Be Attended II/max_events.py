class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        points = collections.defaultdict(list)
        days = []
        final_day = -1
        for start,end,val in events:
            points[start].append([end,val])
            final_day = max(final_day,end)
            days.append(start)
        days.sort()
        #print(points)
        @cache
        def backtrack(i,k,can_end):
            nonlocal final_day
            nxt_day = bisect.bisect_right(days,i)
            #print(i,cur_val,k,can_end,nxt_day)
            if i > final_day or k == 0 or nxt_day==len(days):
                if k>0 and i in points and i>can_end:
                    return max(list(map(lambda f:f[1],points[i])))
                return 0
            ans = 0
            
            if i>can_end and i in points:
                for end,val in points[i]:
                    ans = max(ans,backtrack(days[nxt_day],k-1,end)+val)
            ans = max(ans,backtrack(days[nxt_day],k,can_end))
            return ans
        return backtrack(days[0],k,-1)    
            
            
            
            