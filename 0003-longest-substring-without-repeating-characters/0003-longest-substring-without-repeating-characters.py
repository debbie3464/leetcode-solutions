class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = []
        max_count = 0

        for char in s:
            while char in seen:
                seen.pop(0)  
            
            seen.append(char)
            max_count = max(max_count, len(seen))
            
        return max_count

        
            
     

        