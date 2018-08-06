#Simples calculadora, código retirado do app SoloLearn

while True:
    print('Options:')
    print("Enter 'add' to add two numbers")
    print("Enter 'sub' to subtract two numbers")
    print("Enter 'mtl' to multiply two numbers")
    print("Enter 'div' to divide two numbers")
    print("Enter 'quit' to quit the program")

    option = input(': ')

    if option == 'quit':
        break
    
    elif option == 'add':
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a other number: '))
        resp = str(num1 + num2)
        print('The answer is ' + resp)

    elif option == 'sub':
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a other number: '))
        resp = str(num1 - num2)
        print('The answer is ' + resp)

    elif option == 'mtl':
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a other number: '))
        resp = str(num1 * num2)
        print('The answer is ' + resp)

    elif option == 'div':
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a other number: '))
        resp = str(num1 / num2)
        print('The answer is ' + resp)
    else:
        print('Unknown input!')