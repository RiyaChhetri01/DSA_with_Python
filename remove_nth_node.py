from typing import Optional
class ListNode:
    def __init__(self,value,next=None):
       self.value=value
       self.next=next
class Solution:
    def removeNthNode(self,head:Optional[ListNode],n:int)->[ListNode]:
        slow=head
        fast=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            new_head=head.next
            head.next=None
            return new_head
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next

        return head
head=ListNode(3,ListNode(5,ListNode(4,ListNode(8))))
n=1
sol=Solution()
result=sol.removeNthNode(head,n)
def printll(head):
    while head:
        print(f"{head.value}->",end="")
        head=head.next
    print(None)
printll(head)



