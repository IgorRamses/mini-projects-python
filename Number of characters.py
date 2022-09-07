user = input('Enter your username: ')

qtt_user_characters = len(user)

if qtt_user_characters < 6 or qtt_user_characters > 10:
    print('You need to enter between 6 and 10 characters.')
    user = input('Enter your username: ')
    qtt_user_characters = len(user)

password = input(' Enter your password: ')

qtt_password_characters = len(password)

if qtt_password_characters < 6 or qtt_password_characters > 10:
    print('You need to enter between 6 and 10 characters.')
    user = input('Enter your password: ')
    qtt_password_characters = len(password)
print('User registered successfully. ')