transform disappeardeath:
    xalign 0.5
    yalign 0.5
    alpha 1
    parallel:
        linear 0.3 yoffset -100
    parallel:
        linear 0.3 alpha 0

screen huntmodeset():
    grid 4 3:
        xalign 0.5
        yalign 0.2
        spacing 10
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')

        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')

        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')
        imagebutton:
            idle "huntmode/selectarea.png"
            hover "huntmode/selectarea-hover.png"
            action Call('calcperct')

    frame:
        xpadding 10
        ypadding 10
        xminimum 950
        xalign 0.5
        yalign 0.95
        hbox:
            spacing 50
            vbox:
                text "[numoftries] tries left."
            vbox:
                text "You have found [numwisps] wisp(s)."
                text "You have found [numghosts] ghost(s)."
                text "You have found [numskele] skeleton(s)."
                text "You have found [numchests] chest(s)."

label endhuntreport:
    hide screen huntmodeset
    scene black

    #nvl set up
    nvl clear
    window show

    nvlmc "Your Progress Report:"
    nvlmc "You found [numwisps] wisp(s)."
    nvlmc "You found [numghosts] ghost(s)."
    nvlmc "You found [numskele] skeleton(s)."
    nvlmc "You found [numchests] chest(s)."

    #escape nvl mode
    nvl clear
    window hide
    return


label huntmodestart:
    $numghosts = 0
    $numwisps = 0
    $numskele = 0
    $numchests =0
    $numoftries = 12
    window hide

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
        "You have found a wisp!"
    elif  randchance <70:
        #You found a ghost
        $numghosts+=1
        scene black
        show ghostdis at disappeardeath
        "You have found a ghost!"
    elif  randchance <=98:
        #You found a skeleton
        $numskele+=1
        scene black
        show skeledis at disappeardeath
        "You have found a skeleton!"
    elif  randchance >98:
        #You found a chest!
        $numchests+=1
        scene black
        "You have found a chest!"

    $numoftries -=1
    return
