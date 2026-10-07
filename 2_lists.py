# lec 5

# list: stores multiple values in the same variable; mutable(changeable- update, add, remove)
lt = [2, "asad", 90.7, 'paris']
lt.append("True")       #add to the end
lt.insert(1, 'blue')    #insert at a specific index
lt.remove(90.7)         #remove by value
lt.pop(3)               #remove by index
print(lt)

# lec 6: tuple, Set, dictionary 

#tuple: stores multiple values in the same variable; initialized using paranthesis;  ordered; indexed; immutable so NO CHANGES can be made
tp = (21, 34, "wasiq", 'ibrahim')
print(tp)  # ordered: in the same sequence as set

#Set: stores multiple values in the same variable; initialized using curly braces; unordered; unindexed; doesnt allow duplicates
# here we can add and remove with value but not with index
st = {33, "abc", "ptcfrktfd", 999}
st.add("Mahoor")        #to add by value
st.remove(33)           #to remove by value
print(st)

#key value pairs: stores multiple values in the same variable; ordered; unindexed, only keys used to access instead of indices
kvp = {
    "name" : "Mahoor",
    "class" : 12,
    "address" : "srg"
}
print(kvp['name'])
kvp["address"] = 'islamabad'    #update
kvp["pin-code"] = 190011        #to add
del kvp['name']
print(kvp)