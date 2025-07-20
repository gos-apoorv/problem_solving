class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }
        ans = []
        for d in digits:
            curr_chars = num_dict[d]
            if len(ans) < 1:
                ans.extend(curr_chars)
            else:
                tmp_ans = []
                for c in curr_chars:
                    tmp_ans = tmp_ans + [t + c for t in ans]
                ans = tmp_ans
        return ans
