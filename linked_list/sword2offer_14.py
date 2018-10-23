class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        p1 = head
        # 将第一个指针先先后移动k-1的位置
        for _ in range(k - 1):
            if p1.next:
                p1 = p1.next
            else:
                return None
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2


if __name__ == '__main__':
    pHead = ListNode(10)
    p = pHead
    for i in range(9, 0, -1):
        node = ListNode(i)
        p.next = node
        p = node
    print(Solution().FindKthToTail(pHead, 3).val)
