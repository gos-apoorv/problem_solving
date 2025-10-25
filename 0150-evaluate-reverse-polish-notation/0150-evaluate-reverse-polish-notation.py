class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        def is_num(c: str) -> bool:
            if len(c) == 1 and c in ["+", "-", "*", "/"]:
                return False
            
            return True

        def perform_operation(a: int, b: int, operator: str) -> int:
            if operator == "+":
                return a + b
            
            if operator == "-":
                return a - b
            
            if operator == "*":
                return a * b
            # print("operator==", a // b ,"-->", -1 * int(a / b))
            return int(a/b)

        for t in tokens:
            num_flag = is_num(t)
            # print(t,"-->",stack)
            if not num_flag:
                b = stack.pop()
                a = stack.pop()
                result = perform_operation(a, b, t)
                stack.append(result)
            else:
                stack.append(int(t))
            
            # print("post-->",stack)

        
        return stack.pop()