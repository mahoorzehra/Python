# logical operators
boy_age = int(input("Enter the boy's age:"))
girl_age = int(input("Enter the girl's age:"))

# and : both conditions should be true
if boy_age >18 and girl_age > 18:
    print('Welcome!')
# or : one of the conditions should be true
if boy_age >18 or girl_age > 18:
    print('Welcome!')

# for loop
for i in range(10):
    print(i)
for i in range(5):
    print('Hello World!')

#Printing static and dynamic together:
x = int(input('Enter a number:'))
print('Your number is :', x)

# Printing tables using loops:
a= int(input('Enter the number whose table you want:'))
for i in range(1,11):
    result = a * i
    print(a,'x', i, '=', result)            #make sure to put even '=' sign in quotes