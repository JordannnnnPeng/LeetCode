# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
#
# 0 <= 链表长度 <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_a=l1
        l2_a=l2

        if l1_a==None and l2_a==None:
            return None
        if l1_a==None and l2_a!=None:
            return l2_a
        if l2_a==None and l1_a!=None:
            return l1_a

        l1_b = l1_a.next
        l2_b = l2_a.next

        compare=0

        if l1_a.val >= l2_a.val:
            l2_a.next = l1_a
            head=l2_a
            compare=head
            l2_a = l2_b
        else:
            l1_a.next = l2_a
            head=l1_a
            compare=head
            l1_a = l1_b
        while l1_a!=None and l2_a!=None:
            l1_b=l1_a.next
            l2_b=l2_a.next
            if l1_a.val>=l2_a.val:
                compare.next=l2_a
                l2_a=l2_b
                compare=compare.next
            else:
                compare.next=l1_a
                l1_a=l1_b
                compare=compare.next
        if l1_a==None and l2_a!=None:
            compare.next=l2_a
        elif l2_a==None and l1_a!=None:
            compare.next=l1_a
        return head


