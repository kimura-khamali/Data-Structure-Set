def evaluate_stack(expression):
    stack = [] 
    operators = set(['+', '-', '*', '/']) 

    for token in expression.split():
        if token not in operators:
            stack.append(float(token))
        else:
            if len(stack) < 2:
                return "Error: Not enough operands"
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    return "Error: Division by zero"
                stack.append(a / b)

    if len(stack) != 1:
        return "Error: Invalid expression"
    
    return stack[0] 

expressions = [
    "3 4 +",
    "5 2 * 4 +",
    "10 5 2 * -",
    "20 5 /",
    "3 4 + 2 *",
    "3 + 4",     
    "5 0 /"    
]

for expr in expressions:
    result = evaluate_stack(expr)
    print(f"Expression: {expr}")
    print(f"Result: {result}")
    print()