from os import link
from tokenize import String


class Node:

    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None


    def AddNode(self, node: Node):
        if self.head is None:
            self.head = node
        
        self.head.next = node
        self.head = node
    
    
    def PrintNodes(self, head: Node):
        if head is None:
            return
        
        while head is not None:
            print(head.value)
            head = head.next

    
    def Reverse(self, head: Node):
        if head is None:
            return head

        dummy: Node = None
        while head is not None:
            next = head.next
            head.next = dummy
            dummy = head
            head = next
        
        return dummy

    def AddAfter(self, head: Node, valAfter: String, valToAddAfter: String):
        if head is None:
            return head

        nextNode: Node = None
        while head != None:

            if head.value == valAfter:
                nextNode = head.next
                head.next = Node(valToAddAfter)
                head.next.next = nextNode
                return

            head = head.next
        
    def AddBefore(self, head: Node, valBefore: String, valToAddBefore: String) -> Node:
        if head is None:
            return head

        prevNode: Node = None
        while head != None:

            if head.value == valBefore:
                prevNode = head
                head = Node(valToAddBefore)
                head.next = prevNode
                return head

            head = head.next

        return head


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

linkedList = LinkedList()

linkedList.AddNode(a)
linkedList.AddNode(b)
linkedList.AddNode(c)
linkedList.AddNode(d)

res = linkedList.AddBefore( head= a, valBefore= "a", valToAddBefore= "e")

linkedList.PrintNodes(res)