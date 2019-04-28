label firstfloor: #set up of the rest of the story
    #nvl set up
    scene bg mansionentrance with fade
    window show
    nvlmc "There is no door to the mansion for us to open. Where the door should be is a tattered cloth that might have once been a curtain."
    nvlmc "The entrance way creak under our weights. I don't feel any wind, but the makeshift curtain seems to be swaying."
    nvlmc "What a creepy automosphere."
    nvl clear
    nvlmc "According to Blue's research, this place was abandoned due to rumors of it being haunted. Many ambitious owners have tried in the past to restore it to glory but gave up due to \"ghostly activities.\""
    nvlmc "A ghost, in our profession, could mean any number of things. "
    nvlmc "1, A strong feeling left behind by those who lived here previously."
    nvlmc "2, A leftover from a curse or a spell that behaves, in all intent and purposes, like a ghost."
    nvlmc "Or 3, Someone's lingering spirit that was unable to pass on."
    nvlmc "The way you deal with lingering spirits is the hardest out of the three, which is why we came here prepared for the last option. That said, it's possible that what we're dealing with isn't a ghost at all. We do have contingency plans just in case, of course. But I'm personally rooting for an easy mission for Rookie's first."
    nvl clear
    nvlmc "Green lights up his cigarette. He takes a moment to breathe in deeply before he slowly lets it out. Thick smoke surrounds us within seconds."
    show particleFog1:
        alpha 0.5
    nvlmc "This is the part that I hate the most about Green's ability. It's bad enough that the smoke reduces visibility, but it also smells bad, too. But this is for the sake of our safety. Yet another precaution we take on top of our code names."
    nvlmc "Each of us have a special ability that makes us viable Supernatural Investigators (or as our Boss calls us, 'SpIn')."
    nvlmc "Green's ability is to turn a small area around himself into his \"Zone.\" He doesn't need to smoke to mark that area, but he likes to give us a physical representation of where it is. He can detect any outside influences the minute they enter his Zone, and to an extent limit the outsiders' abilities. He once claimed that he can boost our abilities, too. But I've never felt such a thing."
    nvl clear
    nvlmc "When we Supernatural Investigators were first gathered, there wasn't enough of us to form properly balanced teams. Although it is pretty funny looking back on those days, it was painful to suffer through."
    nvlmc "Probably because of that, we got aggressive in recruiting anyone with an ounce of special ability. Things like being able to see the future, being able to change one's shape, being able to control an element, being able to light a candle from ten feet away... Basic things, complex things, specific things meant for small niches... Anyone."
    nvlmc "Thanks to that, though, we received an extra layer of protection in the form of a necklace blessed by a fairy. Vermillion, the one who crafted it, told us that more so than the necklace, what gives us the protection is the three jewels on it. As long as we carry the jewels, we'll be protected from a malicious attack three times. And with each attack, one of the jewels will shatter."
    nvlmc "I am of the opinion that I won't need it for protection. But with that kind of magic infused in it, I might be able to find other ways to use it."
    nvl clear
    nvlmc "Green finally gives us a nod, signaling that the entrance way is safe to enter. "
    nvlmc "I glance around at the others."

    #end nvl
    nvl clear
    window hide

    #Turn on our fog
    show particleFog1:
        alpha 0.5

    #children being cute now
    advmc "Ready?"
    show bl temp at left with dissolve
    blue "Want a candy? It'll help you with your nerves."
    show g temp at right with dissolve
    green "Don't tell me you're getting cold feet? Jeesh, what will we do with you? If you're like this, how'd you think Rookie here feels?"
    show r temp at center with dissolve
    rookie "I feel fine. But if you are in need of rest, I can carry you."

    menu:
        advmc "(Even Rookie is making fun of me? Just how pathetic do I look?)"
        "No to both candy and being carried.":
            show blueapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ blueap+= 1
            advmc "I'm not nervous. Just wanted to cover my bases."
            blue "Got it. But if you change your mind, I have strawberry flavor."
        "I think I'm too nervous to be carried or to eat something.":
            show rookieapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ rookieap+= 1
            advmc "But thank you for offering anyways. I'll be fine."
            rookie "You push yourself too much."
        "I'm fine! Like hell I'm getting cold feet!":
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            advmc "I've taken care of harder missions than this plenty of times!"
            green "Hah! THat we did!"

    advmc "Let's go!"

    #nvl set up
    scene bg fronthall with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    window show
    nvlmc "I can see why the previous owners tried so hard to restore the mansion."
    nvlmc "The entrance area is huge. The broken chandelier looks to be one of the newer addition. There are spiral staircases against the wall leading up to the second floor. The chandelier looks to be at eye-level with it. If it had been taken better care of, I could see the charm in having living in a place like this."
    nvlmc "There appears to be a giant portrait under the staircase. It doesn't look like there's a way to go that way. But there are two hallways, one on either side of us, that seems to lead to other parts of the mansion."
    nvlmc "The way to the left looks to lead to a dining area with a long table. The way to the right looks to have been caved in by some kind of rubble. Was it due to the activity of the ghosts? Or was this done by construction that was halted eventually?"
    nvlmc "At least it doesn't look like there's a way downstairs. I don't like the idea of going to a basement, only to have the mansion crash down on top of us."

    #end nvl
    nvl clear
    window hide

    "It feels like it's bigger on the inside than out."
    show g temp at right with dissolve
    green "I... hate to say this, but it's too large of an area for my ability to cover."
    show bl temp at left with dissolve
    blue "I'll put up a seal."
    show r temp at center with dissolve
    rookie "Seal? In this big of an area? Would it be effective?"

    green "Jeesh, and I thought Red here was pretty air-headed. Pay more attention to others' abilities, won't you?"
    advmc "Hilarious coming from you. You thought my ability was to make tea!"
    green "Whua-?! How many times do I have to say that it was a joke?"
    blue "Since they're too distracted to be of help, let me explain. I'm not putting up a protection seal. This seal is meant to serve as a prison."
    rookie "Ah. I see. To prevent anyone else from leaving, correct? "
    blue "Very good. You're not a complete lost case. Should I give you a candy as reward?"
    rookie "No thank you. But if the seal prevents them from leaving, does it also keep us in?"
    green "Yup! But it's not like you were planning on leaving in the middle of a mission, were you?"
    advmc "No need to get nasty."
    advmc "Rookie, don't worry. No matter how badly things get, I will protect you."
    rookie "...!"
    advmc "(Huh? He looks even more worried now!)"
    green "How selfish! You're seriously going to rely on Red to carry through your first mission?"
    blue "Don't you make Red ‘carry' you all the time?"
    green "Hey! That's different! I'm the support type! You can't make someone like me fight!"
    rookie "I believe a healer is also a support type."
    advmc "Whether you can't fight or you don't want to, it doesn't matter. I will make sure that all of you get out alive. That is my promise to you, my comrades."
    green "Ugh. Way to sap up the conversation."
    rookie "..."
    advmc "(I can't tell what kind of expression that's supposed to be. Is he happy? Is he annoyed? Does he even care about what I just said?)"
    blue "Well, with that established, can you guys shut up so I can put up the seal?"

    menu:
        advmc "Sorry about that!"
        "Green, I want to check out that room.":
            jump cafeteria
        "Rookie, I'm curious about the portrait over there. Come with me?":
            jump portrait
        "I'll stay and guard you, Blue.":
            jump stayguard

