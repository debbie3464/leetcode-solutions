class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            return (nums1[length/2]+nums1[length/2-1])/2.0
        return nums1[length/2]
        




        