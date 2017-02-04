from random import randint

class SpaceCat(object):
    def __init__(self):
        hp = 100,
        attack = 5,
        defense = 5,
        inventory = {}

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            next_scene_name = current_scene.startMap()
            current_scene = self.scene_map.get_scene(next_scene_name)

class CatNipConstellation(object):
    def startMap(self):
        # print "you are in the catNipConstellation beeeaaootcchh"
        # print "where to now?"
        print "As you throttle in from outer CatNipConstellation"
        print "You notice something strange, there's no signal from"
        print "KitterSat, one of the most powerful satellites ever"
        print "made by the Kit-Kat Federation. It has the ability"
        print "to house a crew."
        print "will you go and check it out?"
        print "Kattia, KittySpaceOne, or KitterSat?"
        nextLvl = raw_input(">> ")
        return nextLvl

class KitterSat(object):
    def startMap(self):
        print "Ship is docked in KitterSat, there was no signal"
        print "ever picked up while coming in, but nothing appeared"
        print "wrong on the outside. Gas spills out as you open the hatch."
        print "Lights are off, everythings very silent. A Burst of noise"
        print "From the kitchen!! You turn the light and there's a possesed"
        print "and demonic looking alien with its sight on you."
        print "do you shoot your blaster, run, or try to communicate with it?"
        action = raw_input(">> ")
        if(action == "shoot blaster"):
            print "the alien's skin is melting under your scorching laser."
            print "It leaps out at you, bleeding all over the place with a"
            print "horrible stench. You keep shooting, and pieces of the"
            print "alien are flying off! But it's still coming for you!"
            print "you're feeling mists of alien blood as the alien is inches"
            print "away"
            print "Do you run, throw katnade in its mouth, or try to blast its eyes?"
            action2 = raw_input(">> ")
            if(action2 == "run"):
                print "You turn your back and start running back. Something trips your"
                print "foot and you fall! It's a tentacle, and it's sucked on to your paw!"
                print "when you look up the alien is on you, and that's the last thing you see"
                print "before you die"
                return "Death"
            if(action2 == "throw katnade in its mouth"):
                print "In an instant you pull a katnade from your spacejacket and flick the pin"
                print "off with your opposable cat thumb, then lob the granade two feet in front of"
                print "you as the alien closes in with its mouth wide open. The katnade goes down the alien's"
                print "throat. As it seems to cough for a second, you turn and jump over a near kitchen table"
                print "BOOM!!!! You feel alien blood and guts cover the room as the alien explodes. These stains"
                print "will not come off your new jacket, great."
                print "you go and pick up some glowing relic in the alien carcass."
                print "should you take it?"
                print "You turn the satellite on, report to CatCentral, and get back on KittySpaceOne"
                return "KittySpaceOne"
        if(action == "run"):
            print "The alien leaps out at you, but you are already running. You scrape past the door and"
            print "slam the close button. As the doors glide shut, the alien makes another leap and smashes"
            print "into the door, leaving slime splatters everywhere. The alien is at least twice your height"
            print "and seems to be ball shaped with a mouth and eyes on its front and tentacles coming from its"
            print "back. You get back on KittySpaceOne and call the Federation to send a crew to clean this up."
            return "KittySpaceOne"


class KittySpaceOne(object):
    def startMap(self):
        print "you're aboard kitty Space One"
        print "where do you want to go?"
        print "Kattia or CatNipConstellation?"
        nextLvl = raw_input(">>")
        return nextLvl

class Kattia(object):
    def startMap(self):
        print "you've made it to kattia"
        print "CatNipConstellation or KittySpaceOne?"
        nextLvl = raw_input(">>")
        return nextLvl

class Death(object):
    def startMap(self):
        print "GAME OVER"
        return "bloopppp"

class Map(object):
    scenes = {
        "CatNipConstellation": CatNipConstellation(),
        "KittySpaceOne": KittySpaceOne(),
        "Kattia": Kattia(),
        "KitterSat": KitterSat(),
        "Death": Death()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def get_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.get_scene(self.start_scene)

a_map = Map("KittySpaceOne")
a_game = Engine(a_map)
a_game.play()
