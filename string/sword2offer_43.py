# # -*- coding:utf-8 -*-
# class Solution:
#     def LeftRotateString(self, s, n):
#         # write code here
#         len_s = len(s)
#         if n <= 0 or len_s == 0:
#             return s
#         n = n % len_s
#         return s[n:] + s[:n]


# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        len_s = len(s)
        if n <= 0 or len_s == 0:
            return s
        n = n % len_s
        s = list(s)
        self.reverse(s, 0, n - 1)
        self.reverse(s, n, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
