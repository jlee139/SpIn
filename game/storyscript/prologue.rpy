label prologue:
    #nvl set up
    nvl clear
    window hide
    scene office memory with fade
    window show

    nvlmc "Of all the things in the world, I probably miss his laugh the most."
    nvlmc "Despite not being that much older than me, he’d always laugh and ruffle my hair like I was still a child. And perhaps in his eyes, I was."
    nvlmc "\"Did you fall asleep here again?\" he’d say every time he found me on the couch. \"Isn’t it uncomfortable? You don’t have to wait for me in the office.\""
    nvlmc "\"I don’t mind,\" I’d say instead."
    nvlmc "He would always laugh at those words while ruffling my hair. Like he was rewarding a dog or a child. I both loved and hated him in the same breath."
    nvlmc "\"Want me to leave a blanket here for you?\""

    nvl clear

    nvlmc "…"
    nvlmc "Those days are long gone now."
    nvlmc "And some things are precious because you can’t ever get them back."

    #escape nvl mode
    nvl clear
    window hide

    #Now we get to the main cast
    scene mansionout with fade

    show greentemp at right with dissolve
    green "So this is the place? It definitely looks right. Yeesh, look at that. Looks like something straight out of a clichéd horror flick."
    show bluetemp at left with dissolve
    blue "Of course, it looks like that. It’s been abandoned for the better part of the century."
    show rookietemp at center with dissolve
    rookie "Careful. This area is rocky, [mcname]-"
    green "Hey! How many times do we have to say to use code names? You want to be cursed?"
    rookie "Sorry. I am still not used to this."

    menu:
        "Thanks for watching out for me."
        "Offer to reiterate code names":
            jump rookie1
        "Gently but firmly reiterate the importance of code names":
            jump blue1
        "Get annoyed":
            jump green1

label rookie1:
    $ rookieap+= 1
    "If you want, we can go over everyone's code names again. I'm Red."
    jump procont

label blue1:
    $ blueap+= 1
    "Don't forget that these code names exist to protect us. Until this mission is over, I'm Red."
    jump procont

label green1:
    $ greenap+= 1
    "Until we get back, remember that I’m Red. And you, stop laughing! You couldn’t keep the code names straight on your first mission."
    jump procont

label procont:
    green "I'm Green. In case you couldn't tell from my jacket."
    blue "Don’t be a jackass. I’m Blue. Do you remember your code name?"
    rookie "Yes. It is Pur-"
    green "Rookie. You haven't earned your color yet. Until you can prove yourself, you'll be Rookie."
    rookie "..."
    green "What? Got a problem with it?"
    "Don't mind him. He's just cranky because he's threatened by your presence."
    green "Don’t tell him misleading things! Listen here, Rookie. Our job as Supernatural Investigator is dangerous. One wrong move and we can die or worse, end up cursed. The easiest way to get cursed is by handing your name over carelessly."
    "Oh wow. You actually sound smart for once!"
    blue "He’s just paraphrasing everything I told him. How is that impressive?"
    "But look, it actually sunk in this time. You’ve only told him that for every mission we went on"
    rookie "Have you guys been together long?"

    menu:
        "Reassure him":
            jump rookie2
        "Dodge the question":
            jump green2
        "Answer what you remember":
            jump blue2
        "Answer honestly" if trueend:
            jump boss1

label rookie2:
    $ rookieap+= 1
    "Something like that. Don't worry. You'll fit in in no time."
    rookie "I see."
    "(He got really quiet. Did I say the wrong thing?)"
    jump contpro2

label green2:
    $ greenap+= 1
    "I guess? I don't really remember."
    green "Maybe you should stop getting hit on the head so often, eh?"
    "No one asked you!"
    jump contpro2

label blue2:
    $ blueap+= 1
    "I think so. My memory's a bit fuzzy on the details, but I think it's nearing five years now?"
    blue "Yes. Nearly five years is correct."
    "(He looks happy about something.)"
    jump contpro2

label boss1:
    $ bossap+= 1
    "About five years with these guys. But before that, I worked together with Boss. He’s the one who recruited me."
    rookie "Is that…?"
    blue "Yup. Both myself and Green here have been recruited by him, too. I think you’re the only one who wasn’t. You haven’t even met him, have you?"
    rookie "I’ve seen him in brief passing."
    green "Ugh. He was such a creep, always laughing like some idiot."
    "Yeah, he laughed a lot, didn’t he?"
    blue "..."
    green "..."
    rookie "?"
    jump contpro2

label contpro2:
    blue "Now that we’ve reiterated the importance of code names, do we need to go over what the mission is?"
    green "Hey, why're you looking at me for?!"
    "Don't know. Why're you such an idiot?"
    green "Why you-"
    rookie "It’s to investigate this mansion and to rid of any malicious spirits residing here."
    blue "At least one of you were paying attention to the briefing. Here, have a candy."
    "You’re not that much older than us. Stop treating us like children."
    green "That's not fair! I want candy!"
    blue "As you were saying, Red?"
    "... Are we going to be okay with this mission...?"

    hide greentemp
    hide bluetemp
    hide rookietemp

    if trueend:
        scene office memory with fade

        boss "Hahahaha! Relax a bit, Red! If you’re that tense, you’ll end up hurting yourself."
        "Your code name is Red! That’s your name! How many times do I have to tell that to you?!"
        boss "T-that was a joke! Don’t be mad! I was just trying to make you laugh."
        "A joke should be funny. You have zero tact!"
        boss "Don’t be like that! C’mon, just smile a little for me? Please, Silver?"
        "My code name is Gray! You came up with it!"
        boss "I'm telling you, it's a joke!"

        #turn nvl back on
        window show
        nvlmc "That’s right. It has always been lively like this, hasn’t it? Even before these guys all joined. When it was just him and me."
        nvlmc "We struggled a lot back then. Not just because he's an idiot, but also because I had no patience for his jokes."
        nvlmc "I wonder if that made him sad. But surely even he understood how dangerous what we were doing was? The fact that he wanted to laugh frustrated me."
        nvlmc "Things got easier once we met the others. But getting to that point was a slow and painful process."
        nvlmc "I wonder if he would have been happier if I smiled once in a while back then..."

        #end nvl
        nvl clear
        window hide


    #Remember to erase this!!!
    #scene black

return #Return to story
