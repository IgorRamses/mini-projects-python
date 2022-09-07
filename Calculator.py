while True:
    print()
    num_1 = input('Enter a number: ')
    if not num_1.isdigit():
        print('Enter a valid number')
        break
    
    operator = input('Type an operator: ')
    if operator !='+' and operator !='-' and operator !='*' and operator !='/' and operator !='**' and operator !='%':
        print('invalid operator, exiting calculator ...')
        break

    num_2 = input('Enter another number: ')
    if not num_1.isdigit():
        print('Enter a valid number')
        break

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(f'Result : {num_1+num_2}')

    elif operator == '-':
        print(f'Result : {num_1-num_2}')

    elif operator == '*':
        print(f'Result : {num_1*num_2}')

    elif operator == '/':
        print(f'Result : {num_1/num_2}')

    elif operator == '**':
        print(f'Result : {num_1**num_2}')

    elif operator == '%':
        print(f'Result : {num_1%num_2}')

    else:
        print('invalid operator')

    exit = input('Do you want to leave ? [y]es ou [n]o ')

    if exit == 'y':
        break
    
    else:
        pass
