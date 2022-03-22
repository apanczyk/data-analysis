from enum import Enum

# TASK 1

class Gender(Enum):
    Male = 'Male',
    Female = 'Female'

class Animal():
    def __init__(self, genus, isAlive=True, gender=Gender.Female):
        self.isAlive = isAlive
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        try:
            if(self.gender is Gender.Female and partner.gender is Gender.Male and type(self) is type(partner)):
                new_animal = Animal(self.genus)
                new_animal.__class__ = self.__class__
                return new_animal
        except AttributeError:
            print("attribute not found")

    def __str__(self):
        return f'{self.__class__} {self.genus} {self.isAlive} {self.gender}'

class Dog(Animal):
    def __init__(self, isAlive=True, gender=Gender.Female):
        super().__init__('Canis', isAlive, gender)
        
    def woof():
        return "woof woof"

class Cat(Animal):
    def __init__(self, isAlive=True, gender=Gender.Female):
        super().__init__('Felis', isAlive, gender)
    
    def purr():
        return "purr"

f_dog_1 = Dog()
m_dog_1 = Dog(gender=Gender.Male)
f_cat_1 = Cat()
m_cat_1 = Cat(gender=Gender.Male)

kid_dog = f_dog_1.breed(m_dog_1)
kid_cat = f_cat_1.breed(m_cat_1)
no_cat = f_cat_1.breed(f_cat_1)
print(kid_dog)
print(kid_cat)
print(no_cat)
f_dog_1.breed('exception')