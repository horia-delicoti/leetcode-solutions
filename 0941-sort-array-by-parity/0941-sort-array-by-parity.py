class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        return nums