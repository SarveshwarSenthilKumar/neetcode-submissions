class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftSide=0
        rightSide=0
        maxArea=0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    area = abs(i-j)*min(heights[i],heights[j])
                    if area > maxArea:
                        maxArea=area
                        leftSide=i
                        rightSide=j
        return maxArea
        