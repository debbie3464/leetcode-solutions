class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        majority = n//2
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for key,value in seen.items():
            if value > majority:
                return key  
                    