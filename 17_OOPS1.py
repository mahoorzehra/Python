# Basic OOPs                            29/9/26
class Fruits:                           # class is the blueprint
    def pomegranate(self):              # self because pomegranate will not recieve any parameter and get an error
        print('This is a red fruit')
    def banana(self):
        print('This is a yellow fruit')
    def kiwi(self):
        print('This is a green fruit')

x = Fruits()
x.pomegranate()       # accessing the fxn
x.kiwi()              # accessing the fxn