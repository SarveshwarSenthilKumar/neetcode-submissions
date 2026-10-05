class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            checker = target - nums[i]
            if checker in nums:
                 return [i, nums.index(checker)]