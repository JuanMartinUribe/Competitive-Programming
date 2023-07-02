class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        transfers = collections.defaultdict(int)

        def combs(cnt,cur_transfer):
            if cur_transfer == len(requests):
                return cnt if all(value == 0 for value in transfers.values()) else 0

            start,end = requests[cur_transfer]
            transfers[start]-=1
            transfers[end]+=1
            included = combs(cnt+1,cur_transfer+1)
            transfers[start]+=1
            transfers[end]-=1
            not_included = combs(cnt,cur_transfer+1)

            return max(included,not_included)
        return combs(0,0)