# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nvlmc = Character(None, kind=nvl)
#for if we ever get sprites for Red
define advmc = Character('[mcname]', kind=adv)

define green = Character('Green', color="#088329")
define blue = Character('Blue', color="#0638A9")
define rookie = Character('Rookie', color="#6B0B94")
define boss = Character('Boss', color="#A00303")
define prewitch = Character('???', color="#BC4244")
define witch = Character('Witch', color="#BC4244")

#Backgrounds To be Used
image office = "office.png"
image office memory = "office_memory.png"
image mansionout = "mansionoutside.png"
image mansionentrance = "mansionentrance.png"
image fronthall = "fronthall.png"
image portrait = "portrait.png"

#Character Approval Sprites
image blueapprove = "blueapprove.png"
image greenapprove = "greenapprove.png"
image rookieapprove = "rookieapprove.png"

#Character Sprites
image bluetemp = "bluetemp.png"
image greentemp = "greentemp.png"
image rookietemp = "rookietemp.png"

#Boss Battle Sprites
image tutorialwitchfull = "battlemode/witch_tut_beg.png"
image tutorialwitchhalf = "battlemode/witch_tut_mid.png"
image tutorialwitchno = "battlemode/witch_tut_final.png"

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
image countdown = DynamicDisplayable(countdown, length=10.0)

#Green's Fog Particle Effect Code from EvilDragon (https://lemmasoft.renai.us/forums/viewtopic.php?t=4962)
image particleFog1 = SnowBlossom("fog-particle.png", count=120, border=600, xspeed=(5, 200), yspeed=(5, -5), start=1, fast=True, horizontal=True)
image particleFog2 = SnowBlossom("fog-particle.png", count=120, border=600, xspeed=(-5, -200), yspeed=(-5, 5), start=0, fast=True, horizontal=True)

#Transform for the approval sprites
transform appsprite:
    xalign 0.6 yalign 0.4
    alpha 1.0
    0.2
    alpha 0.8
    0.2
    alpha 0.5
    0.2
    alpha 0.3
    0.2
    alpha 0

image allappsprite:
    "blueapprove.png"
    xalign 0.6 yalign 0.4
    alpha 1.0
    0.2
    alpha 0.8
    0.2
    alpha 0.5
    0.2
    alpha 0.3
    0.2
    alpha 0
    "greenapprove.png"
    xalign 0.6 yalign 0.4
    alpha 1.0
    0.2
    alpha 0.8
    0.2
    alpha 0.5
    0.2
    alpha 0.3
    0.2
    alpha 0
    "rookieapprove.png"
    xalign 0.6 yalign 0.4
    alpha 1.0
    0.2
    alpha 0.8
    0.2
    alpha 0.5
    0.2
    alpha 0.3
    0.2
    alpha 0

#Image of Blue's Shield
image blueshield:
    "shootem/shield.png"
    alpha 1.0
    0.2
    alpha 0.8
    0.2
    alpha 0.5
    0.2
    alpha 0.3
    0.2
    alpha 0.5
    0.2
    alpha 0.8
    0.2
    repeat

#Rookie's Grass
image grassyrookie:
    "shootem/grass1.png"
    0.5
    "shootem/grass2.png"
    0.5
    "shootem/grass3.png"
    0.5
    repeat


#Let's put together some Variables to be used
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

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
        trans.ypos = renpy.random.randint(0, 600)
        trans.xpos = renpy.random.randint(850, 1200)
        return None

    def countdown(st, at, length=0.0):
            remaining = length - st
            if remaining > 5.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                renpy.jump('battleready')
