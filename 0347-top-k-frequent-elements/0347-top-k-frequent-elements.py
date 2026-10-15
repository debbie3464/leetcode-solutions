class Solution(object):
    def topKFrequent(self, nums, k):
        seen = {}
        for i in  nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in seen.items():
            buckets[c].append(num)

        result = []
        for c in range(len(buckets) - 1, 0, -1):
            for num in buckets[c]:
                result.append(num)
                if len(result) == k:
                    return result
         



         



         
        
        