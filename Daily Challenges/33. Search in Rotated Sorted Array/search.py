class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        l = 0
        r = len(nums)-1
        while nums[l]>nums[r]:
            mid = (l+r)//2
            if nums[mid]<nums[l]:
                r = mid
            else:
                l = mid+1
        offset = l

        print(offset)
        l = 0+offset
        n = len(nums)
        r = (n-1+offset)%n
        real_l = 0
        real_r = n-1

        while real_l<=real_r:
            real_mid = (real_l+real_r+1)//2
            mid = (real_mid+offset)%n
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                real_r = real_mid-1
            else:
                real_l = real_mid+1
        return -1