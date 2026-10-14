class Solution(object):
    def longestCommonPrefix(self, strs):
        a, b = min(strs), max(strs)
        for i, ch in enumerate(a):
            if ch != b[i]:
                return a[:i]
        return a  
	        
      
        