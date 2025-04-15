from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    
    def middleofll(self,head:Optional[ListNode])->Optional[ListNode]:
        slow=head
        fast=head
        while fast.next and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeLL(self,L1:Optional[ListNode],L2:Optional[ListNode]):
        demo=ListNode()
        temp=demo
        while L1 and L2:
            if L1.val<L2.val:
                temp.next=L1
                L1=L1.next
            else:
                temp.next=L2
                L2=L2.next
            temp=temp.next
        temp.next =L1 or L2
        return demo.next
    def sortll(self,head:Optional[ListNode])->Optional[ListNode]:

        if not head or not head.next:
            return head
        mid=self.middleofll(head)
        left=head
        right=mid.next
        mid.next=None
        left =self.sortll(left)
        right=self.sortll(right)
        return self.mergeLL(left,right)
head=ListNode(3,ListNode(1,(ListNode(6,ListNode(4,ListNode(2))))))
sol=Solution()
result=sol.sortll(head)
def printlist(head: Optional[ListNode]):
    while head:
        print(f"{head.val}->", end="")
        head = head.next
    print('None')

printlist(result)


        