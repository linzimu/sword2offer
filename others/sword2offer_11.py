# # -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         count = 0
#         flag = 1
#         for _ in range(32):
#             if flag & n != 0:
#                 count += 1
#             flag <<= 1
#         return count

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n &= 0xffffffff
        while n:
            n &= n - 1
            count += 1
        return count
