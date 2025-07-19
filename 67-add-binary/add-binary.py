class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0

        a_len = len(a) 
        b_len = len(b) 

        max_len = max(a_len, b_len)

        final_a = "".join(['0'] * (max_len - a_len)) + a
        final_b = "".join(['0'] * (max_len - b_len)) + b

        final_str = ""
        # print("final_a=", final_a, " final_b=", final_b)
        for i in range(max_len-1, - 1, -1):
            # print("i=", i, " carry=", carry, " final_a[i]=", final_a[i], " final_b[i]=", final_b[i])
            sum = carry + int(final_a[i]) + int(final_b[i])

            curr_dig = sum % 2
            carry = sum // 2
            final_str = str(curr_dig) + final_str
            # print("carry=", carry, " curr_dig=", curr_dig, " final_str=", final_str)

        if carry > 0:
            final_str = str(carry) + final_str

        return final_str
        