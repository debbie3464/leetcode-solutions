class Solution(object):
    def isPalindrome(self, s):
        cleaned_text = "".join([char.lower() for char in s if char.isalnum()])


        if cleaned_text == cleaned_text[::-1]:
            return True
        else:
            return False

        
        