class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        newHeight = 0
        maxVal = max(height)
        maxIndices = [i for i, x in enumerate(height) if x == maxVal]
        if len(maxIndices) >= 2:
            for h in range(maxIndices[0], maxIndices[-1]):
                total += maxVal - height[h]
        for h in range(maxIndices[0]):
            if newHeight < height[h]:
                newHeight = height[h]
            total += newHeight - height[h]
        newHeight = 0
        for h in range(len(height)-1, maxIndices[-1], -1):
            if newHeight < height[h]:
                newHeight = height[h]
            total += newHeight - height[h]
        return total