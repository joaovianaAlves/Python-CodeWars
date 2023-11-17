def basic_op(operator, value1, value2):
    
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '/':
#         return value1 / value2
#     else:
#         return value1 * value2
    
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '/':
            return value1 / value2
        case '*':
            return value1 * value2
