# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
# 返回删除后的链表的头节点。
#
# 注意：此题对比原题有改动
#
# 示例 1:
#
# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:
#
# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        a=head
        if a==None:
            return None
        if a.val==val:
            return a.next
        while a!=None and a.next!=None:
            b=a.next
            if b.val==val:
                a.next=b.next
                return head
            else:
                a=b
