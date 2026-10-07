#nested dictionary      date: 11/09/26
dt={
    1: {'name': 'Mahi', 'class': '10th', 'section': 'A'},
    'abc': {'name': 'baneen', 'class': '11th', 'section': 'C'},
    '3': {'name': 'Avi', 'class': '12th', 'section': 'B'}
}

#printing the entire nested dictionary
print(dt)

#printing one nested dictionary
print(dt['abc'])

#update 
dt['3']['class'] = 'haziq'
print(dt['3'])

#add
dt['4th'] = {'name': 'farah', 'class': '8th', 'section': "D"}
print(dt['4th'])

#delete entire list
del dt[1] 
print(dt)

#delete one 
del dt['abc']['class']
print(dt['abc'])

#note: Key can NOT be same but value can be same