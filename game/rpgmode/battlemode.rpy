#RPG Set up
screen battleui():
    text "Jewels: [numjewels]" xpos 20 ypos 10
    #Witch's HP Bar
    bar:
        range bossmaxhp
        value bosshp
        xmaximum 300
        xpos 480 ypos 100

#For Tutorial Battle
label begin_TutRPG:
    $numturns = 20 #This is for debugging. Remember to turn this off!!
    $bosshp = 50
    $bossmaxhp = 100

    #First place the enemy sprite in front of us
    show tutorialwitchfull at truecenter


    #Display our health and numturns
    call screen battleui


    return
