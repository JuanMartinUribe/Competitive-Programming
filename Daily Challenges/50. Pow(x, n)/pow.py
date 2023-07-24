class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calc(x,n):
            if n<0:
                return 1/calc(x,-n)
            elif n==0:
                return 1
            else:
                if n%2==0:
                    return calc(x*x,n//2)
                else:
                    return x*calc(x*x,(n-1)//2)
        return calc(x,n)