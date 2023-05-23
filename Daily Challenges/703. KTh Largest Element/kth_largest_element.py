from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sl = SortedList()
        self.k = k
        for num in nums:
            self.sl.add(num)

    def add(self, val: int) -> int:
        self.sl.add(val)
        return self.sl[len(self.sl)-self.k]
        a


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)