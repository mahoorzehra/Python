# Using try except, we try to fix everyerror gracefully
# attribute error:
try:
    a = 'hello'
    a. append('123')
    print(a)
except AttributeError:
    print("You can't modify a string")

# Index out of range error
try:
    lt1 = [1, 2, 'abc']
    print(lt1[9])
except IndexError:
    print('You are trying to access a non existing list item')