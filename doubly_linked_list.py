class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            prev = None
            for i in nodes:
                node.next = Node(data=i)
                node.previous = prev
                prev = node
                node = node.next
            node.previous = prev

    def __str__(self):
        n = self.head
        while n is not None:
            if n.previous is not None:
                print("Current:", str(n.data), "Previous:", str(n.previous.data))
            else:
                print("Current:", str(n.data), "Previous: None")
            n = n.next

if __name__ == '__main__':
    dll = DoublyLinkedList(['a','b','c','d','e','f','g'])
    print(dll)
        

        