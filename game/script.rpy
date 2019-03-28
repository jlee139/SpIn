# The script of the game goes in this file.

# The game starts here.
label start:

    #First thing first, get the Player's name
    $ mcname = renpy.input("Enter your name")

    #Then We start the story!
    call prologue      #Start us up with the prologue of the story


    #Debugging each chapter
    #call firstfloor    #After the prologue, we go to the first floor
    #call secondfloor   #Then the 2nd floor
    #call thirdfloor    #Then the 3rd floor

    #Tada! Story is done!

    #Debugging Things:
    #call shootfix #Testing our shooter
    scene black
    #call begin_TutRPG #Testing our Battle Mode
    #jump introToWitch #for debugging

    "That's the end of the demo. Thank you!"


# This ends the game.
return