label cafeteria:
    #Play Green's Theme
    play music "music/Wolf_Nilson_Trio_-_04_-_Auf_der_anderen_Seite.mp3" fadein 1.0 fadeout 1.0
    show greenapprove at appsprite
    play audio "sfx/hand-bells-d-single.mp3"
    $ greenap+= 1
    green "Ugh. Don't make me spread my area so thinly. The furthest I can go is to the doorway... Hey, are you listening?!"

    #nvl set up
    scene bg diningroom with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    window show

    nvlmc "I ignore him and walk into the dining hall area. After a quick glance around, I turn to Green, who is fuming against the doorway."
    nvlmc "Is he that annoyed that I didn't acknowledge hearing him? Or maybe it's that he's trying his best to expand his Zone and marking it with smoke, except it's too thinned out to be of any effect. I probably shouldn't make fun of him for that, though. He did warn me about this, after all."
    nvlmc "But still, this is a huge place. The fact that Green is able to hold up a Zone this big is quite a feat. He'll probably get a huge head if I say something like that, though."
    nvlmc "I will never tell him this either, but his Zone has gotten much more reliable, too. I wonder if the constant stress of the missions is honing his abilities."
    if trueend:
        nvlmc "I wonder if my own abilities have gotten any better. Then again, my ability might not be something that can get better."

    #end nvl
    nvl clear
    window hide

    advmc "Hey, you don't have to move your Zone. Keep it concentrated around Blue."
    show g temp at center with dissolve
    green "And if you get ambushed? You're our best fighter. If you go down, none of us have a chance once Blue's seal goes up. So shut up and let me do my job."
    advmc "Heh. Surprisingly, even you have a soft side, huh?"
    green "If you're done looking, then we should leave!"

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "I turn my attention to the rest of the room. "
    nvlmc "There's a long table stretched in the middle of an elongated room. I'm shocked that it's still standing, what with some of the legs looking like it's been gnawed off. But when I get near enough, I can smell the rot. Better not get too close."
    nvlmc "There aren't any chairs around. It makes me wonder if they were removed for remodeling or if this was part of the \"ghostly activities\" that the previous owners mentioned. I don't feel any spiritual energy right now, though. But just in case, I should keep my guard up."
    nvlmc "It looks like there used to be tapestries on the walls. But there are just torn up pieces of dusty fabric on the walls now. Hm? It looks like there's something tucked in here. But I can't quite reach it. Green probably won't appreciate me asking him for help, right?"
    nvlmc "Despite how the glasses to the windows seem to be shattered at places, it doesn't feel like there's much of air getting in here. Is that just part of the haunting? There's also a lot of dust and signs of spiderwebs. That reminds me, when was the last time we cleaned the office?"

    #end nvl
    nvl clear
    window hide

    green "Hey! Get back here now!"
    advmc "Are we being attacked? How many?"
    green "Too many for Rookie and Blue to handle alone. I'll slow them down. Get going!"

    jump firstambushed

