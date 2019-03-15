# The script of the game goes in this file.

# The game starts here.
label start:

    #First thing first, get the Player's name
    #$ mcname = renpy.input("Enter your name")

    #Then We start the story!
    #call prologue      #Start us up with the prologue of the story
    call firstfloor    #After the prologue, we go to the first floor
    #call secondfloor   #Then the 2nd floor
    #call thirdfloor    #Then the 3rd floor

    #Tada! Story is done!

    #Debugging Things:
    #call shootfix #Testing our shooter
    #call begin_TutRPG #Testing our Battle Mode
    #jump firstfloorcont #for debugging

    "That's the end of the Tutorial. Thank you!"


# This ends the game.
return
