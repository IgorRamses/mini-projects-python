import getpass
import time

while True:

    print('Enter your first name: ')
    first_name = input()
    print('Enter your last name: ')
    last_name = input()
    print('Day of your birth: ')
    day_birth = input()
    if not day_birth.isdigit():
        print('This is not a valid number')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    else:
        pass

    day_birth = int(day_birth)
    if day_birth >31:
        print('Invalid day number')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break


    print('Month of your birth: ')
    month_birth = input()
    if not month_birth.isdigit():
        print('This is not a valid number')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    else:
        pass

    month_birth = int(month_birth)
    if month_birth >12:
        print('Non-existent month number')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break

    print('Year of your birth: ')
    birth_year = input()
    if not birth_year.isdigit():
        print('This is not a valid number')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    else:
        pass

    birth_year = int(birth_year)
    if birth_year >2022:
        print('Non-existent year ')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    elif birth_year <1922:
        print('Invalid year to register.')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    else:
        pass

    print('Enter the current year: ')
    current_year = input()
    if not current_year.isdigit():
        print('This is not a valid number')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    else:
        pass

    current_year = int(current_year)
    if current_year >2022:
        print('Invalid current year')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    elif current_year < 2022:
        print('Invalid current year')
        time.sleep( 1 )
        print('Exiting the registration system...')
        break
    else:
        pass

    if (current_year - birth_year) <18:
        print('It was not possible to proceed with your registration.')
        quit()

    else:
        print('Lets proceed with your registration. ')

        print('Enter your username: ')
        user = input()
        qtd_user_characters = len(user)
        while (qtd_user_characters < 6 or qtd_user_characters> 10):
            print('You need to enter between 6 and 10 characters. ')
            user = input('Enter your username: ')
            qtd_user_characters = len(user)
        print(' Type your password: ')
        password = getpass.getpass (' ')
        qtd_characters_password = len(password)
        while (qtd_characters_password < 6 or qtd_characters_password > 10):
            print('You need to enter between 6 and 10 characters. ')
            password = getpass.getpass ('Enter your password: ')
            qtd_characters_password = len(password)
        print('User registered successfully')

        if 'User registered successfully': 
            print(f'USER: {user}')
        
    correct_user = input('check ? [y]es or [n]o: ')

    if correct_user == 'y':
        print('NEXT STEP: ')
        
    elif correct_user == 'n':
        print('Enter your username: ')
        correct_user_2 = input()
        qtd_user_characters = len(correct_user_2)
        while (qtd_user_characters < 6 or qtd_user_characters> 10):
            print('You need to enter between 6 and 10 characters. ')
            correct_user_2 = input('Enter your username: ')
            qtd_user_characters = len(correct_user_2)

    print(f'password: {password}')
    password_correct = input('check ? [y]es ou [n]o: ')

    if correct_user == 'y' and password_correct == 'n':
        print(' Type your password: ')
        password_correct = getpass.getpass ()
        qtd_characters_password = len(password_correct)
        while (qtd_characters_password < 6 or qtd_characters_password > 10):
            print('You need to enter between 6 and 10 characters. ')
            password_correct = getpass.getpass ('Enter your password: ')
            qtd_characters_password = len(password_correct)
        print(f'Be welcome, {user}')

    elif correct_user == 'n' and password_correct == 'n':
        

        print(' Type your password: ')
        password_correct = getpass.getpass ()
        qtd_characters_password = len(password_correct)
        while (qtd_characters_password < 6 or qtd_characters_password > 10):
            print('You need to enter between 6 and 10 characters. ')
            password_correct = getpass.getpass('Enter your password: ')
            qtd_characters_password = len(password_correct)
        print(f'Be welcome, {correct_user_2}')

    elif password_correct == 'y':
        print(f'Be welcome, {user}')

    elif password_correct == 'n':
        print(' Type your password: ')
        password_correct = getpass.getpass()
        qtd_characters_password = len(password_correct)
        while (qtd_characters_password < 6 or qtd_characters_password > 10):
            print('You need to enter between 6 and 10 characters. ')
            password_correct = getpass.getpass('Enter your password: ')
            qtd_characters_password = len(password_correct)
        print(f'Be welcome, {user}')
        
    time.sleep( 1 )
    print('User registered successfully.')
    time.sleep( 1 )
    print()
    print('New user:')
    time.sleep( 1 )
    print()