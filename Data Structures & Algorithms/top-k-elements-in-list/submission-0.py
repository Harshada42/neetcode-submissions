class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tally = {}
        for num in nums:
            if num not in tally:
                tally[num] = 1
            else:
                tally[num] = tally[num] + 1
        sorted_numbers = sorted(tally, key=tally.get, reverse=True)
        
        return sorted_numbers[:k]