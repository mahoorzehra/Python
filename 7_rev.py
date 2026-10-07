#       ______LISTS______
lt = [[['hello', 90, 44.2],['Abdul', True, 12]],[['Hey',False, 2],[11, 70, 80]],[[True, False, 9],[12, 'khan', 'fazilat']]]

#accessing:
print(lt)
print(lt[0])
print(lt[0][1][2])

#update:
lt[0][0][0] = 'hii'
print(lt[0][0][0])

#add:
lt[1][0].append('faiz') 
print(lt[1][0])

lt[1][0].insert(1, False)
print(lt[1][0])

#delete:
del lt[2][0][0]
print(lt[2][0][0])

#      ________Dictionary________
dt= {
    1:{'Name': {'fname' : 'Abdul', 'lname' : "Majid"},
       "Address" : {'pincode' : 190002, 'District' : 'srinagar' }},
    2: {'Name': {'fname' : 'Mir', 'lname' : "Azra"},
       "Address" : {'pincode' : 190012, 'District' : 'budgam' }},
}

#access:
print(dt[1]['Name']['lname'])

#update: 
dt[2]['Address']['District'] = 'kupwara'
print(dt[2]['Address']['District'])

#add:
dt[3] = {'Name': {'fname' : 'Mir', 'lname' : "Azra"}, "Address" : {'pincode' : 190012, 'District' : 'budgam' }}
print(dt[3])

#delete
del dt[2]
print(dt)