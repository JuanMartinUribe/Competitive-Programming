class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = arr[1]-arr[0]

        for x1,x2 in zip(arr[1:],arr[2:]):
            if x2-x1!=delta:
                return False
        return True