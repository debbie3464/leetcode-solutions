class Solution(object):
    def maxArea(self, height):
        left, right, best = 0, len(height) - 1, 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            if area > best:
                best = area
            if height[left] < height[right]:     
                left += 1
            else:                              
                right -= 1
        return best
        