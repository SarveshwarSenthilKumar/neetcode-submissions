class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alreadySeen=[]
        count=0
        highestCount=0
        for char in s:
            if char in alreadySeen:
                count=0
                alreadySeen=[]
            else:
                count+=1
                alreadySeen.append(char)
                if count > highestCount:
                    highestCount = count
        return highestCount