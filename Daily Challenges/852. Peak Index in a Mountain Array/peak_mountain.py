class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1

        while l<r:
            mid = (l+r)//2
            if 0<mid<len(arr)-1:
                if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                    return mid
                elif arr[mid]>arr[mid+1]:
                    r = mid
                else:
                    l = mid
            elif mid == len(arr)-1:
                r = mid-1
            else:
                l = mid+1
        