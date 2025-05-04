class Solution:
    def minimumKeypresses(self, s: str) -> int:
        res = 0 

        # To create counter of each char
        cnts = collections.Counter(s)
        print(cnts)

        # Sort the Counter
        cnts = sorted(cnts.items(), key=lambda x: -x[1])
        print(cnts)


        for idx,(char, cnt) in enumerate(cnts):
            # For First chars in keyboard
            if idx <=8:
                res += cnt
            # For second chars in keyboard
            elif idx > 8 and idx <= 17:
                res += cnt*2
            else:
                res += cnt*3

        return res
