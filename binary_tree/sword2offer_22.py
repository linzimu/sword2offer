# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        ans = []
        if not root:
            return ans
        _queue = [root]
        while _queue:
            item = _queue.pop(0)
            ans.append(item.val)
            if item.left is not None:
                _queue.append(item.left)
            if item.right is not None:
                _queue.append(item.right)
        return ans
