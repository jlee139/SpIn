#RPG Set up
screen battleui():
    text "Jewels: [numjewels]" xpos 20 ypos 500
    text "Turns Left: [numturns]" xpos 20 ypos 520
    #Witch's HP Bar
    bar:
        range bossmaxhp
        value bosshp
        xmaximum 260
        xpos 850 ypos 200
    label _("Enemy HP") xpos 850 ypos 170
    bar:
        range 100
        value hp
        xmaximum 260
        xpos 20 ypos 580
    label _("Your HP") xpos 20 ypos 550
    imagebutton:
        xpos 320 ypos 480
        idle "battlemode/attack_up.png"
        hover "battlemode/attack_down.png"
        action Call('attackdmg')
    imagebutton:
        xpos 550 ypos 480
        idle "battlemode/defend_up.png"
        hover "battlemode/defend_down.png"
        action Call('defenddmg')
    imagebutton:
        xpos 780 ypos 480
        idle "battlemode/magic_up.png"
        hover "battlemode/magic_down.png"
        action Call('magicdmg')
    imagebutton:
        xpos 1010 ypos 480
        idle "battlemode/heal_up.png"
        hover "battlemode/heal_down.png"
        action Call('healdmg')


#For Tutorial Battle
label begin_TutRPG:
    $numturns = 20 #This is for debugging. Remember to turn this off!!
    $bosshp = 100
    $bossmaxhp = 100
    $turnnum = 0 #To determine whose turn it is

    #First place the enemy sprite in front of us
    show tutorialwitchfull at top

    #While we have turns, go through the battleui
    while numturns>1:
        #Display our health and numturns
        call screen battleui
        $numturns-=1

    return

label attackdmg:
    $bosshp -= 10
    "You did 10 damage!"
    call witchattack
    return

label defenddmg:
    return
label magicdmg:
    return

label healdmg:
    return

label witchattack:
    "The witch hits you!"
    $hp-=10
    return

return
