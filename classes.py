class Car():
    def __init__(self,year):
        self.year = year

    def __init__(self):
         print('i am parent')

class Tata(Car):
    def __init__(self,year):
        self.year = year

    def display(self):
        print('i am child now')   
