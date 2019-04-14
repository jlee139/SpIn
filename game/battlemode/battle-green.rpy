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
    if bosshp<=20:
        #There's 100% chance he'll defend
        call butdef
    elif  bosshp<=40:
        if butdef >=5: #There's 50% chance he'll defend
            call butdef
    else:
        if butdef >=9: #There's 10% chance he'll defend
            call butdef
    #Ask which one to attack
    if puppetnum>0:
        menu:
            "Who should I attack?"
            "Attack the first Puppet" if pupone:
                show scratch:
                    xalign 0.0 yalign 0.5
                "You attacked the first puppet."
                hide scratch
                hide battlepuppet1
                $puppetnum -=1
                $pupone = False
            "Attack the second Puppet" if puptwo:
                show scratch:
                    xalign 0.3 yalign 0.5
                "You attacked the second puppet."
                hide scratch
                hide battlepuppet2
                $puppetnum -=1
                $puptwo = False
            "Attack the third Puppet" if pupthree:
                show scratch:
                    xalign 0.7 yalign 0.5
                "You attacked the third puppet."
                hide scratch
                hide battlepuppet3
                $puppetnum -=1
                $pupthree = False
            "Attack the fourth Puppet" if pupfour:
                show scratch:
                    xalign 1.0 yalign 0.5
                "You attacked the fourth puppet."
                hide scratch
                hide battlepuppet4
                $puppetnum -=1
                $pupfour = False
            "Attack the Butler":
                show scratch:
                    xalign 0.5 yalign 0.2
                "You did [redatk] damage to the Butler!"
                hide scratch
                $bosshp -= redatk
            "Nevermind.":
                $numturns +=1
                return
    else:
        show scratch:
            xalign 0.5 yalign 0.2
        "You did [redatk] damage to the Butler!"
        hide scratch
        $bosshp -= redatk

    #If butler's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition

    if bosshp<=20:
        #There's 100% chance he'll defend
        pass
    elif  bosshp<=40:
        if butdef <5: #There's 50% chance he'll defend
            call butturn
    else:
        if butdef <9: #There's 10% chance he'll defend
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
    if bosshp<=20:
        #There's 100% chance he'll defend
        call butdef
    elif  bosshp<=40:
        if butdef >=5: #There's 50% chance he'll defend
            call butdef
    else:
        if butdef >=9: #There's 10% chance he'll defend
            call butdef
    #First decide if we're doing AOE or ST
    if puppetnum>0:
        menu:
            "Should I hit one target with a strong magic spell? Or hit all of them with a weaker one?"
            "One target with a strong spell.":
                menu:
                    "Who should I attack?"
                    "Attack the first Puppet" if pupone:
                        show torchitall:
                            xalign 0.1 yalign 0.5
                        "You attacked the first puppet."
                        hide torchitall
                        hide battlepuppet1
                        $puppetnum -=1
                        $pupone = False
                    "Attack the second Puppet" if puptwo:
                        show torchitall:
                            xalign 0.34 yalign 0.5
                        "You attacked the second puppet."
                        hide torchitall
                        hide battlepuppet2
                        $puppetnum -=1
                        $puptwo = False
                    "Attack the third Puppet" if pupthree:
                        show torchitall:
                            xalign 0.65 yalign 0.5
                        "You attacked the third puppet."
                        hide torchitall
                        hide battlepuppet3
                        $puppetnum -=1
                        $pupthree = False
                    "Attack the fourth Puppet" if pupfour:
                        show torchitall:
                            xalign 0.9 yalign 0.5
                        "You attacked the fourth puppet."
                        hide torchitall
                        hide battlepuppet4
                        $puppetnum -=1
                        $pupfour = False
                    "Attack the Butler":
                        $numturns-=2
                        $redatk = redatk * 1.5
                        show torchitall:
                            xalign 0.5 yalign 0.2
                        "By using 3 energy, you fire a magic spell that does [redatk] damage."
                        hide torchitall
                        $bosshp -= redatk
            "All of them with a weaker one.":
                if pupone:
                    show torchitall:
                        xalign 0.1 yalign 0.5
                    pause 0.5
                    hide torchitall
                    hide battlepuppet1
                    $puppetnum -=1
                    $pupone = False
                if puptwo:
                    show torchitall:
                        xalign 0.34 yalign 0.5
                    pause 0.5
                    hide torchitall
                    hide battlepuppet2
                    $puppetnum -=1
                    $puptwo = False
                if pupthree:
                    show torchitall:
                        xalign 0.65 yalign 0.5
                    pause 0.5
                    hide torchitall
                    hide battlepuppet3
                    $puppetnum -=1
                    $pupthree = False
                if pupfour:
                    show torchitall:
                        xalign 0.9 yalign 0.5
                    pause 0.5
                    hide torchitall
                    hide battlepuppet4
                    $puppetnum -=1
                    $pupfour = False
                #If butler
                $numturns-=2
                $redatk = redatk * 0.8
                show torchitall:
                    xalign 0.5 yalign 0.2
                "By using 3 energy, you fire a magic spell that does [redatk] damage to all targets."
                hide torchitall
                $bosshp -= redatk
            "Nevermind.":
                $numturns +=2
                return
    else:
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

    if bosshp<=20:
        #There's 100% chance he'll defend
        pass
    elif  bosshp<=40:
        if butdef <5: #There's 50% chance he'll defend
            call butturn
    else:
        if butdef <9: #There's 10% chance he'll defend
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
    "The Butler braces for impact. Your attack does less damage."
    $redatk = redatk*0.8 #Reduce Red's attack to 8
    return

label butturn:
    show battleb full at top
    if bosshp<=40:
        show battleb half at top
    if bosshp<=20:
        show battleb no at top
    #Now we do some puppet magic
    if puppetnum<4 and bosshp>10:
        $bosshp-=10 #For 10 of Boss's HP, create puppets
        "The Butler exchanged his health to create puppets! These puppets are flimsy enough that one hit should destroy them."
        if pupone == False:
            show battlepuppet1:
                xalign 0 yalign 0.3
            $pupone = True
            $puppetnum += 1
        if puptwo == False:
            show battlepuppet2:
                xalign 0.3 yalign 0.3
            $puptwo = True
            $puppetnum += 1
        if pupthree == False:
            show battlepuppet3:
                xalign 0.7 yalign 0.3
            $pupthree = True
            $puppetnum += 1
        if pupfour == False:
            show battlepuppet4:
                xalign 1.0 yalign 0.3
            $pupfour = True
            $puppetnum += 1

    #Then he attacks normally with the puppets
    "The Butler does [bossatk] damage. The puppets each does 2 damage."
    with vpunch
    $hp-=bossatk
    $hp-=8
    return

return
