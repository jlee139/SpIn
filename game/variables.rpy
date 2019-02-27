# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nvlmc = Character(None, kind=nvl)
define advmc = Character(None, kind=adv)

define green = Character('Green', color="#088329")
define blue = Character('Blue', color="#0638A9")
define rookie = Character('Rookie', color="#6B0B94")
define boss = Character('Boss', color="#A00303")

#Let's put together some Variables to be used
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

    trueend = False #Activated when player has unlocked everything
    endingct = 0    #num of time player has played through
    #Affection points
    greenap = 0
    blueap = 0
    rookieap = 0
    bossap = 0
