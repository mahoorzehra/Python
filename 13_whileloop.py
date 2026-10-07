# while loop being used on calculator, palindrome, even odd   22/09/26
# even odd
# while True:
#     n = int(input('Enter a number = '))
#     if n%2 == 0:
#         print('Even')
#     else:
#         print('odd')
#     ch = input('Enter no to exit: ')
#     if ch == 'no':
#         break

# # palindrome
while True:
    x  = input('Enter the word')
    rev = x[::-1]

    if x == rev:
        print('Palindrome')
    else:
        print('Not a palindrome')
    ch = input('Enter no to exit: ')
    if ch == 'no':
        break

# calculator
while True:
    n1 = int(input('Enter the 1st number: '))
    op = input('Enter the operator: ')
    n2 = int(input('Enter the 2nd number: '))
    if op == '+':
        print(n1+n2)
    elif op == '-':
        print(n1-n2)
    elif op == '*':
        print(n1*n2)
    elif op == '/':
        print(n1/n2)
    else:
        print('Not a valid operator')
    ch = input('Enter no to exit: ')
    if ch == 'no':
        break
    