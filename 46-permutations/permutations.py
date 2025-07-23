class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(curr, level):
            # print(curr)
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            level = "--|" + level
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    # print(level + "pre", curr , num, ans)
                    backtrack(curr, level)
                    curr.pop()
                    # print(level + "post", curr , num, ans)

        level = "->"
        backtrack([], level)
        
        return ans
