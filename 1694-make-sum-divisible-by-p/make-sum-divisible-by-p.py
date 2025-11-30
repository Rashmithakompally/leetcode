class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0  # Already divisible, remove empty subarray
        
        mp = {0: -1}   # prefix_sum % p → index
        prefix = 0
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - target) % p

            if need in mp:
                res = min(res, i - mp[need])

            mp[prefix] = i

        return res if res < len(nums) else -1
