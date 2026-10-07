# Keywords: 
# break 
for i in range(10):
    if i==4:
        break
    print(i)

# continue   
for i in range(10):
    if i==4:
        continue
    print(i)

#printing a list as a list:
lt = ["Wasik", "Abdul", 121, 24, True, 4, 20]
print(lt)

#accessing lists but not as a list:
lt = [1, 7.5, 3, True, 4, 'hello', 'abc']
# instead of writing print(lt) write:
for item in lt:
    print(item)

#using continue in lt:
for item in lt:
    if item == True:
        continue
    print(item)

#dictionary:
dt= {
    'name' : 'Abc',
    'roll number' : 21,
    'pincode' : 190001
    }
for key, value in dt.items():
    print(key, ':', value)

#prime number:
n = int(input('Enter the number: '))
if n<=1:
    print('It is not a prime number')
else:
    for i in range(2,n):
       if i in range(2, n):
           print('Not  prime')
           break
    else:
        print('prime number')
