# The script of the game goes in this file.

# The game starts here.
label start:
    #Then We start the story!
    #call prologue      #Start us up with the prologue of the story


    #Debugging each chapter
    #call firstfloor    #After the prologue, we go to the first floor
    #call secondfloor   #Then the 2nd floor
    #call thirdfloor    #Then the 3rd floor

    #Tada! Story is done!

    #Debugging Things:
    scene bg greenroom with fade
    show particleFog1:
        alpha 0.8
    window hide
    #call huntmodestart #Testing our hunt mode
    #call shootfix #Testing our hunt mode
    call battlebutler #Testing our Battle Mode
    #jump breakpoint #for debugging

    #scene black
    #"That's the end of the demo. Thank you!"


# This ends the game.
return
