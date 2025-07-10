class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_x = 0
        
        while x > 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and digit > 7):
                return 0
            
            reversed_x = reversed_x * 10 + digit
        
        return sign * reversed_x