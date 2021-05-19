class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while (current!=None):
              next=current.next
              current.next=prev
              prev=current
              current=next              
        self.head=prev
    def push(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
LList=LinkedList()
LList.push(20)
LList.push(30)
LList.push(40)
LList.push(50)
LList.printlist()
LList.reverse()
print("Reversed List:\n")
LList.printlist()
