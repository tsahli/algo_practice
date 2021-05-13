class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(i)
                node = node.next

    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev # This step reverses the pointer between Curr & Next --- None <= Curr Next => Node => Node => None
            prev = curr
            curr = next
        self.head = prev

    def insert_at_beginning(self, new_node_data):
        new_node = Node(data=new_node_data)
        old_head = self.head
        self.head = new_node
        new_node.next = old_head

    def __str__(self):
        nodes = []
        n = self.head
        while n is not None:
            nodes.append(n.data)
            n = n.next
        return " -> ".join(nodes)

if __name__ == '__main__':
    ll = LinkedList(['a','b','c','d','e','f','g'])
    ll.reverse()
    print(ll)
