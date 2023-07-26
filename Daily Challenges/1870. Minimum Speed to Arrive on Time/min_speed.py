class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calculate(speed):
            if speed==0:
                return False
            cur_time = 0
            for i,d in enumerate(dist):
                if i<len(dist)-1:
                    cur_time += int(math.ceil(d/speed))
                else:
                    cur_time += d/speed
            return cur_time <= hour
        def bs(speed):
            l = 0
            r = 10**7+1
            while l<r:
                mid = (l+r)//2
                #print(mid,calculate(mid))
                if calculate(mid):
                    r = mid
                else:
                    l = mid+1
            return l
        
        ans = bs(10**7//2) 
        return ans if ans<=10**7 else -1