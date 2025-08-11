class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        left_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]

        for i in range(len(nums)):
            # Check if left_sum equals right sum
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1