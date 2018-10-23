class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        p_reverse = None
        while pHead:
            p_next = pHead.next
            pHead.next = p_reverse
            p_reverse = pHead
            pHead = p_next
        return p_reverse


if __name__ == '__main__':
    pHead = ListNode(1)
    p = pHead
    for i in range(2, 11):
        node = ListNode(i)
        p.next = node
        p = node
    p = pHead
    while p is not None:
        print(p.val, end='\t')
        p = p.next
    print()
    p = Solution().ReverseList(pHead)
    while p is not None:
        print(p.val, end='\t')
        p = p.next
