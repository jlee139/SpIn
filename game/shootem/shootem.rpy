#Tweak of Shootem Mode

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


label shootfix:
    "hi"
return
