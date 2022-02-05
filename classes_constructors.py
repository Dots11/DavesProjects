class Point:

    def move(self): #methods
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
point1.draw()

#w/Constructor
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self): #methods
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.y)

#exercise on classes and constructors

class Person:
    def __init__(self, name):
        self.name = name # self refers to object

    def talk(self): #the method
        print(f"Hi, I am {self.name}")

john = Person("John Smith") # 'john' is the object
john.talk()

bob = Person("Bob Smith") # again 'bob' is the object
bob.talk()