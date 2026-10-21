class Solution(object):
    def isValid(self, s):
        if len(s) % 2:
            return False
        match = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for ch in s:
            if ch in match:
                stack.append(match[ch])   
            elif not stack or stack.pop() != ch:
                return False
        return not stack