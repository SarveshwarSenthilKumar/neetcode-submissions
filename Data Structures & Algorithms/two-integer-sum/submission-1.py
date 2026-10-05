class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            checker = target - nums[i]
            if checker in nums[i:len(nums)]:
                 return [i, nums[i:len(nums)].index(checker)]