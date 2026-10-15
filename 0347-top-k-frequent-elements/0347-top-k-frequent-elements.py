class Solution(object):
    def topKFrequent(self, nums, k):
        seen = {}
        for i in  nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        result = sorted(seen, key=seen.get, reverse=True)[:k]
        return result
         



         



         
        
        