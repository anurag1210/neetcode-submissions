class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={} #Create a count dictionary
        for num in nums:
            counts[num]=counts.get(num,0)+1
        return sorted(counts,key=counts.get,reverse=True)[:k]