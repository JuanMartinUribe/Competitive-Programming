# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        l = 1
        r = N-2
        peak = 0
        while l<=r:
            m = (l+r+1)//2
            mid = mountain_arr.get(m)
            nxt = mountain_arr.get(m+1)
            if mid<nxt:
                l=m+1
            elif mid>nxt:
                peak = m
                r = m-1
        
        def bs(l,r,target,reverse=False):
            while l<=r:
                mid = (l+r+1)//2
                cur = mountain_arr.get(mid)
                if cur==target:
                    return mid
                if cur<target:
                    if reverse:
                        r = mid-1
                    else:
                        l = mid+1 
                else:
                    if reverse:
                        l = mid+1
                    else:
                        r = mid-1
            return -1
        left = bs(0,peak,target) 
        right = bs(peak,N-1,target,True)

        return left if left!=-1 else right