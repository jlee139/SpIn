#To make it clear who is speaking. PyTom's code (https://lemmasoft.renai.us/forums/viewtopic.php?t=31501)
transform speak:
    linear 0.05 zoom 1.0

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
    hp = 300
    numjewels = 3
    numturns = 0
    totghost = 0

    #Battle Shoot Mode Helper
    greenwith = True
    bluewith = True
    rookiewith = True

    #NVL vs ADV Screen Boolean
    nvl_showing = False

    #Ending Variables
    trueend = False #Activated when player has unlocked everything
    greenend = False #Activated when player has unlocked green's happy end
    blueend = False #Activated when player has unlocked blue's happy end
    rookiened = False #Activated when player has unlocked rookie's happy end
    endingct = 0    #num of time player has played through

    #The Color of Orbs collected
    greenOrb = False #Activated when player defeats Green's Boss
    blueOrb = False #Activated when player defeats Blue's Boss
    purpleOrb = False #Activated when player defeats Rookie's Boss

    #OnRoute Variables
    onGreenRoute = False #Activated when player is on Green's Route
    onBlueRoute = False #Activated when player is on Blue's Route
    onRookieRoute = False #Activated when player is on Rookie's Route

    #For Ending CGs
    badend1 = False #The very first ending we can get. "Empty Hands"
    greenbadend = False #Green's Bad Ending

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
#For all our blank textbox needs
define blanktxt = Character(None, kind=adv)
# name of the character.
define nvlmc = Character(None, kind=nvl)
#for if we ever get sprites for Red
#mcname = renpy.input("Enter your name")
#define advmc = Character('[mcname]', kind=adv)
define advmc = Character('Red', kind=adv)

define green = Character('Green', color="#088329", callback=RaiseImage("g"), window_background="gui/textbox-green.png")
define blue = Character('Blue', color="#0638A9", callback=RaiseImage("bl"), window_background="gui/textbox-blue.png")
define rookie = Character('Rookie', color="#6B0B94", callback=RaiseImage("r"), window_background="gui/textbox-rookie.png")
define boss = Character('Boss', color="#A00303", callback=RaiseImage("bs"), window_background="gui/textbox-red.png")
define prewitch = Character('???', color="#555555", callback=RaiseImage("w"), window_background="gui/textbox-witch.png")
define witch = Character('Witch', color="#555555", callback=RaiseImage("w"), window_background="gui/textbox-witch.png")
define prebut = Character('???', color="#555555", callback=RaiseImage("but"), window_background="gui/textbox-witch.png")
define butler = Character('Butler', color="#555555", callback=RaiseImage("but"), window_background="gui/textbox-witch.png")

default mouse_xy = (0, 0)
