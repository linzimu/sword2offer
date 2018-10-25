# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '$'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        _list = s.split(',')
        return self.deserializeTree(_list)

    def deserializeTree(self, _list):
        # write code here
        if not _list:
            return None
        val = _list.pop(0)
        root = None
        if val != '$':
            # 现需遍历
            root = TreeNode(int(val))
            root.left = self.deserializeTree(_list)
            root.right = self.deserializeTree(_list)
        return root
