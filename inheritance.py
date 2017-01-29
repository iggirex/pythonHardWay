class Parent(object):
    def implicit(self):
        print "PARENT implicity()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# to override inheritance, write a function of same name in Child

class Parental(object):
    def override(self):
        print "PARENT override()"

class Kid(object):
    def override(self):
        print "KID override()"

mom = Parental()
girl = Kid()

mom.override()
girl.override()
mom.override()

# override parent inheritance with SUPER

class Shaperone(object):
    def altered(self):
        print "PARENT altered()"

class Kiddo(Shaperone):
    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Kiddo, self).altered()
        print "CHILD, AFTER PARENT altered()"

daddyo = Shaperone()
kiddo = Kiddo()

daddyo.altered()
kiddo.altered()

# MIMIC inheritance with a little something called COMPOSITION

class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit"

    def altered(self):
        print "OTHER altered"

class OtherChild(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD AFTER OTHER altered()"

sonny = OtherChild()

sonny.implicit()
sonny.override()
sonny.altered()
