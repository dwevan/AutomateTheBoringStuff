import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('You typed ' + response + '. \nGoodbye...')
        sys.exit()
    else:
        print('try again...')