transform disappeardeath:
    xalign 0.5
    yalign 0.5
    alpha 1
    parallel:
        linear 0.8 yoffset -60
    parallel:
        linear 0.8 alpha 0
    yoffset +60

transform celebrationchest:
    xalign 0.5
    yalign 0.3
    alpha 0
    parallel:
        linear 0.8 yoffset 100
    parallel:
        linear 0.8 alpha 1
    linear 0.3 alpha 0

screen huntmodeset():
    grid 4 3:
        xalign 0.5
        yalign 0.2
        spacing 10
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt1 == True, [SetVariable("butt1", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt2 == True, [SetVariable("butt2", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt3 == True, [SetVariable("butt3", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt4 == True, [SetVariable("butt4", False), Call('calcperct')], None)

        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt5 == True, [SetVariable("butt5", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt6 == True, [SetVariable("butt6", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt7 == True, [SetVariable("butt7", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt8 == True, [SetVariable("butt8", False), Call('calcperct')], None)

        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt9 == True, [SetVariable("butt9", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt10 == True, [SetVariable("butt10", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt11 == True, [SetVariable("butt11", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            hover_sound "sfx/click2.mp3"
            activate_sound "sfx/menu-selection-click.mp3"
            action If(butt12 == True, [SetVariable("butt12", False), Call('calcperct')], None)

    frame:
        xpadding 10
        ypadding 10
        xminimum 950
        xalign 0.5
        yalign 0.95
        hbox:
            spacing 50
            vbox:
                text "You found [numwisps] wisp(s)."
                text "You found [numghosts] ghost(s)."
                text "You found [numskele] skeleton(s)."
                text "You found [numchests] chest(s)."

label endhuntreport:
    hide screen huntmodeset
    scene black

    #nvl set up
    nvl clear
    window show

    nvlmc "Your Progress Report:"
    nvlmc "You found [numwisps] wisp(s). That gives you [numwisps] energy."
    $calcghost = numghosts*2
    nvlmc "You found [numghosts] ghost(s). That gives you [calcghost] more energy."
    $calcskele = numskele*5
    nvlmc "You found [numskele] skeleton(s). That gives you [calcskele] more energy."
    $calcchest = numchests*10
    nvlmc "You found [numchests] chest(s). That gives you [calcchest] more energy."
    $numturns = numwisps + calcghost + calcskele+calcchest

    #If we have multiple Orbs, give us a boost in energy
    if numOrb > 0:
        $numturns = numturns+numturns
        if orblangchange:
            nvlmc "You draw upon the magic of the crushed orb in the air, giving you a boost in power. You may not know what this is, but it sure is convenient."
        else:
            nvlmc "The orb in your pocket glows, giving you a boost in power. No seriously, what is this thing?"

    nvlmc "You have total of [numturns] energy for the upcoming battle."

    #escape nvl mode
    nvl clear
    window hide
    $quick_menu = True
    return


label huntmodestart:
    $numghosts = 0
    $numwisps = 0
    $numskele = 0
    $numchests =0
    $numoftries = 12
    $quick_menu = False
    window hide

    $butt1 = True
    $butt2 = True
    $butt3 = True
    $butt4 = True
    $butt5 = True
    $butt6 = True
    $butt7 = True
    $butt8 = True
    $butt9 = True
    $butt10 = True
    $butt11 = True
    $butt12 = True

    call huntmode from _call_huntmode

label huntmode:
    while numoftries >0:
        call screen huntmodeset
    if numoftries==0:
        $numoftries -=1
        jump endhuntreport
    return

label calcperct:
    #Do a random number generator
    $randchance = renpy.random.randint(0, 100)

    if randchance <40:
        #You found wisp
        $numwisps+=1
        #scene black
        play audio "sfx/collect.mp3"
        show wispdis at disappeardeath
        "You found a wisp!"
    elif  randchance <80:
        #You found a ghost
        $numghosts+=1
        #scene black
        play audio "sfx/collect.mp3"
        show ghostdis at disappeardeath
        "You found a ghost!"
    elif  randchance <=98:
        #You found a skeleton
        $numskele+=1
        #scene black
        play audio "sfx/collect.mp3"
        show skeledis at disappeardeath
        "You found a skeleton!"
    elif  randchance >98:
        #You found a chest!
        $numchests+=1
        #scene black
        play audio "sfx/jingle-achievement-00.mp3"
        show chestfound at celebrationchest
        "You found a chest!"

    $numoftries -=1
    return
