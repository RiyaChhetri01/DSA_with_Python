class Node:
    def __init__(self,value):
        self.next=None
        self.value=value
class LL:
    def Linkedlist(self,arr):
        n=len(arr)
        new_head=Node(arr[0])
        
        current_node=new_head
        for i in range(1,n):
            new_node=Node(arr[i])
            current_node.next=new_node
            current_node=new_node
        return new_head
arr=[2,4,5,6]
sol=LL()
answer=sol.Linkedlist(arr)
while answer:
        print(f"{answer.value}",end="->")
        answer=answer.next
print(answer)

