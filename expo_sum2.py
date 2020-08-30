def multiply(a, b):
    return sum([a for _ in range(b)])

def expo_sum(x, y):
    result = 1
    for _ in range(y):
        result = multiply(result, x)
        return result
