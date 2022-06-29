def fib(n):
    global fib_count
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        fib_count += 1
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global fibonacci_count
    if n == 2 or n == 1:
        f[n] = 1
    for i in range(3, n):
        fibonacci_count += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input())
fib_count = 0
fibonacci_count = 0
f = [0 for _ in range(n+1)]

fib(n)
fibonacci(n)
print(fib_count + 1, end=" ")
print(fibonacci_count + 1)