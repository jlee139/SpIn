#Tweak of Shootem Mode

transform ghostmove:
    function randomyos

transform skelemove:
    function randomyos

transform wispmove:
    function randomyos



screen ghostspawn():
    text "Jewels: [numjewels]" xpos 20 ypos 10
    #text "Ghosts Created: [totghost]" xpos 20 ypos 35
    text "Ghosts killed: [numturns]" xpos 20 ypos 650
    timer 15.0 action Jump("battleready") #this only works if you don't click anything :\
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
    call createghosts

label createghosts:
    show screen ghostspawn
    call screen ghoster

    return
    #call screen skele

label ghosthit:
    $ numturns += 1
    jump createghosts

return
