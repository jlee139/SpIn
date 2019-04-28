#Tweak of Shootem Mode

transform ghostmove:
    function randomyos
    alpha 1.0 zoom 1.0
    easein_circ 1.0 zoom 2.0
    linear 0.2 alpha 0
    repeat

transform skelemove:
    function randomyos
    parallel:
        linear 0.5 xoffset 100 yoffset 100
        linear 0.5 xoffset -100 yoffset 100
        linear 0.5 xoffset 100 yoffset -100
        linear 0.5 xoffset -100 yoffset -100
    parallel:
        rotate 0
        linear 2.0 rotate 360
    repeat

transform wispmove:
    function randomyos
    alpha 1.0
    linear 1.0 alpha 0
    repeat



screen ghostspawn():
    frame:
        xpadding 10
        ypadding 10
        xalign 0.05
        yalign 0.95
        vbox:
            text "Ghosts killed: [numturns]"
screen ghoster():
    imagebutton:
        idle "shootem/ghost.png"
        hover "shootem/ghost_dead.png"
        at ghostmove
        action [get_mouse(), Jump('ghosthit')]
    imagebutton:
        idle "shootem/ghost.png"
        hover "shootem/ghost_dead.png"
        at ghostmove
        action [get_mouse(), Jump('ghosthit')]
    imagebutton:
        idle "shootem/skeleton.png"
        hover "shootem/skeleton_injured.png"
        at skelemove
        action [get_mouse(), Jump('ghosthit')]
    imagebutton:
        idle "shootem/wisp.png"
        hover "shootem/wisp_red.png"
        at wispmove
        action [get_mouse(), Jump('ghosthit')]
    imagebutton:
        idle "shootem/wisp.png"
        hover "shootem/wisp_red.png"
        at wispmove
        action [get_mouse(), Jump('ghosthit')]
    imagebutton:
        idle "shootem/wisp.png"
        hover "shootem/wisp_red.png"
        at wispmove
        action [get_mouse(), Jump('ghosthit')]

label shootfix:
    #"Hi. We're going to try this again."
    $quick_menu = False
    window hide
    call startshootem from _call_startshootem
    return

label startshootem:
    show countdown at Position(xalign=.9, yalign=.9)
    call createghosts from _call_createghosts
    return

label createghosts:
    #Add a countdown
    show screen ghostspawn
    call screen ghoster

    return
    #call screen skele

label ghosthit:
    #show dustparticle at Position(xpos=mouse_xy[0],ypos=mouse_xy[1])
    $ numturns += 1
    jump createghosts
    return

label battleready:
    hide screen ghostspawn
    scene black

    #nvl set up
    nvl clear
    window hide
    #scene bg office with fade
    window show

    nvlmc "Your information for the upcoming battle:"
    nvlmc "You have [numturns] energy to defeat the enemy."
    nvlmc "You have [numjewels] jewels protecting you."
    nvlmc "You health is currently at [hp]."
    nvlmc "Battle Start"

    #escape nvl mode
    nvl clear
    window hide

    $quick_menu = True

    return





return
