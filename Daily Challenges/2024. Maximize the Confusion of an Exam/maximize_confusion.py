class Solution:
    def maxConsecutiveAnswers(self, answer_key: str, k: int) -> int:
        def calculate(target):
            left = k
            ans = 0
            r = 0
            for l,answer in enumerate(answer_key):
                r = max(l,r)
                while r<len(answer_key) and (answer_key[r]!=target or left):
                    if answer_key[r]==target:
                        left-=1
                    r+=1
                ans = max(ans,r-l)
                if answer==target:
                    left+=1
            return ans
        return max(calculate('F'),calculate('T'))
