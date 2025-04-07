from typing import Optional
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution:
    def detectCycle(self,head: Optional[ListNode])->Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
head = ListNode(2, ListNode(4, ListNode(6)))

sol=Solution()
answer=sol.detectCycle(head)
if answer:
    print(f"Cycle starts at node with value: {answer.value}")
else:
    print("No cycle found")