label portrait:
    #Play Rookie's Theme
    play music "music/krackatoa_-_Pretend_and_walk_outside.mp3" fadein 1.0 fadeout 1.0
    show rookieapprove at appsprite
    play audio "sfx/hand-bells-d-single.mp3"
    $ rookieap+= 1
    rookie "Understood."
    advmc "Green, I'll leave it to you to protect Blue."
    green "Yeah, yeah. So annoying."

    #nvl set up
    scene bg portrait with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    window show

    nvlmc "The portrait on the wall seems to be that of a woman. A blonde, pale woman adorned in bright colors. She has a bouquet of flowers in her lap that she holds gingerly. The background is a field of flowers, almost looking as if they're showering her. The paint is cracked and clearly aged. Despite that, I can't help but to feel like this painting has been very well preserved."
    nvlmc "I wonder who she was and how she's related to this mansion. Is she the wife of a previous owner? Will we have to face her spirit? Or maybe someone just thought it fit the mood of the mansion and put it here. Rich people tend to do crazy things like that. Especially to haunted places."
    nvlmc "In fact, one place that we investigated turned out to not be haunted at all. And it was all just a trick the servants of the manor pulled on their owner. But that's neither here nor there. This place is clearly abandoned. There are no servants to pull a prank like that."
    nvlmc "There looks to be faint marks on the wall that disappear under the frame of the portrait. Is there something behind this?"

    #end nvl
    nvl clear
    window hide

    "Hey, can you help me move the portrait?"
    show r temp at center with dissolve
    rookie "Is that why you asked me to come?"
    advmc "Who else can I depend on?"
    rookie "..."
    advmc "(Please, I can't read your mind. Say something!)"
    rookie "I... I was happy that you asked me."
    advmc "(Did he read my mind...?)"
    rookie "Three years ago..."
    advmc "Huh? Three years ago?"
    rookie "I-it is nothing. I will move this for you."
    if trueend:
        advmc "(Three years ago? Why would he bring something up from that long ago? ... He can't be...?)"

    #nvl set up
    window show

    nvlmc "Rookie's ability is to control plants. According to him, it's not as precise as controlling. He just asks for the plants for help and they comply. This somehow allows him to heal people. Don't ask me how. I don't really understand either."
    nvlmc "But it's a pretty cool ability to watch unfold. Because Rookie is always so stoic and quiet, you don't realize that he's done anything until the plants respond to him. "
    nvlmc "The mansion is old enough that it must have some weeds growing somewhere hidden. Bright green of small sprouts begin to cover the area by the portrait. There's a loud groan of old wood. It almost looks like the portrait's frame has been elaborately decorated by bright green of whatever weed has grown here."
    nvlmc "And standing right next to it as if he had nothing to do with this is Rookie."
    nvlmc "See? What did I tell you? Pretty cool, right?"
    nvlmc "The giant portrait shudders as the plants surround it and-"

    #end nvl
    nvl clear
    window hide

    show whiteflash zorder 50 with vpunch
    play audio "sfx/82082__rmw2861__1000000009.mp3"
    "{i}Skreeeeeeeeeeeeeee!{i}"

    advmc "Tch! Looks like there's no time for this. Rookie, let the portrait be. We need to focus on protecting Blue."
    rookie "Understood."

    jump firstambushed

