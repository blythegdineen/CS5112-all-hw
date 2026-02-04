'''
Problem 3b
'''

import random

class Node: 
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level
        self.level = level

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.sentinel = Node(None, self.max_level)
        self.root = None

    def insert(self, x: int) -> None:
        update = [None] * (self.max_level)
        current = self.sentinel

        for i in range(self.max_level -1, -1,-1):
            while current.next[i] and current.next[i].val < x:
                current = current.next[i]
            update[i] = current
    
        # check if node already exists (i.e. if predecessor next is the same, then dont bother)
        temp = update[0].next[0]
        if temp and temp.val == x:
            return None

        # create new node with random level
        coin = 1
        level = 0
        while coin ==1 and level < self.max_level:
            #add to each level as long as the coin flip is heads
            coin = random.randint(0,1)
            level +=1
        node_x = Node(x,level)

        # update pointers at all levels where this node exists (range up to new level)
        for i in range(level):
            node_x.next[i] = update[i].next[i]
            update[i].next[i] = node_x
        
        # ensure self.root always points to first element in list
        self.root = self.sentinel.next[0]

    def delete(self, x: int) -> None:
        update = [None] * (self.max_level)
        current = self.sentinel

        for i in range(self.max_level -1, -1,-1):
            while current.next[i] and current.next[i].val < x:
                current = current.next[i]
            update[i] = current
        current = current.next[0]
        if current and current.val == x:
            for i in range(self.max_level):
                if update[i].next[i] != current:
                    break
                update[i].next[i] = current.next[i]
        
        self.root = self.sentinel.next[0]
        return None


    def search(self, x: int) -> Node:
        current = self.sentinel
        for i in range(self.max_level -1, -1,-1):
            while current.next[i] and current.next[i].val < x:
                current = current.next[i]
            if current.next[i] and current.next[i].val == x:
                return current.next[i]
        return None