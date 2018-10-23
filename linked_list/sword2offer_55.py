class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        _list = []
        p = pHead
        while p is not None:
            if p in _list:
                return p
            else:
                _list.append(p)
            p = p.next
