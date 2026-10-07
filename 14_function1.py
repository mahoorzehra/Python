# Intro to python 23/09/26
# 1. add
def add(a,b):
    print(a+b)
a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number: '))
add(a,b)


# 2. Prime number
n = int(input('Enter the number: '))
flag = 0
for i in range(2,n):
    if n%i == 0:
        flag = 1
        break
if flag == 0:
    print('No prime')
else:
    print('Prime')


# 3. Palindrome
c  = input('Enter the word:')
rev = c[::-1]
if c == rev:
    print('Palindrome')
else:
    print('Not a palindrome')