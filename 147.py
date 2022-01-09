# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 双指针，一个指向已排序(升序)的链表尾，一个指向未排序的链表头
        def insert(head:ListNode,ins):
            i=head
            j=head.next
            while j:
                if j.val<ins:
                    i=j
                    j=j.next
                else:
                    tmp=ListNode(ins,None)
                    i.next=tmp
                    tmp.next=j
                    return True
            i.next=ListNode(ins,None)
            return False

        dummyhead=ListNode(0,None)
        dummyhead.next=head
        head=dummyhead
        pre=head
        cur=head.next
        while cur:
            pre.next=None
            sorted_node=head#在sorted的链表中插入ins
            is_insert=insert(sorted_node,cur.val)
            if not is_insert:
                pre=pre.next
            cur=cur.next
            pre.next=cur
        return head

head=ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
s=Solution().insertionSortList(head)
pass