class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize new array for sum of amount for each customer
        max_amount = 0

        # Find the max amount and its index is richest customer
        # Start with assumption as first one
        for account in accounts:
            total = 0
            for amount in account:
                total = total + amount
            
            if max_amount < total:
                max_amount = total
        
        return max_amount

        