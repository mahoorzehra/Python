#Calulator with basic aritmetic operations              Date: 16/09/26
n1 = float(input("Enter the 1st number:"))
op = input("Operator:")
n2 = float(input("Enter the 2nd number:"))

if op =='+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
elif op == '%':
    print(n1%n2)
else:
    print('invalid operator')

#even vs odd
x = int(input('Enter the number:'))
if x%2 == 0:
    print('Even')
else:
    print('odd')

#Login
username = input('Enter the username:')
password = input('Enter the password:')

if username == 'chocolate':
    if password =='abc1':
        print("Welcome")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")