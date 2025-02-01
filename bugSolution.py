def function_with_uncommon_error(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    elif a == 0:
        return b
    else:
        return a / b

result = function_with_uncommon_error(5, 0)
print(result)
result = function_with_uncommon_error(5,2)
print(result) 