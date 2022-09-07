from random import randint

# 1 = STONE
# 2 = PAPER
# 3 = SCISSOR

while True:

    x = randint(1,3)
    x = str(x)

    print('STONE[1], PAPER[2] OU SCISSOR[3] ?')
    choice = input()

    if choice != '1' and choice !='2' and choice!= '3':
        print('Invalid option, exiting game...')
        break

    elif choice == '1' and x == '3':
        print('You won')

    elif choice == '2' and x == '1':
        print('You won')

    elif choice == '3' and x == '2':
        print('You won')
        
    elif choice == '1' and x == '2':
        print('You lost')

    elif choice == '2' and x == '3':
        print('You lost')

    elif choice == '3' and x == '1':
        print('You lost')

    else:
        print('A TIE')

    print('Do you want to leave? [y]es ou [n]o ')
    go_out = input('ANSWER: ')

    if go_out == 'y':
        break

    elif go_out == 'n':
        continue
    
    else:
        print('Invalid option, exiting game...')
        break