def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Number must be positive and integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(-5))
print(fibonacci(1.5))