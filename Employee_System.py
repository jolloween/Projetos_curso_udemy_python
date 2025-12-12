# 1. Employee System

# Create a program that:

# Has a function to register employees (name, position, salary).

# Stores the employees in a dictionary where the key is the name.

# Uses a loop to register multiple employees.

# At the end, displays all employees and the total amount owed in arrears.


employee = {}
while True:
    

    name = input('Nome do funcionário: ')
    position = input('position: ')
    salary = float(input('salary: '))

    dado = {'position': position, 'salary': salary}

    employee[name] = dado

    while True:
        resp = input('Do you want to continue ["Y" for yes and "N" for no]? ').upper()
        
        if resp not in ('Y', 'N'):
            print('Just type "Y" for yes and "N" for no.')
            continue
        else:
            break
    if resp == 'N':
        break

for c, v in employee.items():
    print("=-" *20)
    print(f'name: {c}')
    print(f'position: {v['position']}')
    print(f'salary: ${v['salary']:.2f}')

total_saários = sum(v['salary'] for v in employee.values())

total_salary = 0
for wage in employee.values():
    wage = wage['salary']
    total_salary += wage
# print(total_saários)
print("=-" *20)
print(f'Total salaries: {total_salary}')
print("=-" *20)