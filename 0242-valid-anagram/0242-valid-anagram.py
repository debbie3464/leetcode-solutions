class Solution(object):
    def isAnagram(self, s, t):
        return True if sorted(t) == sorted(s) else False