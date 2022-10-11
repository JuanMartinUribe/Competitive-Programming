class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = 10**20
        n1 = n2 = INF
        
        for num in nums:
            if num>n2:
                return True
            elif num>n1:
                n2 = min(num,n2)
            n1 = min(num,n1)
        return False