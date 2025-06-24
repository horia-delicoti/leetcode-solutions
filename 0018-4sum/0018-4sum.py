class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        # trying to use two pointers technique
        for i in range(n):
            for j in range(i+1, n):
                left = j + 1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums [j] + nums[left] + nums[right]
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Move left and right pointers to avoid duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        # Remove duplicates from the result
        result = [list(x) for x in set(tuple(x) for x in result)]
        # Sort the result to maintain order
        result.sort()
        # Return the result
        return result