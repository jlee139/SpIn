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

#Whiteflash tweaked from code by Epadder (https://f95zone.com/threads/renpy-flash-and-punch-effects-how-to.18501/)
image whiteflash:
    Solid("#fff")
    alpha 0.0
    linear 0.25 alpha 0.3
    linear 0.75 alpha 0.0


#Let's put together some Variables to be used
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

    #Variables for Player during battle
    hp = 100
    numjewels = 3
    numturns = 0

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
        trans.ypos = renpy.random.randint(35, 700)
        return None
