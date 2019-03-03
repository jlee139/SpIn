#Code tweaked from justcolorado's Simple Shooting Game (https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=41347#p435420)

image redstand:
    "shootem/fightsprite.png"

transform moving_target:
    xpos 1200
    linear 3.0 xpos 10
    repeat

screen imagebutton_test1():
    imagebutton:
        idle "shootem/ghost.png"
        hover "shootem/ghost_dead.png"
        #xpos 1200 ypos randomyos
        at moving_target
        action Jump('testing')

label begin_ShootMode:
    $ ghostshit = 0
    call shooter
    return

label shooter:

    #scene black
    show redstand at left #Add the player to the left
    #Add the imagebutton
    call screen imagebutton_test1


label testing:
    $ghostshit = ghostshit + 1
    call shooter

    return
