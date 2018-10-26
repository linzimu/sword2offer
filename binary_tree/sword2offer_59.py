# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        ans = []
        if not pRoot:
            return ans
        cur_layer_nodes = [pRoot]
        shift = False
        while cur_layer_nodes:
            cur_layer_values = []
            next_layer_nodes = []
            # 广度优先遍历
            while cur_layer_nodes:
                node = cur_layer_nodes.pop(0)
                cur_layer_values.append(node.val)
                if node.left:
                    next_layer_nodes.append(node.left)
                if node.right:
                    next_layer_nodes.append(node.right)
            cur_layer_nodes = next_layer_nodes
            if shift:
                ans.append(cur_layer_values[::-1])
            else:
                ans.append(cur_layer_values)
            shift = not shift
        return ans
