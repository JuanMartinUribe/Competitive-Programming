class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid<0:
                while stack and stack[-1]>=0 and -asteroid>stack[-1]:
                    stack.pop()
                if not stack or (stack and stack[-1]<0):
                    stack.append(asteroid)
                elif stack and stack[-1]==-asteroid:
                    stack.pop()
            else:
                stack.append(asteroid)
        return stack
