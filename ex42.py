class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
    def sayHi(self):
        print "Hi my name is",self.name

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    def __init__(self):
        self.greet = "yo ima fish"
    def greetNow(self):
        print self.greet

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

mary.sayHi()

frank = Employee("Frank", 120000)

frank.pet = rover

# flipper = Fish()

crouse = Salmon()

harry = Halibut()
