class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        p_list = []
        pos = 0
        final_string = s
        for char in s:
            print("char=", char)
            if '(' == char:
                p_list.append(("(", pos))
            elif ')' == char:
                last_p, _ = p_list[-1] if len(p_list) > 0 else ("", 0)
                if last_p == "(":
                    _, _ = p_list.pop()
                else:
                    p_list.append((")", pos))
            pos += 1
        print("p_list=", p_list)
        if len(p_list) > 0:
            string_list = list(final_string)
            for _, index in p_list:
                string_list[index] = ""
            final_string = "".join(string_list)
        else:
            final_string = s
        return final_string