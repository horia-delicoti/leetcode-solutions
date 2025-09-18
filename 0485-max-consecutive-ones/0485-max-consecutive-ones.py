class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] == 0:
                # Update max before resetting
                max_count = max(max_count, fast - slow)
                # Move slow to the element after this zero
                slow = fast + 1

        # in case array ends with 1s
        max_count = max(max_count, len(nums) - slow)
        return max_count