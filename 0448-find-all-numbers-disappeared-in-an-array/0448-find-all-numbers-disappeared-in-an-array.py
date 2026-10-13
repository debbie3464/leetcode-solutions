class Solution(object):
    def findDisappearedNumbers(self, nums):
        num_sorted = set(sorted(nums))
        new_list = []
        for index, num in enumerate (nums, start = 1):
            if index != num and index not in num_sorted:
                    new_list.append(index)
        return new_list

       