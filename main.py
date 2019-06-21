def run():
    # import ___ as ___
    import command_list
    while True:
        data = input('input: ')
        if data ==  'quit':
            quit
        else:
            execute(data)
    
if __name__ == "__main__":
    import sys
    run()
