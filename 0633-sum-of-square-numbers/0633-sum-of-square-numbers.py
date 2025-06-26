import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            sum = left * left + right * right
            if sum == c:
                return True
            elif sum > c:
                right -= 1
            else:
                left += 1
        return False