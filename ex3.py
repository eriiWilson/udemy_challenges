# Make a program that evaluates two values and shows whether value X is greater than value Y

first_value = float(input('Enter a value: '))
second_value = float(input('Enter another value: '))

if first_value > second_value: 
    print(f'The first value {first_value} is greater than the second value {second_value}')
elif second_value > first_value:
    print(f'The second value {second_value} is greater than the first value {first_value}')
else:
    print('Both values are equal.')
