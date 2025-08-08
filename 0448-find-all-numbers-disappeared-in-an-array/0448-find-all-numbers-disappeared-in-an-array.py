class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dict = {}
        missing = []

        for i in range(n):
            dict[i+1] = 0
        for j in dict:
            dict[nums[j-1]] = 1
        print(dict)

        for x in dict:
            if dict[x] == 0:
                missing.append(x)
        
        return missing