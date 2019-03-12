#RPG Set up
screen battleui():
    text "Jewels: [numjewels]" xpos 20 ypos 500
    text "Turns Left: [numturns]" xpos 20 ypos 520
    bar: #Enemy's HP Bar
        range bossmaxhp
        value bosshp
        xmaximum 230
        xpos 850 ypos 200
    label _("Enemy HP") xpos 850 ypos 170
    bar: #Red's HP
        range 100
        value hp
        xmaximum 230
        xpos 20 ypos 580
    label _("Your HP") xpos 20 ypos 550
    imagebutton: #Attack Button
        xpos 270 ypos 480
        idle "battlemode/attack_up.png"
        hover "battlemode/attack_down.png"
        action Call('attackdmg')
    imagebutton: #Defend Button
        xpos 470 ypos 480
        idle "battlemode/defend_up.png"
        hover "battlemode/defend_down.png"
        action Call('defenddmg')
    imagebutton: #Magic Attack Button
        xpos 670 ypos 480
        idle "battlemode/magic_up.png"
        hover "battlemode/magic_down.png"
        action Call('magicdmg')
    imagebutton: #Beserk Button
        xpos 870 ypos 480
        idle "battlemode/heal_up.png"
        hover "battlemode/heal_down.png"
        action If(numturns >10, Call('zerker'), None)
    imagebutton: #Heal Button
        xpos 1070 ypos 480
        idle "battlemode/heal_up.png"
        hover "battlemode/heal_down.png"
        action If(numjewels >=1, Call('healdmg'), None)



#For Tutorial Battle
label begin_TutRPG:
    $numturns = 20 #This is for debugging. Remember to turn this off!!
    $bosshp = 100
    $bossmaxhp = 100
    $turnnum = 0 #To determine whose turn it is
    #Set up variables for the upcoming battle
    $bossatk = 10
    $redatk = 10


    #First place the enemy sprite in front of us
    show tutorialwitchfull at top

    #While we have turns, go through the battleui
    while numturns>1:
        #Display our health and numturns
        call screen battleui
        $numturns-=1
        $turnnum+=1
        $bossatk = 10
        $redatk = 10

    return

label attackdmg:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=8: #There's 20% chance she'll defend
        call witchdef
    $bosshp -= redatk
    "You did [redatk] damage!"
    if witchdef <8: #There's 80% chance she'll attack
        call witchturn
    return

label defenddmg:
    "You defended. All damage reduced."
    $bossatk = bossatk*0.7
    call witchturn
    return

label magicdmg:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=6: #There's 40% chance she'll defend
        call witchdef
    $numturns-=2
    $redatk = redatk * 1.5
    "By using up 3 of your turns, you fired a magic spell that does [redatk] damage."
    $bosshp -= redatk
    if witchdef <4: #There's 60% chance she'll attack
        call witchturn
    return

label healdmg:
    "By crushing a jewel, you fully healed yourself."
    $numjewels -= 1
    $hp = 100
    call witchturn
    return

label zerker:
    "In return for 10 of your turns, all damage is multiplied by 3 for the next 3 turns."
    $numturns -=10
    return

label witchdef:
    "The witch defended. All damage reduced."
    $redatk = redatk*0.7 #Reduce Red's attack to 7
    return

label witchturn:
    $ witchmagic = renpy.random.randint(1,10)
    if witchdef >=6: #There's 40% chance she'll use magic
        $bossatk = bossatk*1.5
        "The enemy fired a magic spell that does [bossatk] damage"
        $hp-=bossatk
    else:
        "The enemy did [bossatk] damage!"
        $hp-=bossatk
    return

return
