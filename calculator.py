# simple calculator

# add two number
def add(a, b):
    return a + b


# subtract two number
def subtract(a, b):
    return a - b


# multiply two number
def multiply(a, b):
    return a * b


# divide two number
def divide(a, b):
    return a / b

def inputs():
    num_1 = float(input('Enter first number: '))
    num_2 = float(input('Enter second number: '))
    return num_1, num_2


print('select operation')
print('1.addition')
print('2.subtract')
print('3.multiply')
print('4.divide')

while True:
    choice = input('Enter the choice (1/2/3/4): ')

    if choice in ('1', '2', '3', '4'):

        num_1, num_2 = inputs()


        if choice == '1':
            print(num_1, "+", num_2, "=", add(num_1, num_2))

        elif choice == '2':
            print(num_1, "-", num_2, "=", subtract(num_1, num_2))

        elif choice == '3':
            print(num_1, "*", num_2, "=", multiply(num_1, num_2))

        elif choice == '4':
             if num_2 == 0 :
                 print("divide by zero not possible")
             else:
                print(num_1, '/', num_2, '=', divide(num_1, num_2))

        next_calculation = input('Let do next calculation (yes/no): ')
        if next_calculation == 'no':
            break
    else:
        print('invalid input')
