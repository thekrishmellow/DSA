class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.rec(n,{})
    def rec (self,n, memo):
        if n <=1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.rec(n-1, memo) + self.rec(n-2,memo)
        return memo[n]
        