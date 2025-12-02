class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Numbers ending with zero cannot be palindrome unless the number is 0
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_num = 0
        original = x

        # Reverse half of the number
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # For even length, x == reversed_num
        # For odd length, x == reversed_num // 10
        return x == reversed_num or x == reversed_num // 10
