#Code tweaked from justcolorado's Simple Shooting Game (https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=41347#p435420)

image redstand:
    "shootem/fightsprite.png"

#For when Green is
transform moving_target:
    function randomyos
    alpha 1.0
    easeout 2.0 xpos 250
    alpha 0.0
    0.05
    alpha 1.0
    0.05
    alpha 0
    0.05
    alpha 0.5
    0.05
    alpha 0
    0.05
    repeat
#For when Green isn't with us
transform moving_target_fast:
    function randomyos
    alpha 1.0
    easeout 1.5 xpos 250
    alpha 0.0
    0.05
    alpha 1.0
    0.05
    alpha 0
    0.05
    alpha 0.5
    0.05
    alpha 0
    0.05
    repeat

screen ghostspawn():
    text "Jewels: [numjewels]" xpos 20 ypos 10
    #text "Ghosts Created: [totghost]" xpos 20 ypos 35
    text "Ghosts killed: [numturns]" xpos 20 ypos 650
    timer 15.0 action Jump("battleready") #this only works if you don't click anything :\
    imagebutton:
        idle "shootem/ghost.png"
        hover "shootem/ghost_dead.png"
        if greenwith:
            at moving_target
        else:
            at moving_target_fast
        action Jump('hitghost')

#The set up for all the differnt kinds of Shoot Modes
label begin_ShootMode:
    $ numturns = 0
    #$ totghost = 0
    if greenwith:
        show particleFog1:
            alpha 0.5
    show redstand at left #Add the player to the left
    if bluewith:
        show blueshield at left
    if rookiewith:
        show grassyrookie at left
    if greenwith:
        show particleFog2:
            alpha 0.3
    #Add a countdown
    show countdown at Position(xalign=.9, yalign=.9)
    call createghost
    return


label createghost:
    #Add the imagebutton
    call screen ghostspawn
    return

label hitghost:
    $ numturns += 1
    jump createghost

label gameover:
    scene black
    "You died."
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
    nvlmc "You currently have [hp] amount of health left."
    nvlmc "Battle Start"

    #escape nvl mode
    nvl clear
    window hide

    return
