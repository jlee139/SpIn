#Our First Mini Fight Against the Witch
screen battleuifinal2():
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
                hover_sound "sfx/click2.mp3"
                activate_sound "sfx/menu-selection-click.mp3"
                action Call('attackdmgff2')
            imagebutton: #Defend Button
                idle "battlemode/defend_up.png"
                hover "battlemode/defend_down.png"
                hover_sound "sfx/click2.mp3"
                activate_sound "sfx/menu-selection-click.mp3"
                action Call('defenddmgff2')
            imagebutton: #Magic Attack Button
                idle "battlemode/magic_up.png"
                hover "battlemode/magic_down.png"
                hover_sound "sfx/click2.mp3"
                activate_sound "sfx/menu-selection-click.mp3"
                action If(numturns >2, Call('magicdmgff2'), None)
            imagebutton: #Beserk Button
                idle "battlemode/beast_up.png"
                hover "battlemode/beast_down.png"
                hover_sound "sfx/click2.mp3"
                activate_sound "sfx/menu-selection-click.mp3"
                action If(numturns>20 or numjewels==3, Call('zerker'), None)
            imagebutton: #Heal Button
                idle "battlemode/heal_up.png"
                hover "battlemode/heal_down.png"
                hover_sound "sfx/click2.mp3"
                activate_sound "sfx/menu-selection-click.mp3"
                action If(numjewels >=1, Call('healdmg'), None)


#Start Battle Here
label finalfight2:
#    $numturns = 20 #This is for debugging. Remember to turn this off!!
    $turnnum = 0 #To determine whose turn it is
    #Set up variables for the upcoming battle
    $bossatk = 10
    $redatk = 10
    $beastmode = False #To keep track of damages in beast mode
    $showwincond = False #Keep track of whether or not we've seen the win condition
    $quick_menu = False

    window hide

    #First place the enemy sprite in front of us
    if bosshp<=650:
        show battlew half at top
    else:
        show battlew full at top

    #While we have turns, go through the battleui
    while numturns>0 and bosshp>0 and hp>0:
        #Change the Sprite accordingly
        if bosshp<=650:
            show battlew half at top
        else:
            show battlew full at top

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
        call screen battleuifinal2
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

    #if we have ran out of turns...
    if numturns<1 and bosshp>0:
        jump outtaturn2
        return
    return

label attackdmgff2:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=5: #There's 50% chance she'll defend
        call witchdef
    $bosshp -= redatk
    play audio "sfx/metal-sound-fighting-game.mp3"
    show scratch:
        xalign 0.5 yalign 0.3
    "You did [redatk] damage!"
    hide scratch
    #If witch's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if witchdef <5: #There's 50% chance she'll attack
        call witchturn2
    return

label defenddmgff2:
    play audio "sfx/another-magic-wand-spell-tinkle.mp3"
    show shield:
        xalign 0.5 yalign 0.3
    "You brace for impact. Damage taken is reduced."
    hide shield
    $bossatk = bossatk*0.5
    call witchturn2
    return

label magicdmgff2:
    $ witchdef = renpy.random.randint(1,10)
    if witchdef >=5: #There's 5% chance she'll defend
        call witchdef
    $numturns-=2
    $redatk = redatk * 1.5
    play audio "sfx/fire-crackle-and-flames-002.mp3"
    show torchitall:
        xalign 0.5 yalign 0.3
    "By using 3 energy, you fire a magic spell that does [redatk] damage."
    hide torchitall
    $bosshp -= redatk
    #If witch's HP is 0, go straight to winning stance
    if bosshp <1:
        jump wincondition
    if witchdef <5: #There's 50% chance she'll attack
        call witchturn2
    return

label witchturn2:
    if bosshp<=650:
        show battlew half at top
    else:
        show battlew full at top
    $ witchmagic = renpy.random.randint(1,10)
    if witchmagic >=4: #There's 60% chance she'll use magic
        $bossatk = bossatk*1.5
        "The witch fires a magic spell that does [bossatk] damage."
        play audio "sfx/sword-thud.mp3"
        with vpunch
        $hp-=bossatk
    else:
        "The witch does [bossatk] damage."
        play audio "sfx/thud.mp3"
        with vpunch
        $hp-=bossatk
    return

menu outtaturn2:
    "You have ran out of erengy."
    "Give up.":
        jump turngameover
    "Keep fighting.":
        jump retfinalfight2

return