label stayguard:
    #Play Blue's Theme
    play music "music/Peter_Rudenko_-_12_-_Snowing.mp3" fadein 1.0 fadeout 1.0
    show blueapprove at appsprite
    play audio "sfx/hand-bells-d-single.mp3"
    $ blueap+= 1
    advmc "Green, Rookie, look around and make sure we won't be ambushed."
    green "Yeah, yeah. So noisy."
    rookie "Understood."

    scene bg fronthall with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    show bl temp at center with dissolve
    blue "You know you don't have to stay here with me. If there's trouble, Green will let you know."
    advmc "Do you want me to leave?"
    blue "No, no. I just... thought you'd rather explore."
    advmc "(It looked like he was going to say something else.)"
    advmc "If I'm bothering you, I can go."
    blue "Now you're just being petty."
    advmc "What can I say? I'm a petty being."
    blue "I'm sure you are."

    #nvl set up
    window show

    nvlmc "To be honest, I stayed because I like watching Blue's ability."
    nvlmc "As stated, Blue can create seals. He mentioned once that it was a leftover from his trainings from when he was trying to become a mage. But he doesn't really like talking about the past. All I know is that Blue had some disagreement with the people he was with and ended up with us."
    nvlmc "From the way he tells it, though, it doesn't sound like Boss gave him much of a choice. He was already working as a Supernatural Investigator by the time I joined. So I don't know more than that."
    nvlmc "Everyone uses their abilities differently. For Blue, whenever he creates a seal, he calls upon the magic in the air around him. It looks like colorful fireflies decorating the air itself. It's quite a breathtaking sight."
    nvlmc "My own ability is nothing refined like that."
    nvlmc "That's probably why I love watching Blue at work the most."

    #end nvl
    nvl clear
    window hide

    blue "You know, it's hard to focus when you keep staring like that."
    advmc "Eh? I didn't take you for the shy type, Blue."
    blue "Is that supposed to be a compliment?"
    advmc "Always is!"
    blue "Despite accusing me of treating you like a kid, you're quite an offender yourself."
    advmc "I don't treat you like a kid, Blue. At best, you're more like... "
    blue "Like...?"
    advmc "(That's funny. I can see my breath? Tch. That means-)"
    show g temp at left with dissolve
    green "Sorry to interrupt, but we're being attacked!"
    advmc "Blue, get that seal up. I'll deal with this!"

    jump firstambushed

label firstambushed:
    #Suspenseful Music Start!
    play music "music/Chris_Zabriskie_-_14_-_Prelude_No_14.mp3" fadein 1.0 fadeout 1.0
    scene bg fronthall with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    #Ability to skip the tutorial if you've already played through at least once
    if endingct > 0:
        menu:
            "Would you like to skip the tutorial battle?"
            "Yes":
                jump introToWitch
            "No":
                jump firstambushedcont

label firstambushedcont:
    show r temp at center with dissolve
    rookie "There's so many of them..."
    show bl temp at left with dissolve
    blue "Sorry guys. The seal isn't ready yet. Until it is, I won't be able to put up defensive seals around us."
    show g temp at right with dissolve
    green "What a pain. I'll slow them down with my Zone."
    advmc "Please do. Blue, concentrate on your seal. That's our number one priority. Rookie, stay close to Blue and protect him the best you can."
    rookie "What are you going to do?"
    advmc "Don't you remember? I'm the tank."

    hide r
    hide bl
    hide g

    #Explain Hunt Mode
    #NVL Mode
    window show

    nvlmc "Almost as if understanding that standing in my way will get them eliminated, the ghosts hide."
    nvlmc "Do they think such a childish method will keep them safe from me? I honestly hate being underestimated like this. Although I wasn't planning on it, this is pretty much begging me to be petty. They clearly want to be completely eradicated, you know?"
    nvlmc "Until I run out of space to look, I'll search through every nook and cranny until I've found them all. Then I'll swallow them whole and turn their miniscule life force into energy fuel."
    nvlmc "I have zero intention of letting any of them get away."

    #end nvl
    nvl clear
    window hide
    #Hunt Mode Music
    play music "music/Chris_Zabriskie_-_07_-_Its_Always_Too_Late_to_Start_Over.mp3" fadein 1.0 fadeout 1.0
    #Call Hunt Mode
    call huntmodestart

    #Back to our suspenseful music
    play music "music/Chris_Zabriskie_-_14_-_Prelude_No_14.mp3" fadein 1.0 fadeout 1.0

    scene bg fronthall with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    show w temp at center with dissolve
    prewitch "What's this? It's been so long since we had guests!"
    prewitch "Welcome, welcome! And now die!"
    hide w

    #Explain Battle Mode
    #NVL Mode
    window show
    nvlmc "And now the boss shows up. Good thing I'm charged up and ready to go."
    nvlmc "I have five moves I can make. The first is attack. It takes 1 energy to use, and I do flat damage."
    nvlmc "The second is defend. It also takes 1 energy, and it reduces all incoming attacks."
    nvlmc "The third is magical attack. It takes up 3 energy to use, but it does 3 times the damage my normal attack does."
    nvlmc "The fourth is my 'beast' mode. It takes up 20 energy or all three of my jewels, so it's not something I can use without thought. But for a short while, I'll at least be able to do even more damage while taking less damage."
    nvlmc "The last, obviously, is healing. Note that I can only use this if I have at least one jewel. By sacrificing one of my jewel, I can fully heal myself."
    nvl clear
    nvlmc "It's a lot to take in at once. So just try different things. No need to worry. I'm super strong and sturdy, so I won't go down that easily."
    nvlmc "Just be mindful of my health and how much energy I have left. The minute those numbers hit zero, we'll be in big trouble. But if we can defeat the enemy before that happens, then that'll be enough."
    nvlmc "Then I'll be relying on you!"

    #end nvl
    nvl clear
    window hide

    #Begin Battle Music
    play music ["music/Ian_Alex_Mac_-_01_-_Battle_for_the_End_Zone.mp3", "music/Kevin_MacLeod_-_Broken_Reality.mp3"] fadein 1.0 fadeout 1.0
    call begin_TutRPG #Our Battle Mode Tutorial version
    #Back to our suspenseful music
    play music "music/Chris_Zabriskie_-_14_-_Prelude_No_14.mp3" fadein 1.0 fadeout 1.0
    jump introToWitch

