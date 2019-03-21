#Tweak of Shootem Mode

transform ghostmove:
    function randomyos

transform skelemove:
    function randomyos

transform wispmove:
    function randomyos



screen ghostspawn():
    text "Ghosts killed: [numturns]" xpos 20 ypos 650
screen ghoster():
    imagebutton:
        idle "shootem/ghost.png"
        hover "shootem/ghost_dead.png"
        at ghostmove
        action Jump('ghosthit')
    imagebutton:
        idle "shootem/skeleton.png"
        hover "shootem/skeleton_injured.png"
        at skelemove
        action Jump('ghosthit')
    imagebutton:
        idle "shootem/wisp.png"
        hover "shootem/wisp_red.png"
        at wispmove
        action Jump('ghosthit')

label shootfix:
    "Hi. We're going to try this again."
    call startshootem
    return

label startshootem:
    show countdown at Position(xalign=.9, yalign=.9)
    call createghosts
    return

label createghosts:
    #Add a countdown
    show screen ghostspawn
    call screen ghoster

    return
    #call screen skele

label ghosthit:
    $ numturns += 1
    jump createghosts
    return

label battleready:
    scene black

    #nvl set up
    nvl clear
    window hide
    #scene bg office with fade
    window show

    nvlmc "Your information for the upcoming battle:"
    nvlmc "You have [numturns] amount of energy to defeat the enemy."
    nvlmc "You have [numjewels] jewels protecting you."
    nvlmc "You currently have [hp] amount of health."
    nvlmc "Battle Start"

    #escape nvl mode
    nvl clear
    window hide

    return





return
