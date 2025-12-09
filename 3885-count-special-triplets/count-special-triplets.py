class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        from collections import defaultdict
        
        left = defaultdict(int)
        right = defaultdict(int)

        # All elements initially available on the right
        for x in nums:
            right[x] += 1

        ans = 0

        for x in nums:
            right[x] -= 1  # Move j from right to middle

            target = x * 2
            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % MOD

            left[x] += 1  # Move j to the left

        return ans
