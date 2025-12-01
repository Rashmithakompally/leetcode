class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        left, right = 1, sum(batteries) // n  # max possible minutes

        def can_run(t):
            total = 0
            for b in batteries:
                total += min(b, t)
            return total >= t * n

        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1

        return left

