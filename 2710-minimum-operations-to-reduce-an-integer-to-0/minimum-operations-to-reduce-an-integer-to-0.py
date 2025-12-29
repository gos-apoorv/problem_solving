class Solution:
    def minOperations(self, n: int) -> int:

        pows = [2 ** num for num in range(17)]
        count = 0


        while n:
            for i in range(len(pows)):
                if pows[i] > n:
                    break

            
            n = min( abs(pows[i]-n), abs(pows[i-1] - n))
            count += 1

        
        return count 
        