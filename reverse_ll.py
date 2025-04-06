from typing import Optional
class ListNode:
    def __init__(self,val,next=None):
       self.val=val
       self.next=next
class Solution:
    def reverse_list(self,head:Optional[ListNode])->Optional[ListNode]:
        temp=head
        front=temp
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
head=ListNode(3,ListNode(4,ListNode(5)))
sol=Solution()
answer=sol.reverse_list(head)
while answer:
    print(f"{answer.val}",end="->")
    answer=answer.next
print("none")