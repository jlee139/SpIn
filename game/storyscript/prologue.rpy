label prologue:
    #nvl set up
    nvl clear
    window hide
    scene bg office memory with fade
    window show

    nvlmc "Of all the things in the world, I probably miss his laugh the most."
    nvlmc "Despite not being that much older than me, he'd always laugh and ruffle my hair like I was still a child. And perhaps in his eyes, I was."
    nvlmc "\"Did you fall asleep here again?\" he'd say every time he found me on the couch. \"Isn't it uncomfortable? You don't have to wait for me in the office.\""
    nvlmc "It's possible that since asking me to join his Supernatural Investigation Office, he never once considered that I had nowhere else to go but here. That I had nowhere but by his side to call home."
    nvlmc "\"I don't mind,\" I'd say instead."
    nvlmc "He would always laugh at those words while ruffling my hair. Like he was rewarding a dog or a child. I both loved and hated him in the same breath."
    nvlmc "\"Want me to leave a blanket here for you?\""

    nvl clear

    nvlmc "…"
    nvlmc "Those days are long gone now."
    nvlmc "And some things are precious because you can't ever get them back."

    #escape nvl mode
    nvl clear
    window hide

    #Now we get to the main cast
    scene bg mansionout with fade

    show g temp at right with dissolve
    green "So this is the place? It definitely looks right. Yeesh, look at that. Looks like something straight out of a clichéd horror flick."
    show bl temp at left with dissolve
    blue "Of course, it looks like that. It's been abandoned for the better part of the century."
    show r temp at center with dissolve
    rookie "Careful. This area is rocky, [mcname]-"
    green "Hey! How many times do we have to say to use code names? You want to be cursed?"
    rookie "Sorry. I am still not used to this."

    menu:
        "Thanks for watching out for me."
        "Offer to reiterate code names":
            show allappsprite
            #show rookieapprove at appsprite
            $ rookieap+= 1
            "If you want, we can go over everyone's code names again. I'm Red."
        "Gently but firmly reiterate the importance of code names":
            show blueapprove at appsprite
            $ blueap+= 1
            "Don't forget that these code names exist to protect us. Until this mission is over, I'm Red."
        "Get annoyed":
            show greenapprove at appsprite
            $ greenap+= 1
            "Until we get back, remember that I'm Red. And you, stop laughing! You couldn't keep the code names straight on your first mission."

    green "I'm Green. In case you couldn't tell from my hair."
    blue "Don't be a jackass. I'm Blue. Do you remember your code name?"
    rookie "Yes. It is Pur-"
    green "Rookie. You haven't earned your color yet. Until you can prove yourself, you'll be Rookie."
    rookie "..."
    green "What? Got a problem with it?"
    "Don't mind him. He's just cranky because he's threatened by your presence."
    green "Don't tell him misleading things! Listen here, Rookie. Our job as Supernatural Investigator is dangerous. One wrong move and we can die or worse, end up cursed. The easiest way to get cursed is by handing your name over carelessly."
    "Oh wow. You actually sound smart for once!"
    blue "He's just paraphrasing everything I told him. How is that impressive?"
    "But look, it actually sunk in this time. You only told him that for every mission we went on."
    rookie "Have you guys been together long?"

    menu:
        "(Together, huh? What a sore topic to ask.)"
        "Reassure him":
            show rookieapprove at appsprite
            $ rookieap+= 1
            "Don't worry. You'll fit in in no time."
            rookie "I see."
            "(He got really quiet. Did I say the wrong thing?)"
        "Dodge the question":
            show greenapprove at appsprite
            $ greenap+= 1
            "I guess? I don't really remember."
            green "Maybe you should stop getting hit on the head so often, eh?"
            "No one asked you!"
        "Answer what you can":
            show blueapprove at appsprite
            $ blueap+= 1
            "Something like that. It's been what? Two years for the three of us?"
            blue "Nearly two years. Three more months, and it'll be our anni."
            "(He looks way too happy. I hope he's not planning on baking...)"
        "Answer honestly" if trueend:
            $ bossap+= 1
            "About two years with these guys. But before that, I worked together with the former Red. Ah, you'll probably recognize his name as 'Boss.'"
            rookie "Is that...?"
            blue "If you're thinking the one who recruited most of us and formed our Supernatural Invesgitation group by giving it the silly name of 'SpIn,' you are correct."
            rookie "I don't think I've met him."
            green "..."
            blue "..."
            rookie "?"
            "You'll meet him later."
            green "Red, you..."
            "Rookie will meet him later."

    blue "Now then, do we need to go over what the mission is?"
    green "Hey, why're you looking at me for?!"
    "Don't know. Why're you such an idiot?"
    green "Why you-"
    rookie "It's to investigate this mansion and to rid of any malicious spirits residing here."
    blue "At least one of you were paying attention to the briefing. Here, have a candy."
    "You're not that much older than us. Stop treating us like children."
    green "That's not fair! I want candy!"
    blue "As you were saying, Red?"
    "... Are we going to be okay with this mission...?"

    if trueend:
        scene bg office memory with fade

        boss "Hahahaha! Relax a bit, Red! If you're that tense, you'll end up hurting yourself."
        "Your code name is Red! That's your name! How many times do I have to tell that to you?!"
        boss "T-that was a joke! Don't be mad! I was trying to make you laugh."
        "A joke should be funny. You have zero tact!"
        boss "Don't be like that! C'mon, just smile a little for me? Please, Silver?"
        "My code name is Gray! You came up with it!"
        boss "I'm telling you, it's a joke!"

        #turn nvl back on
        window show
        nvlmc "That's right. It's always been lively like this, hasn't it? Even when it was just him and me."
        nvlmc "We struggled a lot back then. Not just because he's an idiot, but also because I had no patience for his jokes. Thinking back on it now, we caused more trouble than we solved them. It's a miracle that our SpIn even managed to last this long."
        nvlmc "But I suppose that's also part of his charms."
        nvlmc "The former Red was someone completely unforgettable."
        nvlmc "That's why, no matter what, I will succeed."

        #end nvl
        nvl clear
        window hide

jump firstfloor #After this, go to the first chapter
#return #Return to story
