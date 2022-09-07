print('Type your name: ')
name = input()
print('Enter your age: ')
age = input ()
print('Enter your weight: ')
weight = input ()
print('Enter your height: ')
height = input()

weight = int(weight) 
height = float(height)

imc = weight/ height**2


print(f'{name} has {age} and weighs {weight} kgs, your height is {height}, your current IMC is {imc: .2f}')