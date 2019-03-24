#To make it clear who is speaking. PyTom's code (https://lemmasoft.renai.us/forums/viewtopic.php?t=31501)
transform speak:
    linear .05 zoom 1.0

transform nospeak:
    linear .05 zoom 0.9

#Let's put together some Variables to be used
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

    #Cont of PyTom's code for making it clear who is speaking (https://lemmasoft.renai.us/forums/viewtopic.php?t=31501)
    class RaiseImage(object):
        def __init__(self, tag, low=0, high=10, speak=speak, nospeak=nospeak):
            self.tag = tag
            self.low = low
            self.high = high
            self.speak = speak
            self.nospeak = nospeak

        def __call__(self, event, **kwargs):

            if not renpy.showing(self.tag):
                return

            at_list = list(renpy.get_at_list(self.tag))

            if at_list:
                if at_list[-1] is self.nospeak:
                    at_list.pop()
                elif at_list[-1] is self.speak:
                    at_list.pop()

            if event == "begin":
                renpy.show(self.tag, zorder=self.high, at_list=at_list + [ self.speak ])
            elif event == "end":
                renpy.show(self.tag, zorder=self.low, at_list=at_list + [ self.nospeak ])

    #Variables for Player during battle
    hp = 100
    numjewels = 3
    numturns = 0
    totghost = 0

    #Battle Shoot Mode Helper
    greenwith = True
    bluewith = True
    rookiewith = True

    #Ending Variables
    trueend = False #Activated when player has unlocked everything
    greenend = False #Activated when player has unlocked green's happy end
    blueend = False #Activated when player has unlocked blue's happy end
    rookiened = False #Activated when player has unlocked rookie's happy end
    endingct = 0    #num of time player has played through

    #Affection points
    greenap = 0
    blueap = 0
    rookieap = 0
    bossap = 0

    #For Randomization of Shoot Mode
    #Tweaked code by Asceai (https://lemmasoft.renai.us/forums/viewtopic.php?t=27086)
    def randomyos(trans, st, at):
        trans.ypos = renpy.random.randint(10, 600)
        trans.xpos = renpy.random.randint(10, 1100)
        return None

    def countdown(st, at, length=0.0):
            remaining = length - st
            if remaining > 5.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                renpy.jump('battleready')

    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nvlmc = Character(None, kind=nvl)
#for if we ever get sprites for Red
define advmc = Character('[mcname]', kind=adv)

define green = Character('Green', color="#088329", callback=RaiseImage("g"))
define blue = Character('Blue', color="#0638A9", callback=RaiseImage("bl"))
define rookie = Character('Rookie', color="#6B0B94", callback=RaiseImage("r"))
define boss = Character('Boss', color="#A00303", callback=RaiseImage("bs"))
define prewitch = Character('???', color="#BC4244", callback=RaiseImage("w"))
define witch = Character('Witch', color="#BC4244", callback=RaiseImage("w"))

default mouse_xy = (0, 0)

#Backgrounds To be Used
image office = "office.png"
image office memory = "office_memory.png"
image mansionout = "mansionoutside.png"
image mansionentrance = "mansionentrance.png"
image fronthall = "fronthall.png"
image portrait = "portrait.png"
image diningroom = "diningroom.png"

#Character Approval Sprites
image blueapprove = "blueapprove.png"
image greenapprove = "greenapprove.png"
image rookieapprove = "rookieapprove.png"

#Character Sprites
image bl temp = "bluetemp.png"
image g temp = "greentemp.png"
image r temp = "rookietemp.png"
image w temp = "witchsprite.png"

#Boss Battle Sprites
image tutorialwitchfull = "battlemode/witch_tut_beg.png"
image tutorialwitchhalf = "battlemode/witch_tut_mid.png"
image tutorialwitchno = "battlemode/witch_tut_final.png"

#Shoot Mode Fire Effect
image torchitall:
    "shootem/fire.png"
    alpha 1.0
    0.05
    alpha 0
    0.05
    alpha 1.0
    0.05
    alpha 0
    0.05
    alpha 1.0
    0.05
    alpha 0

#Whiteflash tweaked from code by Epadder (https://lemmasoft.renai.us/forums/viewtopic.php?t=16604)
image whiteflash:
    Solid("#fff")
    1.4
    Null ()
    0.05
    repeat 2
    Solid("#000")

#Shoot Mode Images
# Show a countdown for 10 seconds.
image countdown = DynamicDisplayable(countdown, length=15.0)

#Green's Fog Particle Effect Code from EvilDragon (https://lemmasoft.renai.us/forums/viewtopic.php?t=4962)
image particleFog1 = SnowBlossom("fog-particle.png", count=120, border=600, xspeed=(5, 200), yspeed=(5, -5), start=1, fast=True, horizontal=True)
image particleFog2 = SnowBlossom("fog-particle.png", count=120, border=600, xspeed=(-5, -200), yspeed=(-5, 5), start=0, fast=True, horizontal=True)

#Transform for the approval sprites
transform appsprite:
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0

image allappsprite:
    "blueapprove.png"
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0
    "greenapprove.png"
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0
    "rookieapprove.png"
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0
