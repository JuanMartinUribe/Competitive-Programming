class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        ans = 0

        for i,itvl in enumerate(intervals[1:]):
            if itvl[0]<prev_end:
                prev_end = min(prev_end,itvl[1])
                ans+=1
            else:
                prev_end = itvl[1]
        return ans     