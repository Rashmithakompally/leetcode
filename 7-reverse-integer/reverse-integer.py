class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647
        
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow BEFORE inserting digit
            if rev > (INT_MAX - digit) // 10:
                return 0
            
            rev = rev * 10 + digit
        
        return sign * rev
