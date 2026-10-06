class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        longest = 0
        current = 0

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue  
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1  
            longest = max(longest, current)

        return longest