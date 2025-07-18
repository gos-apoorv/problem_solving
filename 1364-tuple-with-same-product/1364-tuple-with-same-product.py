class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        def check_pair(a, b, c, d) -> bool:
            return a * b == c * d

        product_list = []
        
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                product_list.append(nums[first] * nums[second])
        

        product_list.sort()

        match_count_dict = {}
        last_product = 0

        print(product_list)
        for product in product_list:

            match_count_dict[product] = match_count_dict.get(product, 0) + 1

        matching_pairs = 0
        match_count = 0
        for freq in  match_count_dict.values():
            matching_pairs = (freq - 1) * freq // 2
            match_count = match_count + matching_pairs
        return match_count*8
        # (match_count-1)*match_count*8//2