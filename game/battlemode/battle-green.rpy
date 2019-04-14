#Our Battle for Green's Route. Boss: Butler
screen battleuigreen():
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
            label _("Enemy HP ([bosshp]/[bossmaxhp])")
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
                action Call('attackdmgg')
            imagebutton: #Defend Button
                idle "battlemode/defend_up.png"
                hover "battlemode/defend_down.png"
                action Call('defenddmgg')
            imagebutton: #Magic Attack Button
                idle "battlemode/magic_up.png"
                hover "battlemode/magic_down.png"
                action If(numturns >2, Call('magicdmgg'), None)
            imagebutton: #Beserk Button
                idle "battlemode/beast_up.png"
                hover "battlemode/beast_down.png"
                action If(numturns>10 or numjewels==3, Call('zerker'), None)
            imagebutton: #Heal Button
                idle "battlemode/heal_up.png"
                hover "battlemode/heal_down.png"
                action If(numjewels >=1, Call('healdmgg'), None)


#Start Battle Here
label battlebutler:
    $numturns = 20 #This is for debugging. Remember to turn this off!!
    $bosshp = 120
    $bossmaxhp = 120
    $turnnum = 0 #To determine whose turn it is
    #Set up variables for the upcoming battle
    $bossatk = 8 #Butler has weaker attack base than witch
    $redatk = 10
    $beastmode = False #To keep track of damages in beast mode
    $showwincond = False #Keep track of whether or not we've seen the win condition
    $quick_menu = False
    #Puppets
    $puppetnum = 0
    $pupone = False
    $puptwo = False
    $pupthree= False
    $pupfour = False

    window hide

    #First place the enemy sprite in front of us
    show battleb full at top

    #While we have turns, go through the battleui
    while numturns>0 and bosshp>0 and hp>0:
        #Change the Sprite accordingly
        show battleb full at top
        if bosshp<=40:
            show battleb half at top
        if bosshp<=20:
            show battleb no at top

        #Checks happen here before we start the battles
        #If butler's HP is 0, go straight to winning stance
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
        call screen battleuigreen
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

    #If butler's HP is 0, go straight to winning stance
    if bosshp <1 and showwincond==False:
        $showwincond = True
        jump wincondition
        return

    #if we have ran out of turns, go straight to game over
    if numturns<1 and bosshp>0:
        jump turngameover
        return
    return

label attackdmgg:
    $ butdef = renpy.random.randint(1,10)
    if butdef >=7: #There's 30% chance she'll defend
        call butdef
    $bosshp -= redatk
    show scratch:
        xalign 0.5 yalign 0.3
    "You did [redatk] damage!"
    hide scratch
    #If butler's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if butdef <7: #There's 70% chance she'll attack
        call butturn
    return

label defenddmgg:
    show shield:
        xalign 0.5 yalign 0.3
    "You brace for impact. Damage taken is reduced."
    hide shield
    $bossatk = bossatk*0.5
    call butturn
    return

label magicdmgg:
    $ butdef = renpy.random.randint(1,10)
    if butdef >=6: #There's 40% chance she'll defend
        call butdef
    $numturns-=2
    $redatk = redatk * 1.5
    show torchitall:
        xalign 0.5 yalign 0.3
    "By using 3 energy, you fire a magic spell that does [redatk] damage."
    hide torchitall
    $bosshp -= redatk
    #If butler's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if butdef <6: #There's 60% chance she'll attack
        call butturn
    return

label healdmgg:
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
    call butturn
    return

label butdef:
    "The butler braces for impact. Your attack does less damage."
    $redatk = redatk*0.8 #Reduce Red's attack to 8
    return

label butturn:
    show battleb full at top
    if bosshp<=40:
        show battleb half at top
    if bosshp<=20:
        show battleb no at top
    #Now we do some puppet magic
    if puppetnum<5 and bosshp>10:
        $bosshp-=10 #For 10 of Boss's HP, create puppets
        show battlepuppet1:
            xalign 0 yalign 0.3
        $pupone = True
        $puppetnum += 1
        show battlepuppet2:
            xalign 0.3 yalign 0.3
        $puptwo = True
        $puppetnum += 1
        show battlepuppet3:
            xalign 0.7 yalign 0.3
        $pupthree = True
        $puppetnum += 1
        show battlepuppet4:
            xalign 1.0 yalign 0.3
        $pupfour = True
        $puppetnum += 1

    #Then he attacks normally
    "The enemy does [bossatk] damage."
    with vpunch
    $hp-=bossatk
    return

return
