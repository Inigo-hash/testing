first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
operator = input("Enter your operation(+, -, *, /): ")
calculation = f'{first_number} {operator} {second_number}'
output = int(eval(calculation))

print(f'The answer is {output}')