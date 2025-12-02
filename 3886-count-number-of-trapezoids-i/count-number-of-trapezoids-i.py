from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        inv2 = (MOD + 1) // 2  # modular inverse of 2 under MOD

        # count points on each horizontal line (same y)
        freq = defaultdict(int)
        for x, y in points:
            freq[y] += 1

        # for each horizontal line with k points, number of horizontal segments = C(k,2)
        ways = []
        for k in freq.values():
            if k >= 2:
                ways.append(k * (k - 1) // 2)

        if len(ways) < 2:
            return 0

        # We need sum_{i<j} ways[i]*ways[j]
        # Use identity: sum_{i<j} a_i*a_j = ( (sum a)^2 - sum(a^2) ) / 2
        s = sum(ways) % MOD
        s_sq = sum((w % MOD) * (w % MOD) for w in ways) % MOD

        ans = ( (s * s - s_sq) % MOD ) * inv2 % MOD
        return ans
