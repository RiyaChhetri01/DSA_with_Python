class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Solution:
    def loopInll(self,head):
        slow=head
        fast=head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                count=1
                while slow!=fast:
                    count+=1
                    slow=slow.next
                return count


        return None
loop_node=Node(6)
head=Node(2,Node(3,Node(5,Node(2,loop_node))))
loop_node.next=Node(3,loop_node)
sol=Solution()
result=sol.loopInll(head)
print(result)




        