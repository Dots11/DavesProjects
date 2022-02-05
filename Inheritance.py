class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): #'Dog' class inherits all the methods defined in the parent 'Mammal' class inheritance reduces repetitive code
    def bark(self):
        print("bark")
    #pass if no methods are present in the class

class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.bark()


cat1 = Cat()
cat1.be_annoying()


