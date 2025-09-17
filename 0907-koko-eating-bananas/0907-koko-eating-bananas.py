class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h <= len(piles):
            return max(piles)
        else:
            start = 1
            end = max(piles)

            while start < end:
                mid = (start + end) // 2
                hours_spend = 0

                for pile in piles:
                    hours_spend += math.ceil(pile/mid) 
                
                if hours_spend <= h:
                    end = mid
                else:
                    start = mid + 1
                
            return end
        