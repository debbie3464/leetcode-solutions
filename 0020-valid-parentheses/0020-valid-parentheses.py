class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:         
            return False

        pairs = {')': '(', ']': '[', '}': '{'}  
        stack = []

        for ch in s:
            if ch in pairs:                      
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:                               
                stack.append(ch)

        return len(stack) == 0