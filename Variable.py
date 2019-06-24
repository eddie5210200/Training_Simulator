def populateVar(length, t = 0):
    import random
    var = ""
    #default string
    if t is 0:
        for i in range(length):
            var +=  chr(random.randint(97,122))
    return var
