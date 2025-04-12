from typing import Optional
class ListNode:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
class Solution:
    def deletefrommiddle(self,head: Optional[ListNode])->[ListNode]:
        if head and head.next is None:
            return 
        slow=head
        fast=head.next.next
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
    
head=ListNode(3,ListNode(4,ListNode(6,ListNode(8,ListNode(9)))))
sol=Solution()
result=sol.deletefrommiddle(head)
def printList(head):
    while head:
        print(f"{head.value}->",end="")
        head=head.next
    print(None)
printList(result)