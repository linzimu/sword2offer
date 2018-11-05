# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
        self.tmp = []

    def push(self, node):
        # write code here
        if not self.tmp:
            self.tmp.append(node)
        if self.tmp[-1] > node:
            self.tmp.append(node)
        self.data.append(node)

    def pop(self):
        # write code here
        if self.data[-1] == self.tmp[-1]:
            self.tmp.pop()
        self.data.pop()

    def top(self):
        # write code here
        return self.data[-1]

    def min(self):
        # write code here
        return self.tmp[-1]
