import time

# 1. Normal Recursive Fibonacci (Exponential Time)


def fib_normal(num):
    if num <= 1:
        return num
    return fib_normal(num - 1) + fib_normal(num - 2)

# using Fibanaci normal recur   sive for 35


def fib_recursive(num):
    if num <= 1:
        return num
    return fib_recursive(num - 1) + fib_recursive(num - 2)


start_time = time.time()
ans = fib_recursive(35)
end_time = time.time()
print('Recursive Fibonacci result:', ans)
print('Recursive Fibonacci Time taken:', end_time - start_time, 'seconds\n')

# 2. Memoization (Top-Down DP)


def fib_memo(num, memo={}):
    if num in memo:
        return memo[num]
    if num <= 1:
        return num
    memo[num] = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)
    return memo[num]


start_time = time.time()
ans = fib_memo(800)
end_time = time.time()
print("Memoized Fibonacci result:", ans)
print("Memoized Fibonacci Time taken:", end_time - start_time, 'seconds\n')

# 3. Tabulation (Bottom-Up DP)


def fib_tabulation(num):
    if num <= 1:
        return num
    prev = 1
    sec_prev = 0
    for _ in range(2, num + 1):
        res = prev + sec_prev
        sec_prev = prev
        prev = res
    return prev


start_time = time.time()
ans = fib_tabulation(800)
end_time = time.time()
print('Tabulated Fibonacci result:', ans)
print('Tabulated Fibonacci Time taken:', end_time - start_time, 'seconds')
