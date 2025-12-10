class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)
        if n == 0:
            return 0

        root = complexity[0]
        # if any other complexity is <= root, impossible
        for i in range(1, n):
            if complexity[i] <= root:
                return 0

        # else answer is (n-1)! % MOD
        fact = 1
        for k in range(1, n):
            fact = (fact * k) % MOD
        return fact
