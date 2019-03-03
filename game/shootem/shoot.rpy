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
        xysize (300, 50)
        at moving_target
        action Jump('testing')

label begin_ShootMode:
    $ targets_hit = 0
    call shooter
    return

label shooter:

    #scene black
    show redstand at left #Add the player to the left
    #Add the imagebutton

    call screen imagebutton_test1

    #imagebutton idle "shootem/ghost.png" hover "shootem/ghost_dead.png" xpos 80 ypos 500 focus_mask

    #imagebutton auto "shootem/ghost.png" xpos 1200 ypos 500 focus_mask True action Start()

    #$ ui.imagebutton("shootem/ghost.png", "shootem/ghost_dead.png", clicked = ui.returns("fired"), xpos= 996, ypos = renpy.random.randint(35, 700))
    #$ fired_gun = ui.interact()

    #show expression position
    #if position.xpos > 950:
    #    if position.xpos < 1100:
    #        with vpunch
    #        "You Hit."
    #        $ targets_hit = targets_hit + 1
    #        call shooter

    #with vpunch
    #"You Missed."
    #call shooter

label testing:
    "Test text"

    return
