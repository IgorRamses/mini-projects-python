# Write a program that asks the user for the time and, based on the time
# described, display the appropriate greeting.

#Ex. Good Morning 0-11, Good afternoon 12-17, Goodnight 18-23.

hours = int(input('Enter what time it is: '))
minutes = int(input('Enter what minutes is: '))

if  hours <=11:
    print('Good Morning')

elif hours <=17 and hours >=12:
    print('Good afternoon')

elif hours <=23 and hours >=18:
    print('Goodnight')

print(f'{hours}:{minutes}')