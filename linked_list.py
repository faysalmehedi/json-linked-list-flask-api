class SingleNode:
    def __init__(self, key):
        self.key = key
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
            
    def push_back(self, key):
        node = SingleNode(key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
