def mul(n, m):
    result = 0
    for i in range(abs(n)):
        result += m
    return result


print(mul(3,-6))