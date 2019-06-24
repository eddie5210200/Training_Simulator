class Node:
    def __init__(self, v):
        self.value = v
        self.child = None
    def addChild(self, child):
        self.child = Node(child)

def populateNode(numChilds):
    import random
    limit = numChilds*10
    n = Node(random.randint(0, limit))
    child = n
    for i in range(numChilds - 1):
        child.addChild(random.randint(0, limit))
        child = child.child
    #printNode(n)
    return n

def lenNode(head, num):
    if(head is None):
        print(num)
        return
    lenNode(head.child, num+1)
    
def printNode(head):
    if(head is None):
        return
    print(head.value)
    if(head.child is not None):
        print(" |")
    printNode(head.child)
    
