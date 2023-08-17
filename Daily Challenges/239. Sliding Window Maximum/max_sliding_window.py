class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexes = collections.defaultdict(int)
        in_heap = collections.defaultdict(bool)
        l = 0
        r = k-1
        h = []
        heapq.heapify(h)
        def push(x):
            heapq.heappush(h,-x)
        def pop():
            return -heapq.heappop(h)
        for i in range(k):
            indexes[nums[i]]=i
            if not in_heap[nums[i]]:
                push(nums[i])
                in_heap[nums[i]]=True
        ans = []
        while r<len(nums):
            num = nums[r]
            indexes[num] = r
            if not in_heap[num]:
                push(num)
            #print(l,r,h,indexes)
            cur_max = -h[0]
            while indexes[cur_max]<l:
                in_heap[pop()] = False
                cur_max = -h[0]
            ans.append(cur_max)
            l+=1
            r+=1
        return ans



        

            
            