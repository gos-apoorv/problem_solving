from math import e, log

class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        ans = int(e ** (0.5*log(x)))

        final = ans if (ans+1)*(ans+1) > x else ans+1

        return final 
        