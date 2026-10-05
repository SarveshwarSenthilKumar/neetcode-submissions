class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index=[]
        for i in range(len(numbers)):
            tempnums=numbers[:]
            tempnums.remove(numbers[i])
            if target-numbers[i] in tempnums:
                if (target-numbers[i] == numbers[i]):
                    if tempnums.index(target-numbers[i])<=i:
                        return [i+1, numbers.index(target-numbers[i])+2]    
                    else: 
                        return [i+1, numbers.index(target-numbers[i])]
                return [i+1, numbers.index(target-numbers[i])+1] 
        