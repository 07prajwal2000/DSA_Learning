class Node:

    def __init__(self, val:str) -> None:
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

        print(head.value)
        self.PrintNodes(head.next)
    
    def Reverse(self, head: Node):
        if head is None:
            return head

        prev: Node = None
        cur: Node = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

    def AddAfter(self, head: Node, valAfter: str, valToAddAfter: str):
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
        
    def AddBefore(self, head: Node, valBefore: str, valToAddBefore: str) -> Node:
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

    def RemoveAt(self, head: Node, valueAt: str):
        if head is None:
            return head
        if head.next is None:
            return head.next
        
        prev: Node = head
        while head != None:
            if head.value == valueAt:
                head.value =  head.next.value
                head.next = head.next.next
                return
            head = head.next



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
d = Node("d")

linkedList = LinkedList()

linkedList.AddNode(a)
linkedList.AddNode(b)
linkedList.AddNode(c)
linkedList.AddNode(d)

# e = linkedList.AddBefore(a, "a", 'e')
# rev = linkedList.Reverse(a)
linkedList.RemoveAt(a, 'd')
linkedList.PrintNodes(a)