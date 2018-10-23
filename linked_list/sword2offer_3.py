# py3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列
    def printListFromTailToHead(self, listNode):
        _stack = []
        while listNode:
            _stack.insert(0, listNode.val)
            listNode = listNode.next
        return _stack


if __name__ == '__main__':
    pHead = ListNode(1)
    p = pHead
    for i in range(2, 11):
        node = ListNode(i)
        p.next = node
        p = node
    print(Solution().printListFromTailToHead(pHead))
