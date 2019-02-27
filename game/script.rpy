# The script of the game goes in this file.

# The game starts here.
label start:
    #jump prologue   #Start us up with the prologue of the story

    call begin_hunt #Testing our shooter
    #jump entermansion #for debugging

label prologue:
    #nvl set up
    nvl clear
    window hide
    #scene bg office with fade
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
    #scene bg outsidemansion with fade

    #show green grin at right with dissolve
    green "So this is the place? It definitely looks right. Yeesh, look at that. Looks like something straight out of a clichéd horror flick."
    #show blue matteroffact at left with dissolve
    blue "Of course, it looks like that. It’s been abandoned for the better part of the century."
    #show rookie neutral at center with dissolve
    rookie "Careful. This area is rocky, El-"
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
    rookie "It’s to investigate this mansion and the rumors of a witch that lives here."
    blue "At least one of you were paying attention to the briefing. Here, have a candy."
    "You’re not that much older than us. Stop treating us like children."
    green "That's not fair! I want candy!"
    blue "As you were saying, Red?"
    "... Are we going to be okay with this mission...?"

    if trueend:
        boss "Hahahaha! Relax a bit, Red! If you’re that tense, you’ll end up hurting yourself."
        "Your code name is Red! That’s your name! How many times do I have to tell that to you?!"
        boss "T-that was a joke! Don’t be mad! I was just trying to make you laugh."
        "A joke should be funny. You have zero tact!"
        boss "Don’t be like that! C’mon, just smile a little for me?"

        #turn nvl back on
        window show
        nvlmc "That’s right. It has always been lively like this, hasn’t it? Even before these guys all joined. When it was just him and me."
        nvlmc "We struggled a lot back then. I had no patience for his jokes due to the situation at hand."
        nvlmc "I wonder if that made him sad. But surely even he understood how dangerous what we were doing was? The fact that he wanted to laugh frustrated me often."
        nvlmc "Things got easier once we met the others. But getting to that point was a slow and painful process."
        nvlmc "I wonder if he would have been happier if I smiled once in a while back then..."

        #end nvl
        nvl clear
        window hide

#Should allow to skip to this
label firstfloor: #set up of the rest of the story
    #nvl set up
    #scene mansionentrance with fade
    window show
    nvlmc "There is no door to the mansion for us to open. Where the door should be is a tattered cloth that might have once been a curtain."
    nvlmc "The entrance way creak under our weights. I don't feel any wind, but the makeshift curtain seems to be swaying."
    nvlmc "What a creepy automosphere."
    nvl clear
    nvlmc "According to Blue's research, this place was abandoned due to rumors of it being haunted. Many ambitious owners have tried in the past to restore it to glory but gave up due to \"ghostly activities.\""
    nvlmc "A ghost, in our profession, could mean any number of things. "
    nvlmc "A strong enough feeling left behind by those who lived here previously."
    nvlmc "A leftover from a curse or a spell that behaves, in all intent and purposes, like a ghost."
    nvlmc "Someone’s lingering spirit that was unable to pass on."
    nvlmc "The way you deal with lingering spirits is the hardest out of the three, which is why we came here prepared for the last option."
    nvl clear
    nvlmc "Green lights up his cigarette. He takes a moment to breathe in deeply before he slowly lets it out. Thick smoke surrounds us within seconds. "
    nvlmc "This is the part that I hate the most about Green’s ability. It’s bad enough that the smoke reduces visibility, but it also smells bad, too. But this is for the sake of our safety. Yet another precaution we take on top of our code names."
    nvlmc "Each of us have a special ability that makes us viable Supernatural Investigators. "
    nvlmc "Green’s ability is to turn a small area around himself into his \"Zone.\" He doesn’t need to smoke to mark that area, but he likes to give us a physical representation of where it is. He can detect any outside influences the minute they enter his Zone, and to an extent limit the outsiders’ abilities."
    nvl clear
    #Run this part if this is our first runthrough
    if endingct<1:
        nvlmc "My ability isn’t anything much. At the very least, it won’t be able to do much right now. It’s a bit vexing, but I suppose I can show off some other time."
    #Otherwise, run this
    else:
        nvlmc "Once Green gives us the clear and Blue sets up a seal, I’ll be able to use my ability. It’s been a while since I’ve been able to do this. I wonder if you can get rusty from not using it."
    #Now back to our regular program
    nvlmc "Whatever. It’s not like I need my ability to get through missions."
    nvlmc "Unlike the others, I wasn’t recruited because of it. I can hold my own without extra help. Granted, that’s also because my previous partner struggled to function normally, so I just learned to take care of myself without relying on anything."
    nvlmc "It also helps that I have a fairy’s blessing in the form of a three-jeweled necklace. As long as I wear this necklace and the jewels shine bright, I’ll be protected from an malicious attack three times."
    nvl clear
    nvlmc "Green finally gives us a nod, signaling that the entrance way is safe. "
    nvlmc "I glance around at the others."

    #end nvl
    nvl clear
    window hide

    #children being cute now
    "Ready?"
    blue "Want a candy? It’ll help you with your nerves."
    green "Don’t tell me you’re getting cold feet? Jeesh, what will we do with you? If you’re like this, how’d you think Rookie here feels?"
    rookie "I feel fine. But if you are in need of rest, I can carry you."

    menu:
        "No to both candy and being carried.":
            jump blue3
        "I think I’m too nervous to be carried or to eat something.":
            jump rookie3
        "I’m fine! Like hell I’m getting cold feet!":
            jump green3

