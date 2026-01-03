class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        final_sum = 0

        num1_len = len(num1)
        num2_len = len(num2)

        outer_multiplier = 1
        for i in range(num1_len-1,-1,-1):
            d = int(num1[i])
            temp_sum = 0
            multiplier = 1
            carry = 0
            for j in range(num2_len-1,-1,-1):
                x = int(num2[j])
                result = (x * d)  + carry
                temp_sum += multiplier*(result%10)
                carry = result // 10
                multiplier *= 10
            
            final_sum += outer_multiplier*(temp_sum + multiplier*carry)
            outer_multiplier *= 10
            print("d=",d,"|final_sum=",final_sum)

        return str(final_sum)
