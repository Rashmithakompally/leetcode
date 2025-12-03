from math import gcd
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points):
        # Using defaultdict to simulate unordered_map with default 0
        lookup_slope = defaultdict(int)
        lookup_line = defaultdict(int)
        lookup_slope_length = defaultdict(int)
        lookup_line_length = defaultdict(int)

        result = 0
        same = 0

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                a = dx // g
                b = dy // g

                # Normalize direction to match C++
                if a < 0 or (a == 0 and b < 0):
                    a = -a
                    b = -b

                # Unique line identifier: ax + by + c = 0 → c = b*x1 - a*y1
                c = b * x1 - a * y1

                # slope count minus same-line count
                result += lookup_slope[(a, b)]
                lookup_slope[(a, b)] += 1

                result -= lookup_line[(a, b, c)]
                lookup_line[(a, b, c)] += 1

                # distance squared
                length = dx * dx + dy * dy

                # similar handling for same-length segments
                same += lookup_slope_length[(a, b, length)]
                lookup_slope_length[(a, b, length)] += 1

                same -= lookup_line_length[(a, b, c, length)]
                lookup_line_length[(a, b, c, length)] += 1

        return result - same // 2