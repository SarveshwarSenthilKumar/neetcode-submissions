class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    area = abs(i-j)*min(heights[i],heights[j])
                    if area > maxArea:
                        maxArea=area
        return maxArea
        