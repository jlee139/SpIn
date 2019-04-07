transform disappeardeath:
    xalign 0.5
    yalign 0.5
    alpha 1
    parallel:
        linear 1.0 yoffset -100
    parallel:
        linear 1.0 alpha 0

transform celebrationchest:
    xalign 0.5
    yalign 0.3
    alpha 0
    parallel:
        linear 1.0 yoffset 100
    parallel:
        linear 1.0 alpha 1

screen huntmodeset():
    grid 4 3:
        xalign 0.5
        yalign 0.2
        spacing 10
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt1 == True, [SetVariable("butt1", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt2 == True, [SetVariable("butt2", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt3 == True, [SetVariable("butt3", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt4 == True, [SetVariable("butt4", False), Call('calcperct')], None)

        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt5 == True, [SetVariable("butt5", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt6 == True, [SetVariable("butt6", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt7 == True, [SetVariable("butt7", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt8 == True, [SetVariable("butt8", False), Call('calcperct')], None)

        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt9 == True, [SetVariable("butt9", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt10 == True, [SetVariable("butt10", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
            action If(butt11 == True, [SetVariable("butt11", False), Call('calcperct')], None)
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            insensitive "huntmode/selectarea_none.png"
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
    nvlmc "You found [numwisps] wisp(s). That gives you [numwisps] turn(s)."
    $calcghost = numghosts*2
    nvlmc "You found [numghosts] ghost(s). That gives you [calcghost] more turn(s)."
    $calcskele = numskele*5
    nvlmc "You found [numskele] skeleton(s). That gives you [calcskele] more turn(s)."
    $calcchest = numchests*10
    nvlmc "You found [numchests] chest(s). That gives you [calcchest] more turn(s)."
    $numturns = numwisps + calcghost + calcskele+calcchest
    nvlmc "You have total of [numturns] turns for the upcoming battle."

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

    call huntmode

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
        scene black
        show wispdis at disappeardeath
        "You found a wisp!"
    elif  randchance <80:
        #You found a ghost
        $numghosts+=1
        scene black
        show ghostdis at disappeardeath
        "You found a ghost!"
    elif  randchance <=98:
        #You found a skeleton
        $numskele+=1
        scene black
        show skeledis at disappeardeath
        "You found a skeleton!"
    elif  randchance >98:
        #You found a chest!
        $numchests+=1
        scene black
        show chestfound at celebrationchest
        "You found a chest!"

    $numoftries -=1
    return
