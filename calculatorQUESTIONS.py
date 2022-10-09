print('Start the questions.' )

operations = input('+   -   *   /\n')
number1 = input('Enter the first number.\n')
number2 = input('Enter the second number.\n')
if(operations == '+'):
    print('The answer is:')
    print((int(number1) + int(number2)))
elif(operations == '-'):
    print('The answer is:')
    print((int(number1) - int(number2)))
elif(operations == '*'):
    print('The answer is:')
    print((int(number1) * int(number2)))
elif(operations == '/'):
    if(number2 == '0'):
        print('That is not allowed.')
    else:
        print('The answer is:')
        print((int(number1) / int(number2)))
else:
    print("Sorry, you can't do that!")