class Solution:
    def intToRoman(self, num: int) -> str:
        
        sym_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        
        t = num
        ans =  ""
    
        for n in sym_dict.keys():
            if t <= 0:
                break
            count, t = divmod(t,n) 
            ans = ans + (sym_dict[n]*count)
            # print(n, t, ans)
    
        return ans
        