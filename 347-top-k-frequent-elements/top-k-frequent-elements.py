class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1 

        print(freq)
        values_list = sorted(list(freq.values()), reverse=True)
        print(values_list)
        min_value = values_list[k-1]

        freq_elem = [x for x in freq if freq[x] >=  min_value]

        return freq_elem

