# # -*- coding:utf-8 -*-
# class Solution:
#     def ReverseSentence(self, s):
#         # write code here
#         if not s:
#             return s
#         return ' '.join(reversed(s.split(' ')))


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        start, end = 0, 0
        while start < len(s):
            if s[start] == ' ':
                start += 1
                end += 1
            elif end == len(s) or s[end] == ' ':
                self.reverse(s, start, end - 1)
                end += 1
                start = end
            else:
                end += 1
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
