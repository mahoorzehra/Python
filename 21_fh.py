# Traditional method                            5/10/26
# f = open('trial.txt', 'w')                      # here we create and write the file
# f.write('Hello World')
# f.close

# f = open('trial.txt', 'r')                      # here we read the file
# abc = f.read()
# print(abc)

# f = open('trial.txt', 'a')                      # here we update
# f.write('This is the updating part')
# f.close

# f = open('trial.txt', 'r')                      # here we read the updated file
# abc = f.read()
# print(abc)

# f = open('trialpt2.txt', x)
# f.write('New file')
# f.close

# f = open('trialpt2.txt', 'r')                      # here we read the updated file
# efg = f.read()
# print(x)

# modern method
# with open('trial.txt', 'r'):
#     data = f.read()
#     print(data)

with open (r'C:\Users\Mahoor Zehra\OneDrive\Desktop\sss.txt', 'w') as f:
     f.write('Hello baya')
    

