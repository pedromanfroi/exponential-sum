def multiply(a, b):
    return sum([a for _ in range(b)])

def expo_sum(x, y):
    if x < 0 or y < 0:
        return "Please enter non-negative numbers for both x and y"
    result = 1
    for _ in range(y):
        result = multiply(result, x)
    return result
