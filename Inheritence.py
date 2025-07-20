#single inheritance
class dad():
    def phone(self):
        print("dad's phone")    

#multiple inheritance
class mom():
    def car(self):
        print("mom's car")
                         
class son(dad, mom):
    def bike(self):
        print("son's bike")

son1 = son()
son1.phone()
son1.car()
son1.bike()


