class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count, best = 0, 0
        for i in nums:
            if i == 1:
                count += 1
                if count > best:
                    best = count
            else:
                count = 0
        return best