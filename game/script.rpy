# The script of the game goes in this file.

# The game starts here.
label start:
    #jump prologue   #Start us up with the prologue of the story

    call begin_ShootMode #Testing our shooter
    #jump portrait #for debugging

label prologue:
    $ mcname = renpy.input("Enter your name")

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

    if trueend:
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
    green "Ugh. Don’t make me spread my area so thinly. The furthest I can go is to the doorway… Hey, are you listening?!"

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "I ignore him and walk into the dining hall area. After a quick glance around, I turn to Green, who is fuming against the doorway."
    nvlmc "Is he that annoyed that I didn’t acknowledge hearing him?"
    nvlmc "Or maybe it’s just that he’s trying his best to expand his Zone and marking it with smoke, except it’s too thinned out to be of any effect. I probably shouldn’t make fun of him about that, though. He did warn me about this, after all."
    nvlmc "But still, this is a huge place. The fact that Green is able to hold up a Zone this big is quite a feat. He’ll probably get a huge head if I say something like that. "

    #end nvl
    nvl clear
    window hide

    "Hey, you don’t have to move your Zone. Keep it concentrated around Blue."
    green "And if you get ambushed? You’re our best fighter. If you go down, none of us have a chance once Blue’s seal goes up. So shut up and let me do my job."
    "Heh. Surprisingly, even you have a soft side, huh?"
    green "If you’re done looking, then we should leave!"

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "I turn my attention to the rest of the room. "
    nvlmc "There’s a long table stretched in the middle of an elongated room. I’m shocked that it’s still standing, what with some of the legs looking like it’s been gnawed off. There aren’t many chairs around. But when I get near enough, I can smell the rot. Better not get too close."
    nvlmc "It looks like there used to be tapestries on the walls. But there are just torn up pieces of dusty fabric on the walls now. Hm? It looks like there’s something tucked in here. But I can’t quite reach it."
    nvlmc "Despite how the glasses to the windows seem to be shattered at places, it doesn’t feel like there’s much of air getting in here. Is that just part of the haunting? There’s also a lot of dust and signs of spiderwebs. That reminds me, I haven’t cleaned the office in a while..."

    #end nvl
    nvl clear
    window hide

    green "Hey! Get back here now!"
    "Are we being attacked? How many?"
    green "Too many for Rookie and Blue to handle alone. I’ll slow them down. Get going!"

    jump firstambushed

label portrait:
    $ rookieap+= 1

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "The portrait on the wall below the staircase seems to be that of a woman. Her face has been ripped off, but the dress looks like something from the victorian times, dark colors with somber laces and everything else covered."
    nvlmc "I wonder who she was and how she’s related to this mansion. Is she the wife of a previous owner? Will we have to face her spirit? Or maybe someone just thought it fit the mood of the mansion and put it here. Rich people tend to do crazy things like that."
    nvlmc "There looks to be faint marks on the wall that disappear under the frames of the portrait. Is there something behind this?"

    #end nvl
    nvl clear
    window hide

    "Hey, can you help me move the portrait?"
    rookie "Is that why you asked me to come?"
    "Who else can I depend on?"
    rookie "..."
    "(Please, I can’t read your mind. Say something!)"
    rookie "I... I was happy that you asked me."
    "(Did he read my mind…?)"
    rookie "Three years ago..."
    "Huh? Three years ago?"
    rookie "I-it is nothing. I will move this for you."
    "(Is he hiding something?)"

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "Rookie’s ability is to control plants. He insists that he can’t actually control them. Rather, he just asks them for help and they respond. As long as the job gets done, I figure it’s not my business what the distinction is."
    nvlmc "But it’s a pretty cool ability to watch unfold. Because Rookie is always so stoic and quiet, you don’t realize that he’s done anything until the plants respond to him. "
    nvlmc "The mansion is old enough that it must have some weeds growing somewhere hidden. Bright green of small sprouts begin to cover the area by the portrait. There’s a loud groaning sound of old wood. It almost looks like the portrait’s frame has been elaborately decorated by bright green of whatever weed has grown here."
    nvlmc "See? What did I tell you? Pretty cool, right?"
    nvlmc "The giant portrait shudders as the plants surround it and-"

    #end nvl
    nvl clear
    window hide

    show whiteflash zorder 50 with vpunch
    "{i}Skreeeeeeeeeeeeeee!{i}"

    "Tch! Looks like there’s no time for this. Rookie, let the portrait be. We need to focus on protecting Blue."
    rookie "Understood."

    jump firstambushed

label stayguard:
    $ blueap+= 1

    blue "You know you don’t have to stay here with me. If there’s trouble, Green will let you know."
    "Do you want me to leave?"
    blue "No, no. I just… thought you’d rather explore."
    "(It looked like he was going to say something else.)"
    "If I’m bothering you, I can go."
    blue "Now you’re just being petty."
    "What can I say? I’m a petty being."
    blue "I’m sure you are."

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "To be honest, I stayed because I like watching Blue’s ability."
    nvlmc "As stated, Blue can create seals. He mentioned once that it was a leftover from his trainings from when he was trying to become a mage. But he doesn’t really like talking about the past. All I know is that Blue had some disagreement with the people he was with and ended up with us."
    nvlmc "Everyone uses their abilities differently. For Blue, whenever he creates a seal, he calls upon the magic in the air around him. It looks like colorful fireflies are floating around him, so it looks beautiful."
    nvlmc "My own ability is nothing refined like that."
    nvlmc "Probably that’s why I love watching Blue at work the most."

    #end nvl
    nvl clear
    window hide

    blue "You know, it’s hard to focus when you keep staring like that."
    "Eh? I didn’t take you for the shy type, Blue."
    blue "Is that supposed to be a compliment?"
    "Always is!"
    blue "Despite accusing me of treating you like a kid, you’re quite an offender yourself."
    "I don’t treat you like a kid, Blue. At best, you’re more like… "
    blue "Like...?"
    "(That’s funny. I can see my breath? Tch. That means-)"
    green "Sorry to interrupt, but we’re being attacked!"
    "Blue, get that seal up. I’ll deal with this!"

    jump firstambushed

label firstambushed:

    call begin_ShootMode #Our Shoot Mode
    #call battle_mode_Tut #Our Battle Mode Tutorial version




# This ends the game.
return
