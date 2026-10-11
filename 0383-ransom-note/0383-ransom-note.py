class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        for ch in ransomNote:
            if count.get(ch, 0) == 0:
                return False
            count[ch] -= 1

        return True
        