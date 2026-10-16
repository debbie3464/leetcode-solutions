class Solution(object):
    def longestPalindrome(self, s):
        char_counts = Counter(s)
        length = 0
        has_odd = False        
        for count in char_counts.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True
        if has_odd:
            length += 1           
        return length
        