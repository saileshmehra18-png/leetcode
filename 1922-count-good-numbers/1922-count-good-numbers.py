class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def helper(x,n):
            if n == 0:
                return 1
            half = helper(x,n//2)
            if n%2 == 0:
                return (half*half)  %  MOD
            return (half*half*x)   %  MOD
        return helper(5,(n+1)//2)*helper(4,n//2) % MOD