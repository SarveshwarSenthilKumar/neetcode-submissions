class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        first_set=[]
        for i in nums:
            if i not in first_set:
                first_set.append(i)
            else:
                return true
        return false