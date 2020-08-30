def expo_sum(x,y):
    if x < 0 or y < 0:
        return "Please enter non-negative numbers for both x and y"
    elif x == 0:
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x
    else:
        result = 0
        i = 0
        n_sums = expo_sum(x, y-1)

        while i < n_sums:
            result += x
            i += 1
        return result

print(expo_sum(2,10))
