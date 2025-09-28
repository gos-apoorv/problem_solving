class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        len_s1 = len(str1)
        len_s2 = len(str2)

        def check_valid(k):
            if len_s1 % k !=0 or len_s2 % k !=0:
                return False

            n1, n2 = len_s1 // k, len_s2 // k

            sub_str = str1[: k]

            return str1 == sub_str * n1 and str2 == sub_str * n2

        for i in range(min(len_s1, len_s2), 0 , -1):
            if check_valid(i):
                return str1[:i]
        
        return ""



        