label introToWitch:
    scene bg fronthall with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    #gotta call everyone now
    show w annoyance at center with dissolve
    prewitch "How frustrating. But you seem to be quite adept at this."
    advmc "As are you. You don't seem to be a normal spirit. Are you, by any chance, a witch?"
    show w laughing at center with dissolve
    witch "My, my! How rude! To call a fragile maiden like myself a witch! But I can't deny it, I suppose."

    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch

    advmc "My, my! How rude! We weren't done talking, you know."
    show w dark at center with dissolve
    witch "You... Did you just nullified my attacks? What the hell are you people?"
    advmc "(To think that it took her this long to get serious... What a monster.)"
    hide w
    show bl temp at left with dissolve
    blue "What a soft life you must have lived if a witch such as yourself aren't familiar with us."
    show g temp at right with dissolve
    green "I'm shocked as well. To think there exists a supernatural creature who do not know of us."
    show r temp at center with dissolve
    rookie "We are Supernatural Investigators, SpIn for short."
    hide r
    hide bl
    hide g

    show w darkfrown at center with dissolve
    witch "Investigators? "
    show w laughing at center with dissolve
    witch "Ha... haha... Hahahahahaha!"
    show w temp at center with dissolve
    witch "So you came to kill me? Is that it?"
    advmc "(Damn it! Can't you guys for once not create more problems for me?!)"
    advmc "Get back! She's going to-"

    hide w
    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch

    #nvl set up
    scene bg fronthall with fade
    window show

    nvlmc "Not good. I underestimated her. I should have taken her seriously from the get-go."

    if trueend:
        play music "music/David_Hilowitz_-_Angle_of_Light.mp3" fadein 1.0 fadeout 1.0
        #end nvl
        #CG????
        window hide
        boss "Hehe... I guess I overestimated myself a bit."
        "Shut up, you idiot! You knew I can take that blast! Why did you jump in front of it?"
        boss "Well, it's just... kind of rare for me to protect you, you know? Thought I'd take advantage of it."
        "Hey, next time you get an opportunity like this?"
        boss "Yeah?"
        "Don't."
        boss "Hehe. That kind of rough side of you is cute, too."
        "Didn't I tell you to shut up?"
        play music "music/David_Hilowitz_-_10_-_Missed_Connections.mp3" fadein 1.0 fadeout 1.0
        window show

    nvlmc "We came here prepared for a spirit, not a witch. Damn it all. This isn't good. "
    nvlmc "Although the modern usage of the word has changed considerably, the way we use the word \"witch\" is to describe someone who, for lack of better words, made a deal with a demon. The details of the deal varies from a person-and-demon pair. But long story short, a deal like that could potentially give someone a strong boost in power or some form of protection from death."
    nvlmc "Ah man. This really sucks."
    nvlmc "Until I figure out exactly what that deal is, I won't be able to just carelessly take her life. After all, it's possible that her deal was something along the lines of 'Whoever kills me is cursed forever!' That's not exactly the kind of life I'd like to live."
    nvlmc "In other words, if I don't start getting serious, none of us will make it out alive."
    nvl clear
    nvlmc "First priority is to protect everyone. "
    nvlmc "Unlike them, I'm durable enough that I can probably survive a blast or two if she starts flinging this dense energy at me. If the others got even scratched with something like this, they'd probably evaporate."
    nvlmc "But can I take the hit without letting even a stray hit get near them? Then the only other way to perfectly protect everyone would be..."
    play music "music/Marsel_Minga_-_03_-_Drum_Machine_Battle.mp3" fadein 1.0 fadeout 1.0
    nvlmc "I clutch the three jeweled necklace. Since this has a fairy's blessing, it should work."
    nvlmc "Without hesitation, I rush towards the spirit, the necklace clutched tightly in my hand. Seeing me move, the spirit turns her whole attention to me."
    nvlmc "Good."

    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch
    nvl clear

    nvlmc "Unsurprisingly, she starts firing as soon as I get airborne. Makes perfect sense. People can't change directions mid-air. I'll have to allow myself to get hit."
    nvlmc "But you know, she underestimated me quite a bit."
    nvlmc "Did she really think that this is my best?"
    nvlmc "There's a crackle of power that envelops me just in time as her blasts hit. I've done this too often to mistime this."
    nvlmc "My ability."
    nvl clear
    nvlmc "Well, to call it my ability is actually misleading. It's a part of who I am, after all. But it's not like there's any better way to describe it. To any other Supernatural Investigators, it'll be considered their ability."
    nvlmc "In the Eastern sector, there's a famous onmyouji (I suppose the closest translation would be an exorcist) by the name of Abe no Seimei. According to legends, his mother was a beast called the \"Nine-tailed Fox.\" A fox is supposed to gain an extra tail for every 100 years it lives. So to have nine of them, that fox must have lived for a long time while collecting wisdom and power. Because of his lineage, Abe no Seimei was an undefeatable man."
    nvlmc "I'm not going to say something so grand like I am a descendent of Abe no Seimei. "
    nvlmc "But there's probably some traces of his blood in my vein."
    nvlmc "Otherwise, I have no real words to describe this form of mine."

    #end nvl
    nvl clear
    window hide

    #FOX CG
    $quick_menu = False
    scene cg foxreveal with fade
    pause 1.0
    scene bg fronthall with fade
    show w temp at center with dissolve
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    $quick_menu = True
    show w temp at center with dissolve
    witch "You think a little form change is enough? "
    advmc "(It looks like she's gathering her energy for a bigger blast. Then I'll just cut her off before she releases!)"

    #nvl set up
    window show

    nvlmc "Although it is a form change, it's not like I myself have changed. It's more that... I've taken off my limiters, if that makes sense."
    nvlmc "In order to fit in human society, I have adopted a look that I personally find the most pleasing. That is my normal form. But when things get serious, that form just gets in the way, since I am using magic to keep it there."
    nvlmc "Thus, by dispelling, I can 'reveal' myself. Boss used to affectionately call this form of mine my 'Beast' form. But again, this is my real form. "
    nvlmc "I'm faster in this form. Stronger, too. I would have to be, since I'm no longer directing part of my magic to keep up appearences."
    nvlmc "But I'm not exactly proud of this form of mine. It's too... inhumane."

    nvl clear

    nvlmc "Somehow, it seems she still hasn't shown her true powers yet. Because she manages to summon smaller blasts while still gathering energy for a larger one. That'll be fine if not for the fact that I cannot allow my comrades to get hurt."
    nvlmc "I guess my weakness is too obvious, seeing that she seems to be aiming for them now."
    nvlmc "Like hell I'll let her do what she wants!"
    nvlmc "The three jewel necklace has been blessed by fairies. The typical usage of something like this is as a protection charm from a surprise attack. But there are other ways to use it, too."
    nvlmc "For example, I can crush it in my hand for an extra boost of power. It also means that I won't be able to rely on this any more, but if I can keep these guys safe..."
    nvlmc "What's a little sacrifice, right?"

    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    nvl clear

    show w annoyance at center with dissolve
    nvlmc "Her screams of pain fill the air as I fall back into Green's hold. He helps steady me as Blue finishes his seal. Rookie seems too frazzled to properly move. We'll have to talk to him later to better protect himself in these situations."
    nvlmc "At least with the seal finally finished, she won't be able to run out of this mansion. If we finish her in here, that will be it. But the problem, obviously, would be killing her and making sure that she stays dead."
    nvlmc "I turn towards her. It looks like she's struggling to hold her form together. Just a little more push should be enough to kill-"
    nvlmc "My knees give out. Huh? Did I use more power than I realized? "
    nvlmc "I stumble as both Blue and Green help steady me on either side. This is bad. If I don't at the very least stun her or tie her up, she'll get the chance to recover and come after us. And by then, there's no telling what other deals she would make with other demons to fortify her strength."

    #end nvl
    nvl clear
    window hide

    show w temp at center with dissolve
    witch "Haha... looks like you're at your limit."
    hide w
    show g temp at right with dissolve
    green "Is she gathering another projectile? Wouldn't that destroy her?"
    show bl temp at left with dissolve
    blue "Looks like she plans on killing herself with us."
    advmc "Any chance you guys can stop her?"
    green "Very encouraging to hear from our only fighter."
    blue "Rookie looks terrified, too. Tch. We need to run."
    hide bl
    hide g
    show w laughing at center with dissolve
    witch "I won't let you!"
    advmc "Heh. Got you."
    show w preplexed at center with dissolve

    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    hide w

    show g temp at right with dissolve
    green "How did you miss at that distance?!"
    hide g
    advmc "(I didn't! She pulled back at the last second. Is she prioritizing survival?)"
    show w temp at center with dissolve
    witch "Are you stupid? Why would I make it that easy for you to catch me?"

    #nvl set up
    window show

    nvlmc "The wind kicks off. I must be really weakened, if this little is enough to knock me back into Blue's arms. At least it looks like Blue has some kind of a minor seal up around us. But if she fires something at us, it won't last. And I don't have my necklace to protect me anymore."
    nvlmc "With another cackle, the witch flies up the staircase and through the gaping hole of the second floor's entrance. She doesn't put up a seal to stop us from entering, which already tells me that the second floor must be filled with traps."
    hide w
    #The music for here should be...
    play music "music/David_Hilowitz_-_10_-_Missed_Connections.mp3" fadein 1.0 fadeout 1.0
    nvlmc "The gust dies down."
    nvlmc "We seem to have returned to relative peace."

    #end nvl
    nvl clear
    window hide

    show g temp at right with dissolve
    green "Oi Rookie, how long are you going to stand dumbly over there?"
    show r temp at center with dissolve
    rookie "..."
    show bl temp at left with dissolve
    blue "You alright, Red? You look pale."
    advmc "Yeah. Just tired."
    green "Hey Rookie, aren't you our healer? Get to it."
    rookie "R-right."
    #Make sure Red is healed!
    $hp=300
    advmc "(He looks shaken. Was too much for his first mission?)"
    advmc "Hey, sorry if I scared you. You probably didn't expect that, right? I'm part... er... I suppose the best way to say is that I have some fox blood in me."
    advmc "Don't worry; I don't lose control or anything. That version is still me. Just... more powerful. Like taking off seals or limiters, you know?"
    advmc "(What am I saying? I'm making less sense trying to explain it.)"
    green "What's with that? He has our files. It's our own responsibility to read about our teammates' abilities before a mission."
    blue "Amazing. Have all of my lectures finally sunk in for you? Or are you just echoing them to look cool in front of a new member?"
    green "Shut up, you."
    rookie "I am not scared."
    advmc "Is that so? That's a relief."
    rookie "Just..."
    green "Just?"
    rookie "Three years ago, my village was attacked by a silver fox with four tails."
    blue "Three years ago? Wasn't that...?"
    advmc "If you were wondering if that was me, then yeah. It was. There haven't been any other silver foxes, let alone four-tailed ones, in about half a century."
    green "Urk. You couldn't think of a kinder way to phrase that?"
    advmc "Look, I'm not a good person. I've done many things I'm not proud of. If that makes you uncomfortable, request that you never be put on the same team with me again."
    advmc "But for this mission, I need you to set aside whatever issues you have and work with me."
    rookie "..."
    advmc "(Hey, say something!)"
    blue "Or if you guys want, I can drop the seal right now. It would mean that our mission is a failure, but at least no one would be forced to work with someone they are uncomfortable with."
    rookie "I... am fine."

    menu:
        advmc "(You don't look fine at all! Great. Now everyone's looking at me to decide.)"
        "Let's call it quits":
            jump storyendEmptyHands
        "We can't give up yet":
            jump firstfloorcont

