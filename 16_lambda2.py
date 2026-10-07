num = [12, 88, 97, 2, 16, 11, 10, 88, 12]

# removing duplicates:
x = list(set(num))
print(x)

# sorting: 
# ascending:
num.sort()
print (num)
print(num[-1])

#descending;
c = [1, 44, 97, 44, 16, 11, 10, 4, 1]
c.sort(reverse=True)
print(c)
print(c[-1])

# To reverse the values:
a = 10
b = 45
a,b = b,a
print(a, b)

# filter:
fruit= ['pineapple', 'apple', 'banana', 'orange', 'pomegranate']
f = list(filter(lambda x: len(x)> 6, fruit))