from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        temp=head
        mid=count//2
        for i in range(mid):
            temp=temp.next
        return temp
head=ListNode(1,ListNode(3,ListNode(5)))
sol=Solution()
answer=sol.middleNode(head)
print(answer.val)