class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[0] = 1
        prefix = [0] * (n + 1)
        prefix[0] = 1

        from collections import deque
        maxQ = deque()
        minQ = deque()

        left = 0

        for right in range(1, n + 1):

            # Maintain max queue
            while maxQ and nums[maxQ[-1]] <= nums[right - 1]:
                maxQ.pop()
            maxQ.append(right - 1)

            # Maintain min queue
            while minQ and nums[minQ[-1]] >= nums[right - 1]:
                minQ.pop()
            minQ.append(right - 1)

            # Shrink window if invalid
            while nums[maxQ[0]] - nums[minQ[0]] > k:
                left += 1
                if maxQ[0] < left:
                    maxQ.popleft()
                if minQ[0] < left:
                    minQ.popleft()

            # Calculate dp[right]
            dp[right] = (prefix[right - 1] - prefix[left - 1]) % MOD
            prefix[right] = (prefix[right - 1] + dp[right]) % MOD

        return dp[n]
