class ils:
    def institute(self):
        print("This is ILS srinagar")
class Techbox(ils):
    def institute(self):
        # super().institute()               THIS LINE HELPS PRINT BOTH PARENT AND SUBCLASS FXN AT ONCE otherwise only the child class will print
        print("This is the BRANCH of ILS srinagar")
t = Techbox()
t.institute()