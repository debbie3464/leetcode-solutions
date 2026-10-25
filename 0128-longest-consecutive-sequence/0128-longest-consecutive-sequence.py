class Solution(object):
    def longestConsecutive(self, nums):
        seen = set(nums)
        best = 0
        for num in seen:
            if num - 1 not in seen:          # num starts a run
                length = 1
                while num + length in seen:  # keep walking up the run
                    length += 1
                best = max(best, length)
        return best