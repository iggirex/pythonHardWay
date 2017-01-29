class Scene(object):
    def __init__(self):
        pass

class Map(object):
    def __init__(self):
        pass

    def next_scene():
        pass

    def current_scene():
        print "in current scene"
        pass

class Meow6_Nebula(object):
    def __init__(self):
        self.saying = "we are in Meow6"

    def enter(self):
        print "we have entered"
        print "and now a choice, you must make right"
        print "how many figers in a hand"
        answer = raw_input(">> ")
        if(answer == "5"):
            print "You are a sucker"
            print "and you die"
            Death()
        elif(answer != 5):
            print "Good job, fingers had to be amputated"
            print "and you go on to the next level"
            nextLevel = CatscratchConstellation()
            nextLevel.enter()

class PlanetPicoDeGallo(object):
    def __init__(self):
        pass
    def enter(self):
        print "inside pico de gallo"

class CatscratchConstellation(object):
    def __init__(self):
        pass
    def enter(self):
        print "You've catspeeded into the CatscratchConstellation"
        print "Many enemies lurk here, must be carefule"
        print "Which planet would you like to head to?"
        print ">Planet Pico de Gallo\n>Planet Green Chile"
        answer = raw_input(">> ")
        if answer == "Planet Pico de Gallo" or answer == "planet pico de gallo":
            pico = PlanetPicoDeGallo()
            pico.enter()
        elif answer == "Planet Green Chile" or answer == "planet green chile":
            PlanetGreenChile()

class Death(object):
    def __init__(self):
        pass
    def enter(self):
        print "You done died sucker GOODBYE"


class Engine(object):
    def __init__(self):
        pass

    def play(self):
        x = 0
        while x < 10:
            print "yo x is: ", x
            x += 1
        now = Meow6_Nebula()
        now.enter()

game = Engine();
game.play()
