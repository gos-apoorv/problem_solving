class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(test_str: str) -> bool:
            count = 0
            for ch in list(test_str):
                if '(' == ch:
                    count += 1
                elif ')' == ch and count > 0:
                    count -= 1
                else:
                    return False
            return count == 0

        def backtracking(temp_str, left_count, right_count):
            set_str = []
            if len(temp_str) == 2 * n:
                if is_valid(temp_str):
                    # print("temp_str=",temp_str)
                    set_str.append(temp_str)
                    # print("set_str=",set_str)
            else:
                if left_count > 0:
                    left_str = backtracking(temp_str + '(', left_count - 1, right_count)
                    if left_str is not None:
                        set_str.extend(left_str)

                if right_count > 0:
                    right_str = backtracking(temp_str + ')', left_count, right_count - 1)
                    if right_str is not None:
                        set_str.extend(right_str)
            return set_str

        set_str = backtracking("(", n-1, n)
        print(set_str)
        return set_str