label storyendEmptyHands:
    play music "music/Chris_Zabriskie_-_03_-_I_Dont_See_the_Branches_I_See_the_Leaves.mp3" fadein 1.0 fadeout 1.0
    advmc "It's clear that you're uncomfortable, Rookie. It'd be better for a different team to take care of this mission."
    green "But doesn't that mean that witch can get stronger in the meanwhile?"
    advmc "(Look, I don't like it either. But I'm not going to force Rookie here to spend time with a monster that wiped out his village. If he's talking about {i}that incident{/i}  three years ago...)"
    blue "At least the next group will have a better heads up about what's here. "
    rookie "If you decided this because of me, I ask that you reconsider."
    advmc "(You say that, but you look the most disturbed by the whole thing.)"
    advmc "It's not because of you. I'm too tired to keep going. Not to mention, I broke my necklace. You want your only tank to face against whatever else is in this mansion without any kind of protection?"
    green "You're a monster, so I'm sure you'll be fine."
    advmc "(Get a hint, you idiot!)"
    advmc "What's that? You want me to accidentally kill you?"
    blue "If that's how Red feels, then that's how Red feels. Go ahead. Punch Green all you want."
    green "H-huh?! Wait a minute!"

    hide bl
    hide g
    hide r

    #nvl set up
    window show

    nvlmc "I feel a little guilty for abandoning the mission before it even starts."
    nvlmc "But I doubt Rookie wants to be stuck in here with me for however long it'll take for us to complete the mission. Not to mention I'm not confident about fighting that witch again while protecting baggage."
    nvlmc "I can't allow any of these guys to get hurt. If I were to fight that witch seriously, all of their lives would be at stake. "
    nvlmc "It's better like this."
    nvlmc "Yeah, that's right. This was the correct choice to make."

    #end nvl
    nvl clear
    window hide

    #Bad End CG
    $quick_menu = False
    $ persistent.badend1 = True
    scene end bad with fade
    pause 2.0
    $ MainMenu(confirm=False)()

    #End EmptyHands

