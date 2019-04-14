#RPG Set up
screen battleui():
    frame:
        xpadding 10
        ypadding 10
        xalign 0.8
        yalign 0.2
    #    ymaximum 50
    #    xmaximum 250

        vbox:
            bar: #Enemy's HP Bar
                range bossmaxhp
                value bosshp
                xmaximum 230
            label _("Witch's HP ([bosshp]/[bossmaxhp])")
    frame:
        xpadding 10
        ypadding 10
        xminimum 950
        xalign 0.5
        yalign 0.95

        hbox:
            vbox:
                text "Jewels: [numjewels]"
                text "Energy Left: [numturns]"
                bar: #Red's HP
                    range 300
                    value hp
                    xmaximum 230
                    left_bar Frame("gui/bar/green.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/green_dry.png", gui.bar_borders, tile=gui.bar_tile)
                label _("Your HP ([hp]/300)")
            imagebutton: #Attack Button
                idle "battlemode/attack_up.png"
                hover "battlemode/attack_down.png"
                action Call('attackdmg')
            imagebutton: #Defend Button
                idle "battlemode/defend_up.png"
                hover "battlemode/defend_down.png"
                action Call('defenddmg')
            imagebutton: #Magic Attack Button
                idle "battlemode/magic_up.png"
                hover "battlemode/magic_down.png"
                action If(numturns >2, Call('magicdmg'), None)
            imagebutton: #Beserk Button
                idle "battlemode/beast_up.png"
                hover "battlemode/beast_down.png"
                action If(numturns>10 or numjewels==3, Call('zerker'), None)
            imagebutton: #Heal Button
                idle "battlemode/heal_up.png"
                hover "battlemode/heal_down.png"
                action If(numjewels >=1, Call('healdmg'), None)


#For Tutorial Battle
label begin_TutRPG:
    #$numturns = 20 #This is for debugging. Remember to turn this off!!
    $bosshp = 80
    $bossmaxhp = 80
    $turnnum = 0 #To determine whose turn it is
    #Set up variables for the upcoming battle
    $bossatk = 10
    $redatk = 10
    $beastmode = False #To keep track of damages in beast mode
    $showwincond = False #Keep track of whether or not we've seen the win condition
    $quick_menu = False

    window hide

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
    if numturns<1 and bosshp>0:
        jump turngameover
        return
    return

label attackdmg:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=9: #There's 10% chance she'll defend
        call witchdef
    $bosshp -= redatk
    show scratch:
        xalign 0.5 yalign 0.3
    "You did [redatk] damage!"
    hide scratch
    #If witch's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if witchdef <9: #There's 90% chance she'll attack
        call witchturn
    return

label defenddmg:
    show shield:
        xalign 0.5 yalign 0.3
    "You brace for impact. Damage taken is reduced."
    hide shield
    $bossatk = bossatk*0.7
    call witchturn
    return

label magicdmg:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=8: #There's 20% chance she'll defend
        call witchdef
    $numturns-=2
    $redatk = redatk * 1.5
    show torchitall:
        xalign 0.5 yalign 0.3
    "By using 3 energy, you fire a magic spell that does [redatk] damage."
    hide torchitall
    $bosshp -= redatk
    #If witch's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if witchdef <8: #There's 80% chance she'll attack
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
    $hp = 300
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
    "The witch braces for impact. Your attack does less damage."
    $redatk = redatk*0.7 #Reduce Red's attack to 7
    return

label witchturn:
    show battlew full at top
    if bosshp<=40:
        show battlew half at top
    if bosshp<=20:
        show battlew no at top
    $ witchmagic = renpy.random.randint(1,10)
    if witchmagic >=5: #There's 50% chance she'll use magic
        $bossatk = bossatk*1.5
        "The witch fires a magic spell that does [bossatk] damage."
        with vpunch
        $hp-=bossatk
    else:
        "The witch does [bossatk] damage."
        with vpunch
        $hp-=bossatk
    return

label healthgameover:
    hide beastoverlay
    scene black
    "You ran out of health. You are unable to keep your promise of keeping your comrades safe and die."
    "Keep a better eye on your health next time!"
    scene end dead with fade
    pause 2.0
    return

label turngameover:
    hide beastoverlay
    scene black
    "You have ran out of energy. You are unable to keep your promise of keeping your comrades safe and die."
    "Budget your energy more carefully!"
    scene end dead with fade
    pause 2.0
    return

label wincondition:
    hide beastoverlay
    $showwincond = True
    scene black
    "You won!"
    $quick_menu = True
    return

return
