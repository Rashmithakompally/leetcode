class Solution:
    def countPartitions(self, nums):
        total = sum(nums)
        leftSum = 0
        count = 0
        
        for i in range(len(nums) - 1):
            leftSum += nums[i]
            rightSum = total - leftSum
            
            # Check if difference is even
            if (leftSum % 2) == (rightSum % 2):
                count += 1
        
        return count


# Example
nums = [10, 10, 3, 7, 6]
print(Solution().countPartitions(nums))
