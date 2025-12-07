class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # If both are even
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        # Otherwise (at least one is odd)
        return (high - low) // 2 + 1


# Example usage:
low = 3
high = 7
print(Solution().countOdds(low, high))   # Output: 3
