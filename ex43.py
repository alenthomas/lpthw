from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser."
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutrom destruct bomb from the Weapons Armory."
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot":
            print "Quick on the draw you shoot the gothon, it misses and gothon "
            print "attacks biting you head off clean"
            return 'death'
        elif action == "dodge":
            print "you dodge as it was the movie matrix, but unfortunately u fall"
            print "break your neck and die"
            return 'death'
        elif action == "joke":
            print "Luckily you remember a gothon joke and spit it out"
            print "eengal enth barupikkal aanu babuetta..!!"
            print "and the gothon starts to laugh uncontrollably"
            print " you sprint past him to the Weapon's armory"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive to the weapon armory to take the neutron bomb"
        print "but the bomb is secured with a lock with 3 digits and you only"
        print "have 10 chances , else you will be locked inside for eternity"
        code = "%d%d%d" %(randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses <10:
            print "BZZZZED"
            guesses +=1
            guess = raw_input("[keypad]")

        if guess == code:
            print "the bomb is now accessible, place it on the bridge for"
            print "maximum anhilation"
            return 'the_bridge'
        else:
            print "there went your last chance" 
            print "see you in next life"
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "you burst onto the bridge with the bomb still in your hand"
        print "5 gothons spot you, whats you next move"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "in a panic you throw the bomb , not the wisest decision, the"
            print "gothons catch it, disarm it and then blow you to pieces"
            return 'death'

        elif action == "slowly place the bomb":
            print "you take the strategic advantage, place the bomb at the backward"
            print "door and lock it"
            print "and run towards the escape pod"
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "you rush to the escape pods there are only 5 left and some of them"
        print "are faulty, you don't have the time to examine you let the"
        print "GOD PLAY WITH DICE"
        
        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "you jump to pod %s and hit eject" % guess
            print "it would have been better if you choose a working pod"
            print "KABOOM"
            return 'death'
        else:
            print "you jump to pod %s and hit eject" % guess
            print "you should take a try at blackjack , you got a good hand"
            print "as you escape to the multiverse you see your mission accomplished"
            print "your ship along with the gothons go off with a puff"
            print "You WON"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "YOU won Good job"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
