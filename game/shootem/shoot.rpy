#Code tweaked from justcolorado's Simple Shooting Game (https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=41347#p435420)

image target:
    "shootem/ghost.png"
    zoom 0.5

image redstand:
    "shootem/fightsprite.png"

transform moving_target:
    ypos 275
    xpos 1200
    linear 3.0 xpos 10
    repeat

label begin_hunt:

    $ shots_fired = 0
    $ targets_hit = 0
    call hunting
    return

label hunting:

    scene black
    show redstand at left
    show target at moving_target
    $ position = At(ImageReference("target"), moving_target)
    show expression position

    $ ui.imagebutton("shootem/crosshair.png", "shootem/crosshair_focused.png", clicked = ui.returns("fired"), xpos= 996, ypos = 163)
    $ fired_gun = ui.interact()

    show expression position
    if position.xpos > 950:
        if position.xpos < 1100:
            with vpunch
            "You Hit."
            $ shots_fired = shots_fired + 1
            $ targets_hit = targets_hit + 1
            if shots_fired >= 3:
                return
            call hunting

    with vpunch
    "You Missed."
    $ shots_fired = shots_fired + 1
    if shots_fired >= 3:
                return

    call hunting

    return
