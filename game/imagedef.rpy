#Ending Cards
image end dead = "ending/deadend.png"
image end bad = "ending/badend1.png"
image end true = "ending/trueend.png"
image end one = "ending/end1.png"
image end two = "ending/end2.png"
image end three = "ending/end3.png"
image end bluebad = "ending/bluebadend.png"
image end bluegood = "ending/bluegoodend.png"
image end greenbad = "ending/greenbadend.png"
image end greengood = "ending/greengoodend.png"
image end rookiebad = "ending/rookiebadend.png"
image end rookiegood = "ending/rookiegoodend.png"

#Backgrounds To be Used
image beastoverlay = "battlemode/overlay.png"
image bg office = "background/office.png"
image bg office memory = "background/office_memory.png"
image bg mansionout = "background/mansionoutside.png"
image bg mansionentrance = "background/mansionentrance.png"
image bg fronthall = "background/fronthall.png"
image bg portrait = "background/portrait.png"
image bg diningroom = "background/diningroom.png"
image bg stairway = "background/stairway.png"
image bg threedoors = "background/threedoors.png"
image bg greenroom = "background/greenroom.png"
image bg exitroom = "background/onedoorexit.png"
image bg exitroomhole = "background/onedoorexit-hole.png"
image bg thirdhall = "background/hallway.png"
image bg thirdhallclose = "background/hallway_closeup.png"
image bg thirdhallbroke = "background/hallway-broken.png"
image bg thirdhallbrokeclose = "background/hallway_closeup-broken.png"
image bg atticdark = "background/attic_dark.png"
image bg atticlight = "background/attic_lighter.png"


#CGs to be Used
image cg foxreveal = "cg/fox.png"

#Character Approval Sprites
image blueapprove = "blue/blueapprove.png"
image greenapprove = "green/greenapprove.png"
image rookieapprove = "rookie/rookieapprove.png"

#Character Sprites
#blue
image bl temp = "blue/bluetemp.png"

#green
image g temp = "green/greentemp.png"

#rookie
image r temp = "rookie/rookietemp.png"

#witch
image w temp = "witch/witchsprite.png"
image w anger = "witch/witchsprite-anger.png"
image w annoyance = "witch/witchsprite-annoyance.png"
image w complain = "witch/witchsprite-complain.png"
image w crying = "witch/witchsprite-crying.png"
image w dark = "witch/witchsprite-dark.png"
image w darkfrown = "witch/witchsprite-darkfrown.png"
image w darksmile = "witch/witchsprite-darksmile.png"
image w laughing = "witch/witchsprite-laughing.png"
image w preplexed = "witch/witchsprite-preplexed.png"


#butler
image but temp = "enemy/butler.png"
image but anger = "enemy/butler-anger.png"
image but annoyance = "enemy/butler-annoyance.png"
image but happy = "enemy/butler-happy.png"
image but saddness = "enemy/butler-saddness.png"

#Boss Battle Sprites
image battlew full = "battlemode/witch_tut_beg.png"
image battlew half = "battlemode/witch_tut_mid.png"
image battlew no = "battlemode/witch_tut_final.png"
image battleb full = "battlemode/butfirst.png"
image battleb half = "battlemode/butmid.png"
image battleb no = "battlemode/butlast.png"
image battlepuppet1 = "battlemode/puppet.png"
image battlepuppet2 = "battlemode/puppet.png"
image battlepuppet3 = "battlemode/puppet.png"
image battlepuppet4 = "battlemode/puppet.png"


#Investigation Sprites
image ghostdis = "huntmode/ghost_dead.png"
image skeledis = "huntmode/skeleton_injured.png"
image wispdis = "huntmode/wisp_red.png"
image chestfound = "huntmode/chest.png"

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
    linear 0.5 alpha 0.8
    alpha 1
    linear 1.0 alpha 0.0


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
    "blue/blueapprove.png"
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0
    "green/greenapprove.png"
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0
    "rookie/rookieapprove.png"
    alpha 1.0
    xalign 0.95 yalign 0.05
    linear 2.0 alpha 0
