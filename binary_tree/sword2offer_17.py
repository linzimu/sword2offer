# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        tmp1 = self.HasSubtree(pRoot1.left, pRoot2)
        tmp2 = self.HasSubtree(pRoot1.right, pRoot2)
        tmp3 = self.is_subtree(pRoot1, pRoot2)
        return tmp1 or tmp2 or tmp3

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)
