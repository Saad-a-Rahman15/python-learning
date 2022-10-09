speech1 = input("Enter the first person's name:\n") #(Enter any name you want]
question1 = input('How many years is he/she?\n') #(You can pick a boy or a girl]
speech2 = input("Enter the second person's name:\n")
question2 = input("How many years old is he/she?\n")
speech3 = input("Enter the third person's name:\n")
question3 = input("How many years old is he/she\n")
if(question1 > (question2) and (question3)):
    print('The oldest person is ' + (speech1))
elif(question2 > (question1) and (question3)):
    print('The oldest person is ' + (speech2))
elif(question3 > (question1) and (question2)):
    print('The oldest person is ' + (speech3))
elif(question1 == (question3) and (question2)):
    print('They are all the same age.')
else:
    print('That cannot be done in the game.')