label blue3:
    $ blueap+= 1
    "I’m not nervous. Just wanted to cover my bases."
    blue "Got it. But if you change your mind, I have strawberry flavor."
    jump entermansion

label rookie3:
    $ rookieap+= 1
    "But thank you for offering anyways. I’ll be fine."
    rookie "You push yourself too much."
    jump entermansion

label green3:
    $ greenap+= 1
    "I’ve taken care of harder missions than this plenty of times!"
    green "Hah! I’m sure you have!"
    jump entermansion

label entermansion:
    "Let's go!"

    #nvl set up
    #scene mansionentrance with fade
    window show
    nvlmc "I can see why the previous owners tried so hard to restore the mansion."
    nvlmc "The entrance area is huge. The broken chandelier hanging looks to be one of the newer addition. There’s a spiral staircase against the wall leading up to the second floor. The chandelier looks to be at eye-level with it. Perhaps one of the previous owners broke the ceiling to put the chandelier like that?"
    nvlmc "There appears to be a giant ripped portrait under the staircase. It doesn’t look like there’s a way to go that way. But there are two hallways, one on either side of us, that seems to lead to other parts of the mansion."
    nvlmc "The way to the left looks to lead to a dining area with a long table. The way to the right looks to have been caved in by some kind of rubble. Was it due to the activity of the ghost? Or was this done by construction that was halted eventually?"

    #end nvl
    nvl clear
    window hide

    "It feels like it’s bigger on the inside than out."
    green "I... hate to say this, but it’s too large of an area for my ability to cover."
    blue "I’ll put up a seal."
    rookie "Seal? In this big of an area? Would it be effective?"
    green "Jeesh, and I thought Red here was pretty air-headed. Pay more attention to others’ abilities, won’t you?"
    "Hilarious coming from you. You thought my ability was to make tea!"
    green "Whua-?! How many times do I have to say that it was a joke?"
    blue "Since they’re too distracted to be of help, let me explain. I’m not putting up a protection seal. This seal is meant to be a lock."
    rookie "Ah. I see. To prevent them from leaving, correct? "
    blue "Very good. You’re not a complete lost case. Should I give you a candy as reward?"
    rookie "No thank you. But if the seal prevents them from leaving, does it also keep us in?"
    green "Yup! But it’s not like you were planning on leaving in the middle of a mission, were you?"
    "No need to get nasty."
    "Rookie, don’t worry. No matter how badly things get, I will protect you."
    rookie "...!"
    green "How selfish! You’re seriously going to rely on Red to carry through your first mission?"
    blue "Don’t you still make Red ‘carry’ you?"
    green "Hey! That’s different! I’m the support type! You can’t make someone like me fight!"
    "Whether you can’t fight or you don’t want to, it doesn’t matter. I will make sure that all of you get out alive. That is my promise to you guys for following me here."
    rookie "..."
    "(I can’t tell what kind of expression that’s supposed to be. Is he happy? Is he annoyed? Does he even care about what we’re talking about?)"
    blue "Well, with that established, can you guys shut up so I can put up the seal?"

    menu:
        "Sorry about that!"
        "Green, I want to check out that room.":
            jump cafeteria
        "Rookie, I’m curious about the portrait over there. Come with me?" if endingct>1:
            jump portrait
        "I’ll stay and guard you, Blue." if endingct>1:
            jump stayguard

label cafeteria:
    $ greenap+= 1
    jump firstambushed

label portrait:
    $ rookieap+= 1
    jump firstambushed

label stayguard:
    $ blueap+= 1
    jump firstambushed

label firstambushed:

    # This ends the game.
    return
