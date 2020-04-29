def fibonacci(n):
    # base case
    fib_base = [0, 1]

    while len(fib_base) < n + 1:
        fib_base.append(0)
    if n <= 1:
        return n
    else:
        if fib_base[n - 1] == 0:
            fib_base[n - 1] = fibonacci(n - 1)
        if fib_base[n - 2] == 0:
            fib_base[n - 2] = fibonacci(n - 2)
    fib_base[n] = fib_base[n - 1] + fib_base[n - 2]
    return fib_base[n]
