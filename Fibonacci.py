def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    count = 0
    while count < n:
        fib_series.append(a)
        a, b = b, a + b
        count += 1
    return fib_series


n_terms = int(input("Enter a number : "))
result = fibonacci(n_terms)
print(f"Fibonacci series with {n_terms} terms: {result}")