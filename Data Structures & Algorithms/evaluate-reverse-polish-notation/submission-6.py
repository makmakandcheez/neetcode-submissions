class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '-':
                    stack.append(-(stack.pop() - stack.pop()))
                case '/':
                    temp = stack.pop()
                    stack.append(int(stack.pop() / temp))
                case _:
                    stack.append(int(token))

        return stack.pop()

            