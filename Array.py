def populateArray(x, y, t = 0):
    import random
    arr = [[0] * x for i in range(y)]
    #populate with numbers
    if t is 0:
        for v in range(x):
            for w in range(y):
                arr[w][v] = random.randint(0, x * y * 100)
    #populate with letters
    if t is 1:
        for v in range(x):
            for w in range(y):
                arr[w][v] = chr(random.randint(97, 122))  
    printArray(arr)
    return arr

#print array but limited up to ~9 digit based on spacing of tab
def printArray(arr):
    for y in range(len(arr)):
        string = ""
        for out in arr[y]:
            string += str(out) + "\t"
        print(string)
