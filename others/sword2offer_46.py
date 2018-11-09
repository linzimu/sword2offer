class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0 or m < 0:
            return -1
        array = list(range(n))
        out = 0
        while len(array) > 1:
            out = (out + (m - 1)) % len(array)
            del array[out]
        return array[0]
