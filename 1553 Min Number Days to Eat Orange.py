from functools import lru_cache


class Solution:
    # Bottom Up
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        moves = [0, 1, 2]
        for i in range(3, n + 1):
            moves.append(1 + min(moves[i - 1], i % 2 + moves[i // 2], i % 3 + moves[i // 3]))
        return moves[n]

    # Top Down
    @lru_cache(None)
    def minDays2(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
        