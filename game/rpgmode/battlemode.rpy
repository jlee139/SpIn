#RPG Set up
screen battleui():
    text "Jewels: [numjewels]" xpos 20 ypos 500 outlines [ (1, "#fff") ]
    text "Energy Left: [numturns]" xpos 20 ypos 520 outlines [ (1, "#fff") ]
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
        action If(numturns >2, Call('magicdmg'), None)
    imagebutton: #Beserk Button
        xpos 870 ypos 480
        idle "battlemode/beast_up.png"
        hover "battlemode/beast_down.png"
        action If(numturns>10 or numjewels==3, Call('zerker'), None)
    imagebutton: #Heal Button
        xpos 1070 ypos 480
        idle "battlemode/heal_up.png"
        hover "battlemode/heal_down.png"
        action If(numjewels >=1, Call('healdmg'), None)



#For Tutorial Battle
label begin_TutRPG:
    $numturns = 20 #This is for debugging. Remember to turn this off!!
    $bosshp = 80
    $bossmaxhp = 80
    $turnnum = 0 #To determine whose turn it is
    #Set up variables for the upcoming battle
    $bossatk = 10
    $redatk = 10
    $beastmode = False #To keep track of damages in beast mode
    $showwincond = False #Keep track of whether or not we've seen the win condition


    #First place the enemy sprite in front of us
    show battlew full at top

    #While we have turns, go through the battleui
    while numturns>0 and bosshp>0 and hp>0:
        #Change the Sprite accordingly
        show battlew full at top
        if bosshp<=40:
            show battlew half at top
        if bosshp<=20:
            show battlew no at top

        #Checks happen here before we start the battles
        #If witch's HP is 0, go straight to winning stance
        if bosshp <1 and showwincond==False:
            $showwincond = True
            jump wincondition

        #If player's HP is 0, go straight to game over
        if hp < 1:
            jump healthgameover

        #if the turn is 3, then reset
        if turnnum == 3:
            $turnnum=0
            $beastmode = False

        #Display our health and numturns
        call screen battleui
        $numturns-=1
        $turnnum+=1
        #If we're in beastmode, put up the attack
        if beastmode:
            $bossatk = 7
            $redatk = 30
            show beastoverlay
        else:
            $bossatk = 10
            $redatk = 10
            hide beastoverlay

    #If witch's HP is 0, go straight to winning stance
    if bosshp <1 and showwincond==False:
        $showwincond = True
        jump wincondition
        return

    #if we have ran out of turns, go straight to game over
    if numturns<1:
        jump turngameover
        return
    return

label attackdmg:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=8: #There's 20% chance she'll defend
        call witchdef
    $bosshp -= redatk
    show scratch:
        xalign 0.5 yalign 0.3
    "You did [redatk] damage!"
    hide scratch
    #If witch's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if witchdef <8: #There's 80% chance she'll attack
        call witchturn
    return

label defenddmg:
    show shield:
        xalign 0.5 yalign 0.3
    "You defended. All damage reduced."
    hide shield
    $bossatk = bossatk*0.7
    call witchturn
    return

label magicdmg:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=6: #There's 40% chance she'll defend
        call witchdef
    $numturns-=2
    $redatk = redatk * 1.5
    show torchitall:
        xalign 0.5 yalign 0.3
    "By using up 3 of your energy, you fired a magic spell that does [redatk] damage."
    hide torchitall
    $bosshp -= redatk
    #If witch's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if witchdef <6: #There's 60% chance she'll attack
        call witchturn
    return

label healdmg:
    scene black
    menu:
        "You can crush 1 jewel to fully heal yourself."
        "Crush jewel":
            show healing:
                xalign 0.5 yalign 0.3

        "Nevermind.":
            $numturns +=1
            return
    "You're fully healed."
    hide healing
    $numjewels -= 1
    $hp = 100
    call witchturn
    return

label zerker:
    menu:
        "Damage done is increased and damage received is decreased for the next 3 turns."
        "Use 10 energy" if numturns>10:
            $numturns -=9
        "Use 3 jewels" if numjewels==3:
            $numjewels = 0
            $numturns +=1
        "Nevermind.":
            $numturns +=1
            return

    $beastmode = True
    $turnnum = 0 #Once this turns 3, we need to turn off beastmode
    return

label witchdef:
    "The witch defended. All damage reduced."
    $redatk = redatk*0.7 #Reduce Red's attack to 7
    return

label witchturn:
    show battlew full at top
    if bosshp<=40:
        show battlew half at top
    if bosshp<=20:
        show battlew no at top
    $ witchmagic = renpy.random.randint(1,10)
    if witchmagic >=6: #There's 40% chance she'll use magic
        $bossatk = bossatk*1.5
        "The enemy fired a magic spell that does [bossatk] damage"
        with vpunch
        $hp-=bossatk
    else:
        "The enemy did [bossatk] damage!"
        with vpunch
        $hp-=bossatk
    return

label healthgameover:
    hide beastoverlay
    scene black
    "You have ran out of health. You are unable to keep your promise of keeping your comrades safe and die."
    "Keep a better eye on your health next time!"
    scene end dead with fade
    pause 2.0
    return

label turngameover:
    hide beastoverlay
    scene black
    "You have ran out of energy. You are unable to keep your promise of keeping your comrades safe and die"
    "Try shooting more ghosts down next time!"
    scene end dead with fade
    pause 2.0
    return

label wincondition:
    hide beastoverlay
    $showwincond = True
    scene black
    "You have defeated the enemy!"
    return

return
