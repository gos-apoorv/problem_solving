from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        char_stack = []
        opr_stack = []
        s_len = len(s)
        prev_num = None

        def is_digit(s: str) -> bool:
            return s.isdigit()


        def apply_div_multiplication(a: str, b: str, opr: str)-> int:
            ans = 0
            # print(a, '----', b, '===========', opr)
            if opr == "/":
                ans = a // b
            else:
                ans = a * b
            return ans
        
        def handle_negative():
            i = 0
            for op in opr_stack:
                if op == '-':
                    opr_stack[i] = '+'
                    char_stack[i+1] = -1 * char_stack[i+1]
                i = i+1


        def empty_stack() -> int:
            ans = 0
            while len(char_stack) > 1:
                # print("es==",char_stack)
                b = int(char_stack.pop())
                operator = opr_stack.pop()
                a = int(char_stack.pop())

                if operator == "+":
                    ans = a + b
                else:
                    ans = a - b
                char_stack.append(ans)

            return char_stack.pop()

        for c in s:
            if not is_digit(c):
                if c == " ":
                    continue
                char_stack.append(prev_num)
                prev_num = None
                if len(opr_stack) > 0 and (opr_stack[-1] == "/" or opr_stack[-1] == "*"):
                    b = char_stack.pop()
                    a = char_stack.pop()
                    opr = opr_stack.pop()
                    ans = apply_div_multiplication(a, b, opr)
                    char_stack.append(ans)
                opr_stack.append(c)
            else:
                if prev_num != None:
                    curr_num = prev_num*10 + int(c)
                else:
                    curr_num = int(c)
                prev_num = curr_num

        char_stack.append(prev_num)  

        if len(opr_stack) > 0 and (opr_stack[-1] == "/" or opr_stack[-1] == "*"):
            b = char_stack.pop()
            a = char_stack.pop()
            opr = opr_stack.pop()
            ans = apply_div_multiplication(a, b, opr)
            char_stack.append(ans)
        handle_negative()
        # print(char_stack)
        # print(opr_stack)
        if len(char_stack) == 1:
            return int(char_stack.pop())

        return empty_stack()