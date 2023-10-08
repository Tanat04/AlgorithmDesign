def countNodes(head):
    count = 1
    current = head
    while current.next != None:
        count += 1
        current = current.next
    return count

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

NodeA = Node(4)
NodeB = Node(6)
NodeC = Node(2)

NodeA.next = NodeB
NodeB.next = NodeC

print(countNodes(NodeA))