# indentation & if elif else                   Date: 15/09/26
#Q1: age
age = int(input("Enter your age:"))
if age>18:
    print('You are eligible')
else:
    print('Not eligible')

#Q2: grade
grade = input('Enter your grade: ')
if grade=='A':                          #NEVER FORGET A COLON
    print('Topper')
else:
    print('Failure')

# Incorporating multiple options:    elif: gives us a chance to check multiple options
grade = input('Enter your grade: ')
if grade=='A':                          
    print('Topper')
elif grade=='B':
    print('good')
elif grade== 'C':
    print('Average')
else:
    print('Failure')

# positive, negative and zero
n = input('Enter the number: ')
if n>0:                          
    print('Positive')
elif n==0:
    print('You entered zero')
else:
    print('Negative')

