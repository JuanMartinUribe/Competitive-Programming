class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        total = 0
        for num,amt in zip(cnt.keys(),cnt.values()):
            if amt==1:return -1
            elif amt%3==0:
                total+=amt//3
            elif amt%3==1:
                total+=(amt-4)//3+2
            elif amt%3==2:
                total+=(amt-2)//3+1
        return total