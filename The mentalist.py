from random import randint
import time

print('The mentalist')
time.sleep( 1 )
print('Do you want to start the game ? [y]es ou [n]o')
start = input()

if start == 'y':
    x = randint(1, 50)

    print('Choose a number from 1 to 50')
    while True:
        
        choice = input()
        choice = int(choice)

        if choice <x:
            time.sleep(1)
            print('Enter a larger number')
           
        elif choice >x:
            time.sleep(1)
            print('Enter a smaller number')
        
        elif choice == x:
            time.sleep(1)
            print('Congratulations, you got it right')
            option = input('Do you want to play again ? [y]es ou [n]o ')
            time.sleep(1)
            if option == 'y':
                x = randint(1, 50)

            elif option == 'n':
                print(' leaving the game ... ')
                break
                

            print('Choose a number from 1 to 50')

elif start == 'n':
    print(' leaving the game ... ')
    pass      

else:
    print('Invalid option, exiting the game ...')
    pass