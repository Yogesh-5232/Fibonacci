class Solution:
    def nthFibonacci(self, n : int) -> int:
        a = 1
        b = 1
        mod = 10**9+7
        for i in range(n-2):
            c = (a+b)
            if c>=mod:
                c-=mod
            a = b
            b = c
        return b
