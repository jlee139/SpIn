#Code tweaked from justcolorado's Simple Shooting Game (https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=41347#p435420)

image redstand:
    "shootem/fightsprite.png"

transform moving_target:
    xpos 1200
    function randomyos
    easeout 2.0 xpos 20
    repeat

label dodmg:
    if numjewels>0:
        $numjewels -= 1
    elif hp >0:
        $hp -=1
    else:
        call gameover

screen ghostspawn():
    text "Jewels: [numjewels]" xpos 20 ypos 10
    #text "Position: [position.xpos]" xpos 20 ypos 30
    text "Ghosts killed: [numturns]" xpos 20 ypos 650
    imagebutton:
        idle "shootem/ghost.png"
        hover "shootem/ghost_dead.png"
        at moving_target
        action Jump('hitghost')

label begin_ShootMode:
    $ numturns = 0
    call shooter
    return

label shooter:
    show redstand at left #Add the player to the left
    call createghost


label createghost:
    #Add the imagebutton
    #$ position = ghostspawn.xpos
    call screen ghostspawn

label hitghost:
    $numturns = numturns + 1
    call createghost

label gameover:
    scene black
    "You died."

    return
