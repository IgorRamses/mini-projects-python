name = 'Ramsés'
age = 19
height = 1.75
weight = 69
current_year  = 2022
imc = weight/ height**2

print('year of birth:', current_year - age)

print(f'{name}, has {age} years of age and your IMC is {imc:.2f}')

print(f'{name} has {age} years of age, was born in {current_year -age} in the city of Crato-CE')

print(f'currently weighs {weight} kgs and measure {height} of height, with a IMC of {imc:.2f}')

print(f'today in the year {current_year } is studying Systems Analysis and Development at IFCE - Campus Canindé')


user = input('Enter your username: ')

qtt_user_characters = len(user)

while (qtt_user_characters < 6 or qtt_user_characters> 10):
    print('You need to enter between 6 and 10 characters. ')
    user = input('Enter your username:: ')
    qtt_user_characters = len(user)


password = input(' Enter your password: ')

qtt_characters_password = len(password)

while (qtt_characters_password < 6 or qtt_characters_password > 10):
    print('You need to enter between 6 and 10 characters. ')
    password = input('Enter your password:: ')
    qtt_characters_password = len(password)

print('User registered successfully. ')