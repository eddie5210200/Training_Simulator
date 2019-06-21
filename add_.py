def create_array(x, y):
    import random
    arr = []
    for v in range(x):
        list_to_add = []
        for w in range(y):
            list_to_add.extend(random.randInt((1+x) * (1+y)))
        arr.append(list_to_add)
    return arr

def createNode(number):
    import Node
    return populateNode(number)

def createTree(level, children, skew = 0):
    
def create_variable(value):
    return value
    
