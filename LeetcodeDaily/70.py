class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1. Using Memoization Fibonacci
        2. Tabulation Fibonacci to optimize DP recursion
        """
        def fib_memo(n, memo):
            if n <= 1:
                return 1  # base case: 1 way to reach step 0 or 1
            if n in memo:
                return memo[n]
            memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
            return memo[n]

        return fib_memo(n, memo={})
