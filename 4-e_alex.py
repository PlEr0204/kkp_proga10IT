#постфиксная форма записи
def evaluate_postfix(expression):
    stack = []
    operators = {"+": lambda x, y: x + y,
                 "-": lambda x, y: x - y,
                 "*": lambda x, y: x * y,
                 "/": lambda x, y: x / y}

    for token in expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()

postfix_expression = "7 3 + 5 7 2 + - *"   # ввод формы
result = evaluate_postfix(postfix_expression)
print(result)
