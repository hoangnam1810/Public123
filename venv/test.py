def digitize(n):
    return map(int, str(n)[::-1])


print(list(digitize(12345)))