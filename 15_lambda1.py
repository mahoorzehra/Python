# lambda (shorter version of function)
# addition
add = lambda x, y: x+y
print(add(10,2))
print(add(210,82))

# Square
sq = lambda a: a*a
print(sq(5))
print(sq(15))

# Taking input:
cube = lambda v: v*v*v
n= int(input('Enter a number: '))
print('Cube: ', cube(n))

# Multiple parameters, if else:
max = lambda x,y: x if x>y else y
print(max(20, 8))
