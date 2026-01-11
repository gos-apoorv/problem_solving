class Solution:
    def countAndSay(self, n: int) -> str:
        current_string = "1"

        for _ in range(n-1):
            j = 0
            k = 0
            next_string = ""

            while j < len(current_string):

                while k < len(current_string) and current_string[j] == current_string[k]:
                    k += 1
                
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string

        return current_string