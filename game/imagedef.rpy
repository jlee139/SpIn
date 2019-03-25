#Ending Cards
image deadend = "ending/deadend.png"
image badend = "ending/badend1.png"
image truend = "ending/trueend.png"

#Backgrounds To be Used
image beastoverlay = "battlemode/overlay.png"
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
#blue
image bl temp = "bluetemp.png"

#green
image g temp = "greentemp.png"

#rookie
image r temp = "rookietemp.png"

#witch
image w temp = "witchsprite.png"

#Boss Battle Sprites
image battlew full = "battlemode/witch_tut_beg.png"
image battlew half = "battlemode/witch_tut_mid.png"
image battlew no = "battlemode/witch_tut_final.png"

#Fire Effect
image torchitall:
    "shootem/fire.png"
    alpha 1.0
    0.1
    alpha 0
    0.1
    alpha 1.0
    0.1
    alpha 0
    0.1
    alpha 1.0
    0.1
    alpha 0

#Scartch for Normal Attack in RPG Mode
image scratch:
    "battlemode/scratch.png"
    alpha 1.0
    0.1
    alpha 0
    0.1
    alpha 1.0
    linear 0.2 alpha 0.0

#Defense Shield for RPG Mode
image shield:
    "battlemode/defense.png"
    rotate 0
    linear 0.5 rotate 360
    linear 0.2 alpha 0.0

#Heal for RPG Mode
image healing:
    "battlemode/purpleheal.png"
    alpha 1
    linear 0.4 alpha 0
    "battlemode/blueheal.png"
    alpha 1
    linear 0.4 alpha 0
    "battlemode/greenheal.png"
    alpha 1
    linear 0.4 alpha 0

#Explosion for Shoot Mode
image dustparticle:
    "shootem/explode.png"
    alpha 0
    linear 0.05 alpha 0.8
    alpha 1
    linear 0.5 alpha 0.0


#Whiteflash tweaked from code by Epadder (https://lemmasoft.renai.us/forums/viewtopic.php?t=16604)
image whiteflash:
    Solid("#fff")
    0.5
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
