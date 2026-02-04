'''
Problem 3a
'''

class Node:
    def __init__(self, val:int, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, x):
        node_x = Node(x,None)
        
        if not self.root or self.root.val > x:
            node_x.next = self.root
            self.root = node_x
            return None
        
        current = self.root
        while current.next and current.next.val < x:
            current = current.next
        
        node_x.next = current.next
        current.next = node_x

        return None

    def search(self, x):
        current = self.root
        while current:
            if current.val == x:
                return current
            current = current.next
        return None

    def delete(self, x):
        if not self.root:
            return None

        if self.root.val == x:
            self.root = self.root.next
            return None
        
        current = self.root
        while current.next:
            if current.next.val == x:
                current.next = current.next.next
                return
            current = current.next
        return None
