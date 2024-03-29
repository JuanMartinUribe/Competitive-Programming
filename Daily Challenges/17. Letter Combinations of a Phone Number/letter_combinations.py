class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }

        def combs(cur,i):
            if len(cur)==len(digits):
                return [cur] if cur else []
            else:
                ans = []
                for digit in digits[i]:
                    for letter in hashmap[digit]:
                        ans+=combs(cur+letter,i+1)
                return ans
        return combs('',0)
