class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen = set(nums)
        new_list = []
        for index in range(1, len(nums) + 1):
            if index not in seen:
                new_list.append(index)
        return new_list

       