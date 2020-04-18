from colorama import init
class Geek:
    def __init__(self, age=0):
        self._age = age

        # getter method

    def get_age(self):
        return self._age

        # setter method

    def set_age(self, x):
        self._age = x

    def transform(self):
        self._age  = self._age.upper()

g = Geek("alma")
g.set_age("ss")
g.transform()


print(g.get_age())

