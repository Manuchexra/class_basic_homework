#Create a "Person" class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
aboutMe=Person("Manuchexra",16)
print(f'My name is {aboutMe.name} and i am {aboutMe.age} years old')