label firstfloorcont:
    show allappsprite
    play audio "sfx/hand-bells-d-single.mp3"
    $ blueap+= 1
    $ greenap+= 1
    $ rookieap+= 1

    advmc "We can't let any witch go free. That'd cause a bureaucratic mess that will doubtlessly end up with us pulling multiple all-nighters to handle."
    green "Oh, please let's not do that again."
    blue "Whose fault was it that we were in that position to begin with?"
    green "C-come on, we all suffered together. So don't blame it all on me!"
    advmc "So if we can, I would really like to complete this mission. "
    rookie "That is fine with me."
    advmc "(Are you really okay? You look pale.)"
    advmc "That witch was really powerful. If you guys are near me when I fight her again, I can't guarantee your safety. So-"
    green "That's fine. We'll stay near the back. "
    blue "I'll be focused enough to set up a better seal around us this time. Don't worry about us and go full out."
    advmc "(I'm saying if I do, you'll die!)"
    rookie "I will trust your judgement."
    advmc "(All of you suck.)"
    advmc"(But this is the first.)"

    if trueend:
        play music "music/David_Hilowitz_-_Angle_of_Light.mp3" fadein 1.0 fadeout 1.0
        boss "Pwhahahaha! What expression is that supposed to be?"
        advmc "S-shut up! I don't know! I don't know what I'm feeling!"
        boss "Tsk, tsk. You've spent this long with humans and still can't figure out emotions? I thought you foxes are supposed to be smart!"
        advmc "Being smart and knowing your emotions are different things. "
        boss "[mcname], emotions are simple. If it's a positive feeling, you smile. If not, you cry. See?"
        advmc "I-I don't know. Is this... positive? I can't figure it out."
        boss "Do you hate it?"
        advmc "N-no? I don't think so? I don't understand myself."
        boss "Then what about this? If you don't know what you're feeling, just laugh."
        advmc "What kind of logic is that?"
        boss "Once you laugh, it gets easier, you know. If it was a negative feeling, you'll suddenly feel a lot better. If it was a positive feeling, it'll make you feel doubly better for sharing it."
        advmc "That... sounds fake."
        boss "H-hey! I'm trying to give you some sound advice!"
        play music "music/David_Hilowitz_-_10_-_Missed_Connections.mp3" fadein 1.0 fadeout 1.0

    advmc "Pfft... Hahahahaha!"
    green "Nice going, Rookie. Red's lost it because of you."
    blue "A-are you alright?"
    rookie "..."
    advmc "I will make sure all of you get back safely. Until then, will you trust me?"
    green "Were you hit on the head while fighting? What's with such a gross question?"
    blue "Did you forget, Red? We are a team. As much as we trust you, you should trust us."
    rookie "... I... I will leave it to you."
    advmc "Good. Then our next objective is the floor above us. I have no idea what's waiting for us up there, but I will keep you safe. If you can't trust me, please feel free to stay here."
    green "I'm telling you, stop being so gross!"
    blue "I'll layer so many seals around you that no one will be able to touch you. Heh."
    rookie "I trust your judgements."
    advmc "Then let's go!"

jump secondfloor #Proceed to the 2nd Chapter

#return #Back to story
