# The script of the game goes in this file.

# The game starts here.
label start:

    #First thing first, get the Player's name
    #$ mcname = renpy.input("Enter your name")

    #Then We start the story!
    #call prologue      #Start us up with the prologue of the story


    #Debugging each chapter
    #call firstfloor    #After the prologue, we go to the first floor
    #call secondfloor   #Then the 2nd floor
    #call thirdfloor    #Then the 3rd floor

    #Tada! Story is done!

    #Debugging Things:
    scene bg fronthall with fade
    window hide
    #call huntmodestart #Testing our hunt mode
    #call shootfix #Testing our hunt mode
    #call begin_TutRPG #Testing our Battle Mode
    #jump introToWitch #for debugging


    #Rando Scenes to Test our Quick Menus
    show g temp at right with dissolve
    green "By the way, Rookie, you know that the whole 'SpIn' thing is a joke, right? No one actually calls us that."
    show r temp at center with dissolve
    rookie "... I... was not aware."
    show bl temp at left with dissolve
    blue "How many times do I have to tell you to stop confusing people? It's not a joke. SpIn is silly sounding, but it is still our name."

    nvl clear
    window show

    nvlmc "On one such mission, we were interrupted by a witch. Since what we were taking care of at the time was time sensitive, we decided to ignore that witch for the time being to complete the mission."
    nvlmc "That was our mistake."

    window hide



    scene black
    #"That's the end of the demo. Thank you!"


# This ends the game.
return
