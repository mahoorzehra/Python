# List ke andar list ke andar list                  8/09/26
lt = [[['hello', 66, 'mary'],[12, 'abc', 'two']],[['abdul', 'lily', 21],[11, 'umar', 'noor']],[[990, 'falah', 'aidah'],['azmat', 70, 660]]]

#update
lt[0][1][1] = 'maheen'
print(lt)

#append
lt[1][1].append('hey')
print(lt[1][1][3])

#insert
lt[2][1].insert(3, 'rabiya')
print(lt[2][1][3])

#del
del lt[1][0][2]
print(lt[1][0][2])

#pop
lt[1][1].pop(2)
