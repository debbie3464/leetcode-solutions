class Solution(object):
    def frequencySort(self, s):
        seen = {}
        for ch in s:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch] += 1

        ordered = sorted(seen, key=seen.get, reverse=True)
        result = ""
        for ch in ordered:
            result += ch * seen[ch]
        return result