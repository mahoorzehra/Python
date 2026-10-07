# Inheritance               30/09/26
# class ils:
#     def edu(self):
#         print('This is ILS Srinagar')
# class ils2:
#     def inst(ils):
#         print('This is ils 2')
# x = ils2
# x.inst()
# x.edu()

# Multiple inheritance
class A: 
    def aa(self):
        print('This is a part of class A')
class B:
    def bb(self):
        print('This is a part of class B')
class C(A,B):
    pass

# Multi level inheritance
class A: 
    def aa(self):
        print('This is a part of class A')
class B(A):
    def bb(self):
        print('This is a part of class B')
class C(B):
    def cc(self):
        print('This is a part of class C')
x= C()
x.aa()
x.bb()
x.cc()