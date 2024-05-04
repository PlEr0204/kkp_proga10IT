#префиксная форма
def evaluate_prefix(expression):
    stack = []
    operators = {"+": lambda x, y: x + y,
                 "-": lambda x, y: x - y,
                 "*": lambda x, y: x * y,
                 "/": lambda x, y: x / y}

    for token in reversed(expression.split()):
        if token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()
prefix_expression = "/ + 4 6 - + 4 7 1"  # ввод данных
result = evaluate_prefix(prefix_expression)
print(result)
