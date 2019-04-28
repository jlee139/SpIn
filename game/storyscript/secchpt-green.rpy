#Green Route Here
label secgreen:
    #Play Green's Theme
    play music "music/Wolf_Nilson_Trio_-_04_-_Auf_der_anderen_Seite.mp3" fadein 1.0 fadeout 1.0
    show greenapprove at appsprite
    play audio "sfx/hand-bells-d-single.mp3"

    green "Your phrasing is worse! Can’t you just say that you’re dazzled by my ruggedly good looks instead?"

    menu:
        advmc "(Oh, please! Like you're all that!)"
        "Rookie, here’s another patient for you!":
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "So you don’t deny my good looks!"
            advmc "You’ll never be able to settle down if you treat everyone you meet like this!"
            green "It’s fine since you’ll be with me."
            advmc "Says who?!"
            green "Oh jee, I don’t know… Maybe the little fox who is determined to save my life?"
            advmc "I-I’m trying to save everyone, n-not just you!"
            green "Haha! You’re stuttering! That’s adorable!"
            blue "If you guys can please focus. You're scaring Rookie."
            rookie "I am fine."
        "Like hell. If you’re good looking, then I pity those who are considered ugly.":
            $ greenap-= 1
            green "What’s with that? I’m plenty good looking! You just have rotten eyes."
            advmc "You sure it’s not your senses that’s rotten?"
            blue "Stop fighting, children."
            advmc "We’re not children!"
            green "Red’s the one being rude. Stop blaming it on me."
            rookie "Would you rather pick someone else?"
            advmc "(Ah, what am I doing, worrying Rookie? Tch. What was I thinking, picking this idiot of a guy?)"
            advmc "Don’t worry about it. We’re always like this."


    green "Alright, then we’ll take this door. Try not to slow me down, Red."
    advmc "Hilarious coming from the guy who could barely keep up with my pace."
    blue "Are you two sure you want to team up?"
    rookie "If you want to change-"
    advmc "We’ll be fine. Sorry for worrying you."

    #nvl set up
    nvl clear
    window show

    nvlmc "I allow Green to enter first to establish his Zone before following after him. It’s something that we’ve talked about before. Despite the fact that I’d be able to react much faster than him if this turned out to be a trap, he prefers that I put in an extra effort to save him by going first. "
    nvlmc "He likes to insist that he can establish his Zone faster than I can react to a trap, all because of this one mission. He refuses to acknowledge that it was because he tripped me."
    nvlmc "Just as I thought about that time, I hear Green’s panicked voice call out to me. Tch. No time to rest, huh?"
    scene black
    nvlmc "I rush in to help him. But even in my haste, I notice the door slamming shut behind me. Guess Blue and Rookie will be on their own. I hope they’ll be okay."
    nvlmc "But I have no time to waste on thinking about them. I need to find Green. The thick cigarette smoke makes it hard to smell or see. But there’s still one more trick up my sleeve."

    show particleFog1:
        alpha 0.9

    #escape nvl mode
    nvl clear
    window hide

    "Green!"

    menu:
        advmc "(Hehe. Green's weakness is-)"
        "I’ll go with you to that concert you talked about!":
            advmc "..."
            advmc "(Did it not work?)"
            show g temp at center with dissolve
            green "Hey… Didn’t I already tell you? Someone with zero music sense like you will never fit in at a concert."
            advmc "(I guess it worked. But why does he look so mad?)"
            $ greenap-= 1
        "I know who broke your favorite figurine!":
            advmc "(Ugh. What horrid stench. That must be-)"
            show g temp at center with dissolve
            green "Who was it? It was that damned Zero, wasn’t it?"
            advmc "(... his cigarette.)"
            advmc "(Sorry, Zero! I’ll make it up to you when we see each other again!)"
            advmc "You already knew, huh?"
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "I’m going to kill that brat!!"

    green "But why are you in here already? I didn’t give you any signal to come in."
    advmc "What are you talking about? I heard you call out for help."
    green "Me? Ask for help? What dimension are you living in?"
    advmc "This coming from the guy who screamed like a little girl when we were watching a horror movie?"
    green "Hey! Jump scares are a different thing!"
    advmc "(... The fog around us thickened just now, didn’t it? Ah, how troublesome. I hate fighting blind.)"
    green "Red..."
    advmc "Yeah. This fog isn’t yours, is it?"
    show g temp at left with dissolve
    show but happy at right with dissolve
    #Butler's Theme
    play music "music/David_Szesztay_-_Bizarre_Waltz.mp3" fadein 1.0 fadeout 1.0
    prebut "Astute observation, my esteemed guests."
    green "Alas, my smoke isn’t that thick. I’m not the type to keep things in until I can’t take it anymore, after all."
    advmc "If that was supposed to be a dirty joke, I’m afraid it flew over my head."
    green "But you recognized it as a dirty joke. So it’s my victory, I’m afraid."
    show but temp at right with dissolve
    prebut "Ahem."
    advmc "But can you really claim victory when your jokes fall this flat?"
    green "You’re such a sore loser! Why can’t you just admit that I won?"
    advmc "When you’ve actually won, I’ll acknowledge it. Until then, keep trying!"
    show but annoyance at right with dissolve
    prebut "Hello? Do you not see me?"
    green "Do you not have eyes or something? Can’t you see that we’re talking? "
    advmc "Honestly, have some more manners!"
    show but temp at right with dissolve
    prebut "I-I apologize."
    advmc "(Huh? Wait. There shouldn’t be a third person here!)"
    advmc "Who are you? Are you the cause of this fog?"
    show but happy at right with dissolve
    prebut "Astute observation, my esteemed guest!"
    green "Didn’t you already say that?"
    show but temp at right with dissolve
    prebut "You noticed? But you didn’t say anything? My, the esteemed guests this time seems to like cruel jokes."
    advmc "I prefer the term ‘rude.’"
    green "Of course, you would."
    advmc"It’s what I use to describe you, after all."
    green "Hilarious coming from the fox who bites people’s fingers."
    advmc"I told you to stop trying to put your finger in my mouth when I’m sleeping! I gave you a warning!"
    prebut "Can we please move on…?"
    advmc "You done yet?"
    green "I’ve been done for a while, actually."

    menu:
        advmc "(Then say it sooner!)"
        "Why wouldn’t you say that earlier?!":
            $ greenap-= 1
            green "It was obviously to see how good you are at keeping up with me. Unfortunately, Red, you failed."
            advmc "Consider the people who have to put up with your prattles the next time you decide to keep silent."

        "Are you stupid? That could’ve put both our lives in danger!":
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "B-but you’re… You’re you. There’s no way that this little can put our lives in danger."
            advmc "D-don’t just suddenly flatter me! "

    hide g
    show but temp at center with dissolve
    prebut "Ahem. As I was saying-"

    #Suspenseful Music Start!
    play music "music/Chris_Zabriskie_-_14_-_Prelude_No_14.mp3" fadein 1.0 fadeout 1.0

    #nvl set up
    nvl clear
    window show

    nvlmc "I don’t give him a chance to finish. "
    nvlmc "Instead, I lunge for his neck, determined to tear it out. "
    nvlmc "If I can finish this quickly, this fog will disappear. That should at least give us a chance to find the door to make sure that Blue and Rookie are okay. I know that I should be trusting them to take care of themselves, but I can’t help but to worry. "
    nvlmc "At the very least, this is Rookie’s first mission. I don’t want him to get scared because of this one mission (or worse, scared because he met the one who destroyed his village) and decide to quit. We need healers."
    nvlmc "Besides, if I can’t take care of something like this fast, Green will never let me hear the end of it."

    nvl clear

    nvlmc "But just as my hands seemed to reach the figure, he disappears in a puff of smoke. "
    hide but
    nvlmc "It’s not teleportation. It can’t be. At least, if it was, I’d have been forced to go along with him, since I made contact. The more likely scenario is that he was never standing in front of me in the first place."
    nvlmc "In other words, a fake. "
    nvlmc "Just how shot are my senses from this dense fog that I made such an elementary mistake?"

    #escape nvl mode
    nvl clear
    window hide

    show g temp at left with dissolve
    green "Seeing that the fog is still here, I’m assuming you missed?"
    advmc "No, I hit."
    show but temp at right with dissolve
    prebut "Indeed, you did hit my puppet. But as you can see, it doesn’t mean much."

    #nvl set up
    nvl clear
    window show

    nvlmc "From the distance of the dense fog, I see bunch of silhouettes staggering towards us. Their movement is slow. I can only assume that these \"puppets\" as this guy had said can’t move too fast. Are they zombies? Ghouls? Golems? Are they really there or is it an illusion trick of the fog?"
    nvlmc "Just to check, I lunge forward to attack. The minute an attack hits, the \"puppet\" disappears in a puff of smoke. "
    nvlmc "Nothing solid, then. But it didn’t feel like just an illusion either. I get the feeling that they could actually do some damage to me if I let them get too close. "
    nvlmc "Feeling uneasy, I rush back to Green and pick him up. He’s heavier than he looks. But there’s no time to dwell on that. It’s important to see if I can get away from this mob approaching us."

    hide but
    #escape nvl mode
    nvl clear
    window hide

    show g temp at center with dissolve
    green "Hey! What the hell? P-put me down!"
    advmc "Shut up, I’m trying to save our lives!"
    green "I dropped my cigarette. My Zone-"
    advmc "With this much fog, marking your Zone with smoke is stupid!"

    #nvl set up
    nvl clear
    window show

    nvlmc "I think I finally found a wall. There’s no sign of the door, so it’s probably not in the direction that we came in from. Jeesh, just how big is this room? It didn’t look like much when we were outside. Or perhaps that's just my senses being shot from the fog?"
    nvlmc "Green squirms in my grasp, so I finally set him down. He looks like he’s very much offended by the whole thing, but it can’t be helped. Saving lives comes before dignity."
    nvlmc "From here, the mob seems to be taking their time to come towards us. Their speed is too slow to actually be threatening, though. Then we should use this precious few time to figure out a way to defeat them."

    #escape nvl mode
    nvl clear
    window hide

    green "My Zone isn’t working, is it?"
    advmc "Why are you asking me? Shouldn’t you know that best? It’s your ability."
    green "I can’t feel that mob. I didn’t even feel that guy when he appeared either. "
    advmc "Is it the fog? Is it interfering with your ability?"
    green "Yeah, I think so."

    menu:
        advmc "(He looks pretty down about this.)"
        "Ehhhh? So there are things that even the great you can’t do, huh?":
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "Can you not? I’m serious here."
            advmc "It's fine. We’re a team. Our purpose is to cover each others’ backs."
            green "… Yeah. You’re right. Guess I’m being sensitive for no reason."
        "It is what it is.":
            $ greenap-= 1
            advmc "Yeah. I guess so."
            advmc "(Huh? He seems upset about something. Jeesh, what a kid, being this sensitive.) "

    advmc "Well, we should focus on figuring out how to defeat that guy anyways."
    green "I bet this place is his Zone, and we walked in without another thought. If he has already established it, then it explains why I wasn’t able to."
    advmc "Hey, can you create those zombie like creatures?"
    green "Maybe if I had something more physical to work with… H-hey, you don’t think…?"
    advmc "They disappear too easily to be made out of corpses. "
    show g temp at left with dissolve
    show but happy at right with dissolve
    #Butler's Theme
    play music "music/David_Szesztay_-_Bizarre_Waltz.mp3" fadein 1.0 fadeout 1.0
    prebut "That’s correct! My esteemed guests this time around are so smart. "
    advmc "How long have you been there?"
    show but temp at right with dissolve
    prebut "A good butler like myself is never too far from providing a necessary service!"
    green "A butler, huh? What? You used to work here or something? "
    butler "I am troubled to correct you, my esteemed guests, that I am still an employee of this mansion. If you have any issues, please feel free to inform me or any of my fellow butlers."
    advmc "How do we get out of here?"
    butler "Oh, how terribly hurtful! My esteemed guests are already planning on leaving! Tell me, was our hospitality not enough? What should we do to improve the situation?"
    green "Hey, since you’re a Butler, aren’t you supposed to serve us tea and snacks?"

    menu:
        advmc "(Huh? What’s this guy trying to do?)"
        "(Play along)":
            advmc "I prefer coffee and cake. If the coffee isn’t bitter, I’ll send it back."
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "Oh? Bitter coffee? Didn’t think you were the type to prefer bitter things. Are you trying to be an adult?"
            advmc "Have you forgotten just how many tails I have?"
            green "Weren’t you asleep for a good 300 of those years? "
            advmc "That’s still 100 more than you!"
            green "Haha! You have no idea how to do basic calculations, do you? "
            advmc "S-shut up!"
        "(Stay Focused)":
            advmc "What are you talking about, Green? Now is not the time to play around."
            $ greenap-= 1
            green "You have no tactical brain, do you? This is why you’ll never be more than a grunt worker."
            advmc "As if you can go through missions like this by yourself. "
            butler "My dearest esteemed guests, I insist that you stay for tea!"
            advmc "(Great. Way to go, Green. Now this guy is going to chase us to drink tea!)"
            advmc "Alright. Fine. Get me the bitterest coffee."

    show but happy at right with dissolve
    butler "Then please, leave it to us!"

    #nvl set up
    nvl clear
    window show

    play audio "sfx/click.mp3"
    nvlmc "With a snap of his fingers, the fog clear just enough for us to see a comfortable-looking set up."

    scene bg greenroom with fade
    show particleFog1:
        alpha 0.8

    nvlmc "There are two couches facing each other with a low table in the middle. Despite the fog, there seems to be just enough lighting for us to see. Just how does this fog of this Butler’s work? It has to be his ability, but it seems different from Green’s."
    nvlmc "Is this set up something created from his fog? Or are these leftover furnitures from those who lived here previously?"
    nvlmc "The mob from before are nowhere to be seen. Is that on purpose? Or are they currently hiding in the fog to surprise us? But at the same time, I don’t sense any hostility as of now. It’s possible that this Butler really does just want to serve us before sending us off. "
    nvlmc "Already, I know that’s too naïve a thought."

    #escape nvl mode
    nvl clear
    window hide

    show g temp at left with dissolve
    green "So how long have you served in this mansion?"
    show but happy at right with dissolve
    butler "It is the pride of my family to have served in this mansion for generations. "
    advmc "Every single member of your family did? "
    butler "That is correct."
    advmc "So as long as your family works for this mansion, you don’t care about the master?"
    butler "I must beg to differ, my esteemed guest. My family served the same family who owned this mansion for generations."
    green "How’d they lose it?"
    show but annoyance at right with dissolve
    advmc "(Oh, he got quiet all of a sudden. Is this a sore topic?)"
    butler "My esteemed guests are mistaken. This mansion was never lost."
    advmc "But it was sold and bought by various people who tried to to modernize this place."
    butler "That may be so, but this mansion never belonged to any of those thieves. "
    advmc "Then who does it belong to?"
    show but temp at right with dissolve
    butler "Here comes your drinks and sweets. "
    advmc "(He’s hiding something.)"

    #nvl set up
    nvl clear
    window show

    nvlmc "A small trolly cart is pushed forward by one of the butler’s puppets from the dense fog. On the trolly is a tray that the butler wastes no time to pick up. As promised, there are two cups filled with liquid and two small slices of cakes on fancy looking plates on the tray."
    nvlmc "The butler turns to Green and I with a polite smile. "
    nvlmc "He places the two cakes in front of Green and me before he puts the cups down. His manner is impeccable. He doesn’t spill nor make loud clanking noise when the plates hit the table. So this must be the power of a butler."
    nvlmc "Once everything has been placed, the butler takes a step back and makes a small motion that seems to say dig in."
    nvlmc "I get a bad feeling about this. It’ll be too easy for the food and the drink to have been poisoned. Therefore, I make no move to eat. "
    nvlmc "But it seems Green didn’t get the memo."

    #escape nvl mode
    nvl clear
    window hide

    green "Oh hey, this cake is delicious. The tea’s kind of too bitter for me, though."
    advmc "Y-you’re eating it?!"
    green "I mean, he and his puppets worked really hard to make this for us, you know?"

    menu:
        advmc "Green..."
        "Are you stupid?":
            advmc "Even if that’s a really touching mental image, it doesn’t change the fact that we’re not exactly on the same side here!"
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "But isn’t it a waste of this good looking food?"
            butler "Indeed, my esteemed guest. It will be a waste to not try it at least."
        "Who cares how they feel?!":
            $ greenap-= 1
            green "That’s rude."
            butler "Indeed, my esteemed guest. That is quite rude of you."
            green "C’mon, stop being so stubborn and try it. Boss didn’t raise a rude fox, now did he?"
            advmc "Shut up, you."

    advmc "I can’t believe this."

    #nvl set up
    nvl clear
    window show

    nvlmc "There has to be a limit to the craziness one finds themselves in. Does Green really not find it strange to be given consumable from someone who tried to kill us not few minutes ago?"
    nvlmc "With the pressure of both of them staring down at me, I reluctantly pick up my cup of coffee."
    nvlmc "It smells like coffee. It looks like black coffee, too. But it is actually? Should I just pretend to drink it?"
    nvlmc "I tip the cup towards me, being very careful to just appear to drink. Then slowly, I put the cup back down on the table and meet their eyes."

    #escape nvl mode
    nvl clear
    window hide

    if trueend:
        play music "music/David_Hilowitz_-_Angle_of_Light.mp3" fadein 1.0 fadeout 1.0
        scene bg office memory with fade
        boss "Oh, you don’t want to drink that. That’s coffee."
        advmc "But you’re drinking it. Why can’t I have it?"
        boss "It’s too bitter for you."
        advmc "You don’t know that. Maybe I like bitter things."
        boss "Alright, if you want to try it. But I’m warning you, this is really bitter."
        advmc "..."
        boss "..."
        advmc "... Stop smirking."
        boss "Hahaha! I told you. It’s too bitter for you."
        advmc "But you drink it without a problem."
        boss "Ah… I don’t drink it for the taste."
        advmc "Eh? What’s with that? You humans are too strange in your ways. If food cannot be enjoyed for their taste, what’s the point?"
        boss "Funnily enough, coffee is also pretty toxic for most other species, too."
        advmc "What!? That’s like saying you’re drinking poison for fun! Hey, stop laughing at me! It’s a valid concern!"
        #Play Green's Theme
        play music "music/Wolf_Nilson_Trio_-_04_-_Auf_der_anderen_Seite.mp3" fadein 1.0 fadeout 1.0
        scene bg greenroom with fade
        show particleFog1:
            alpha 0.5

    green "Well?"
    advmc "Well what?"
    green "How’d it taste?"
    advmc "Coffee is coffee. It’s bitter. How’s it supposed to taste?"
    green "You’re such a…! I’m so sorry about this stupid idiot. Absolutely no manners at all, this fox!"
    advmc "I resent that!"
    butler "It is alright, my esteemed guest. I am deeply honored and touched that you are worried for me. However, my duty as a butler is to serve. It is a great honor and pleasure for it to be appreciated, but a thank you isn’t necessary."
    green "You’re a great guy!"
    show but happy at right with dissolve
    butler "Thank you, my esteemed guest."

    menu:
        advmc "(Ugh. These two are getting on my nerves. I should change the topic.)"
        "So how did it happen that bunch of ‘thieves’ took this place?":
            show but temp at right with dissolve
            butler "It was the most unpleasant set of unfortunate events. The master of the house suddenly fell ill, forcing his young daughter to take over. Our young mistress did everything she believed to be correct."
            green "But it wasn’t enough?"
            butler "Humans’ hearts are cold. If they see an easy prey, they will find a way to take advantage of it anyway they can."
            advmc "(Yeah. I get that.)"
        "What was your former master like?":
            show but temp at right with dissolve
            butler "The mistress was a beautiful and kind soul. She was suddenly forced into the role of the head of the house when she was young. But she never complained."
            advmc "(Mistress? Could she be the lady depicted in the portrait?)"
            green "That must have been hard for her."
            butler "If it was, she never let us know. She’s that kind of a gentle person."

    advmc "What happened to her?"
    show but saddness at right with dissolve
    butler "She was tricked. Because she was so young, it was easy for those vultures to tear everything out of her hands."
    advmc "(So this mansion fell into ruin because of that? But at that point in time, there shouldn’t have been ghosts and this mansino shouldn’t have been abandoned. This clearly isn’t lining up.)"
    green "It must have been rough for her. Good thing you were there to help her, huh?"
    butler "..."
    advmc "You didn’t help her?"
    butler "… What power does but a servant have?"
    advmc "For someone who proclaims loyalty, you don’t follow through, do you?"
    green "H-hey, no need to get nasty. Sometimes, there’s really nothing you can do."
    advmc "I find that hard to believe. "
    advmc "You’re telling me that someone you serve was in trouble but you didn’t even raise your hand to help? Because \"servants don’t have power.\" Isn’t that too convenient? "
    green "It’s not about conveniency. Even if you want to help, there are limits to what you can do."
    advmc "That just means that you’re not trying hard enough. There’s always something you can do. Even if it’s biting off my own tails, I-"
    green "But that’s the case for you. Not everyone has that luxury."
    show but temp at right with dissolve
    butler "It is exactly as my esteemed guest says. There was nothing that we, the servants, could do to save our mistress."
    advmc "(What’s with that kind of a weak response? I… don’t understand.)"
    butler "Your expression seems to be saying that you don’t understand. "
    advmc "… Wasn’t she your most important person? "
    green "It was because she was so important that they couldn’t do much."
    advmc "Yeah, I don’t get it at all."
    green "You’re such a hopeless fox. It’s simple. No matter how strongly you feel, there are still things you cannot do. You can’t bring back the dead, can you? For that matter, you can’t release the curse on Boss."
    advmc "T-that is… I see. So it’s that kind of situation."
    green "I thought you’d argue a little more. It’s not fun if you just give up like that."
    advmc "This isn’t a game, you know."
    advmc "(Huh? Wait a minute.)"
    butler "My esteemed guests are so kind."
    advmc "(I completely forgot about him!)"
    show but saddness at right with dissolve
    butler "If people as kind as you were around my Mistress, I’m sure this wouldn’t have been her fate. "
    advmc "So after she lost this mansion, what happened to her?"
    butler "She was silenced. We found out about it much too late. When we made our discontent known to the new owner, we were all killed."
    show but annoyance at right with dissolve
    butler "What that person was after was the money behind our Mistress’s name. Our Mistress, the servants, and the physical mansion were of no consequence. "
    green "W-wait, everyone was killed?"
    butler "Yes. Bunch of ruffians were hired to set the mansion on fire with us inside. It was quite gruesome. Did you know that you’re more likely to die due to the smoke than you are to burn to death?"
    advmc "(No wonder this place has so many spirits. If everyone who used to work here died while bearing a grudge…)"
    advmc "(Then most likely, that Witch is this Mistress of his. Guess that’s why she didn’t take well to us suddenly intruding.)"
    green "Man, what a way to go. "
    advmc "(‘Thieves,’ he said. Is that how we look to him, too? Huh? Wait a minute!)"
    green "I can’t imag- {i}cough{i}"

    #nvl set up
    nvl clear
    window show

    nvlmc "I should have realized something like this would happen. I should have realized it. Why didn’t I put it together from the beginning? It was so damned obvious!"
    nvlmc "Green starts to cough up blood. He tries to cover his mouth, but the blood seems to gush out from between his fingers. "
    nvlmc "I should have seen this coming. I should’ve realized what would happen. Why did I let him drink and eat anything that these damned spirits offered? Why did I let him trust them so easily?"
    nvlmc "Fine! This is how they want to play? I’ll teach them what happens when you anger a fox!"
    nvlmc "The fog in the area begin to swirl, reacting to my powers. Maybe I should have done this from the beginning. I should have just blown everything away!"
    hide but
    nvlmc "As if understanding my anger, the Butler quickly steps back, calling his little puppets to stand between us."

    #escape nvl mode
    nvl clear
    window hide

    show g temp at center with dissolve
    green "Red, that’s no good."
    #Green CG

    advmc "Shut up! If you have time to speak, figure out how to heal yourself!"
    green "Look around! They outnumber you. If you lash out blindly like that, you’ll lose."
    advmc "(Why does he have to make so much sense at a time like this?)"
    advmc "Then what exactly do you suggest?"

    #Green CG2

    green "Tsk. Tsk. You’re underestimating me quite a lot, aren’t you?"
    advmc "You drank their tea and ate the cake. How am I not supposed to underestimate you?"
    green "Hey, I did it to lower their guard, you know. And look. Because we got them to talk about their past a little, I regained control of this place."
    advmc "You… didn’t look like you were thinking at all."
    green "This is when you’re supposed to praise me!"

    menu:
        advmc "(Honestly, this guy...)"
        "Yes, yes. Good job.":
            $ greenap-= 1
            green "Can’t you put some heart?"
            advmc "I couldn’t help but to be dumbfounded by the sheer amount of stupidity that you’ve displayed."
            green "Argh, you’re the worst!"
        "I can’t believe you!":
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "Aw c’mon, is it that hard to praise me for a job well done?"
            advmc "You’re bleeding out! Every time you speak, you spew out more blood! You really want to talk about praises right now?"
            green "So you do care~"

    green "Well, now that this place is my playground, we might as well as play a little."
    advmc "Take care of the puppets for me then. Make sure you stay hidden from any attacks."
    green "Hey, before you go…"
    advmc "Huh? Don’t give me your necklace. This is supposed to keep you safe."
    green "Yeah, but you’re going straight into a fight without any other backup. Besides, you broke yours, right? So use this."

    menu:
        advmc "(Sometimes, Green is…)"
        "(... An idiot)":
            advmc "Stupid! Like hell I need it! But if I don’t have it, you’re going to get mopey and worried, right? Look. I’ll show you that I don’t even need it!"
            show greenapprove at appsprite
            play audio "sfx/hand-bells-d-single.mp3"
            $ greenap+= 1
            green "Yeah, yeah. You’re the mighty fox."
            advmc "Damn straight."
            $numjewels=3
        "(... An annoyance)":
            advmc "I appreciate the thought, but I don’t need it. I’m stronger than you. Therefore, you should use this to protect yourself."
            green "Don’t be like that. C’mon. Think of it as just a way to relieve my worry."
            advmc "Nonetheless, I don’t need it."
            $ greenap-= 1
            green "You’re such an idiot."

    #nvl set up
    nvl clear
    window show

    hide g

    nvlmc "Is Green’s Zone really doing anything? I can’t tell from here."
    nvlmc "It looks like there's more than just the puppets, though. The fog really makes it hard to tell. But hiding can only help them so much when I'm on the hunt."
    nvlmc "I feel calm. I have enough of my wits on me to be able to properly think this through. This time, I won't be rash."
    if numjewels>0:
        nvlmc "And on top of that, I have this necklace to protect me. What a thought. Being protected by Green, huh? Thanks Green. I won't disappoint you."
    nvlmc "Well, better go cause some destructions. I'll show them exactly why you don't underestimate a fox!"

    #escape nvl mode
    nvl clear
    window hide

    scene bg greenroom with fade
    show particleFog1:
        alpha 0.8

    #Hunt Mode!
    #Hunt Mode Music
    play music "music/Chris_Zabriskie_-_07_-_Its_Always_Too_Late_to_Start_Over.mp3" fadein 1.0 fadeout 1.0
    call huntmodestart

    stop music fadeout 1.0

    scene bg greenroom with fade
    show particleFog1:
        alpha 0.8

    advmc "There you are! Don’t think you’ll get away!"
    show but anger at center with dissolve
    butler "What a persistent guest you are!"

    hide but
    #Begin Battle Music
    play music ["music/Ian_Alex_Mac_-_01_-_Battle_for_the_End_Zone.mp3", "music/Kevin_MacLeod_-_Broken_Reality.mp3"] fadein 1.0 fadeout 1.0
    #Battle Mode against Butler
    call battlebutler

label debug:
    #Play Green's Theme
    play music "music/Wolf_Nilson_Trio_-_04_-_Auf_der_anderen_Seite.mp3" fadein 1.0 fadeout 1.0
    scene bg greenroom with fade
    show particleFog1:
        alpha 0.8

    show but saddness at center with dissolve
    butler "Forgive me, my Mistress. Once again, I…"
    play audio "sfx/bone-crunch-fast.mp3"
    show dustparticle at center
    pause 0.8
    hide particleFog1
    hide but with fade


    advmc "That should have destroyed the puppets. Where’s Green? Hm?"
    advmc "(There’s a small green ball rolling this way. Did the Butler drop this? What even is this?)"
    #If this route has never been ran before, change it so that we've collected the green Orb
    if greenOrb == False:
        $numOrb=+1
        $ persistent.greenOrb = True
    show g temp at center with dissolve
    green "Hey Red!"
    advmc "Should you be yelling so much? What if you start bleeding again?"
    green "We need to go!"

    #nvl set up
    nvl clear
    window show

    nvlmc "I have no idea what this idiot did while I was taking care of the Butler. But it seems that the floor can no longer hold our weight. Or perhaps the problem was that the Butler himself was holding it up with his own Zone? "
    nvlmc "Whatever the case, I need to get us out fast."
    nvlmc "First, I rush back to Green’s side. It seems that he is no longer coughing up blood, which is a wonderful thing. But I don’t have time to focus on that."
    nvlmc "I reach to grab him, but he pulls back. "
    nvlmc "Is he serious? He’s going to draw a line about this again? His life's at stake here. Does he not realize that? Whatever. If he’s going to make that big of a deal, I’ll have to just settle for this."

    #escape nvl mode
    nvl clear
    window hide

    advmc "C’mon, let’s go."
    green "Eh? You’re not even going to hold my hand?"
    advmc "Do you want to get out of here or not?"
    green "Picky! I liked you better when you were getting all weepy that I was hurt."
    advmc "That never happened! Now shut up and focus on running. This place will collapse before we get out at this rate!"

    scene bg exitroom with fade

    #nvl set up
    nvl clear
    window show

    nvlmc "The room that we’re in shakes. It feels as if the floor crumbles the minute we step on it. If we’re even a second too slow, I fear that we’ll fall through."
    nvlmc "Green’s pace is not fast enough. "
    nvlmc "I think he realizes that himself, because his expression is grim. "
    nvlmc "Should I just ignore his wishes and just carry him through? But wouldn’t that make him resentful? "
    nvlmc "No, no. I should just trust that he can make it through this without any problems."
    nvlmc "That’s right. I should just trust him."

    #escape nvl mode
    nvl clear
    window hide

    show g temp at center with dissolve
    green "Even if you don’t say it, I know what you’re thinking."
    advmc "Is that so? That’s a relief."
    green "Yup. I know exactly what you’re thinking."
    advmc "(The way he said that is pretty worrying…)"

    #Door Background Change

    #nvl set up
    nvl clear
    window show

    nvlmc "The door is just ahead of us. It’s a big enough distance from where we are now that a normal human won’t be able to make it in one jump. But I should be able to if I push a bit."
    nvlmc "I won’t be able to make that jump if I’m carrying someone. But Green looks like he’s slowing down, and I’m starting to feel a little antsy on whether we’ll be able to escape. Well, it’s more correct to say that I’m worried whether he’ll be able to make it out alive."
    nvlmc "Should I just grab him and jump?"
    nvlmc "The minute I think that, the floor shudders. It looks like this floor is going to completely go under."
    nvlmc "No time to hesitate."
    nvl clear
    nvlmc "I know I won’t make this jump all the way to the door. But if I can get close enough, I will be able to push Green through."
    nvlmc "With that thought comforting me, I grab Green and jump."
    nvlmc "Surprisingly, Green doesn’t say anything. Is his condition bad? Should I have checked on that first? But there was no time. The floor is collapsing. We don’t really have the luxury of time to make sure that we’re both okay."
    nvlmc "Forgive me, Green. Once we’re out of here, I promise I’ll force Zero to buy you a new figurine. "
    nvl clear
    nvlmc "I’m just a few meters shy of the door. But the floor is already giving out here. We won’t have long to stand here before we fall through."
    nvlmc "If that door is locked, we’re screwed. Then it’ll be for the best that there is no door."
    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch
    scene bg exitroomhole with fade
    nvlmc "I gather just enough energy to blast a hole next to the door. I meant to destroy the door, but it seems that my aim isn’t good when I’m trying to balance Green in one arm while trying to land somewhere that won’t immediately make us fall through."
    nvlmc "It makes me a little bitter, but beggars can’t be choosers."

    #escape nvl mode
    nvl clear
    window hide

    #If Green's Approval Points are too low
    if greenap<2:
        play music "music/Chris_Zabriskie_-_03_-_I_Dont_See_the_Branches_I_See_the_Leaves.mp3" fadein 1.0 fadeout 1.0
        play audio "sfx/bone-crunch-fast.mp3"
        show whiteflash zorder 50 with vpunch
        advmc "(What? I’m bleeding? Why…?)"
        show g temp at center with dissolve
        green "Thanks for taking me all the way here. I got it from here on, though. "
        advmc "What…? Green? You…?"
        green "Hm? Are you really having that hard of a time to figure out what I did? It’s Strychnine. I heard it’s a deadly poison for foxes. Looks like it’s true. "
        advmc "Why… would you?"
        green "Are you seriously asking me that? Isn’t it obvious? You got exactly what you gave. In other words, it’s just karma."

        #nvl set up
        nvl clear
        window show

        nvlmc "Even if he says that, I don’t understand."
        nvlmc "Green pushes off from me and grabs the hole that I created in the wall. He glances back at me and gives me a mocking salute."
        nvlmc "It should make sense. It really should."
        nvlmc "But I don’t understand what has happened."
        nvlmc "Why am I falling backwards?"
        nvlmc "Why did he do this?"
        nvlmc "I don’t…"

        #escape nvl mode
        nvl clear
        window hide

        #Bad End CG
        $quick_menu = False
        $ persistent.greenbadend = True
        scene end greenbad with fade
        pause 2.0
        $ MainMenu(confirm=False)()

        #End Green Bad End

    #If Green's Points are Awesome, go to Green's Route
    if greenap>9:
        $ onGreenRoute = True #So we can toggle on the correct ending card
        show g temp at center with dissolve
        green "You know, no matter how you slice it, it’s too late for me."
        advmc "So what?"
        green "So let’s change the plan."
        advmc "Change? "
        advmc "(I don’t like where this is going.)"
        green "I’ll take this time to look for the others and make sure they’re okay. You go ahead and finish the mission."
        advmc "You’re not feeling well enough to go on, huh? That’s fine. I’ll finish things properly."
        green "Then I’ll leave it to you."

        #nvl set up
        nvl clear
        window show

        nvlmc "I wonder why I didn’t realize exactly what he meant until then. "
        nvlmc "Green twists out of my hold and allows himself to fall into the darkness of the floor below. I’m so startled that I can’t even react properly. As if realizing that, Green gives me a wide grin and a wink as he disappears."
        nvlmc "Is it selfish that I don’t even consider running after him? "
        nvlmc "But this is Green’s pride. "
        nvlmc "He sounded sure that he can survive to find the others. If that’s the case, then I should also focus on the mission."
        nvlmc "They will be fine. "
        nvlmc "I feel strangely content and confident."

        #escape nvl mode
        nvl clear
        window hide

        jump aftermath

    #Otherwise, Green's Points are Normal, so we'll go straight into the Normal Ending
    play music "music/David_Hilowitz_-_10_-_Missed_Connections.mp3" fadein 1.0 fadeout 1.0
    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch
    advmc "(Did this guy seriously just smack me? I’m trying to save his sorry life!)"
    show g temp at center with dissolve
    green "No matter how we look at it, it’s clear that I’m just a dead weight right now."
    advmc "So you have to hit me?"
    green "Drop me."
    advmc "W-what?"
    green "Right now, this place is still my Zone. Even if I fall, I’ll survive. So don’t worry about me and go."

    menu:
        advmc "(Damn this guy!)"
        "Like hell I can do that!":
            green "… If that’s how you feel, then I’ll just do this."
            play audio "sfx/dropping-wood-2.mp3"
            show whiteflash zorder 50 with vpunch
            advmc "Ow! Stop hitting me! You… you idiot!"
        "You promise you’ll be fine?":
            green "Yup! I’ll be fine 110%! So don’t worry about me."
            advmc "When you’re on solid ground, look for the others and keep them safe."
            green "Will do. You just worry your pretty head about that witch."

    #nvl set up
    nvl clear
    window show

    nvlmc "How bitter."
    nvlmc "Even though I swore I’ll be the one to protect them, It feels like I’m the one being protected. Why is it that no matter what I do? I’m never good enough?"

    if trueend:
        #escape nvl mode
        window hide
        play music "music/David_Hilowitz_-_Angle_of_Light.mp3" fadein 1.0 fadeout 1.0
        boss "You don’t get it, do you?"
        advmc "Get what?"
        boss "That desperate want to protect those close to you? It’s the same for everyone. Wanting to protect someone is a normal feeling that everyone feels."
        advmc "Who cares whether this feeling is mutual or not? I don’t like it."
        boss "Heh. Yeah. I hate it, too."
        advmc "… How do you deal with it?"
        boss "I don’t think there’s a real way to deal with it. When things happen, you’ll always regret all the things you did, even if it was the best thing you could have done. That’s something that probably won’t change, no matter how strong you become."
        advmc "I really hate human emotions."
        boss "Hahaha! Yeah, me too!"
        play music "music/David_Hilowitz_-_10_-_Missed_Connections.mp3" fadein 1.0 fadeout 1.0
        #nvl set up
        window show

    nvlmc "But we’re running out of time. I have to just trust Green to survive through this."
    nvlmc "He’ll be fine. He’ll be fine. He’ll be…"
    nvlmc "I repeat that like a mantra and release him. My hands shoot out and grab onto the hole in the wall that I created. And once I’m certain I’ll be fine, I turn back to see him."
    nvlmc "Green falls into the darkness of the floor below us. "
    nvlmc "For a second, I think I saw him smile."

    #escape nvl mode
    nvl clear
    window hide

    jump aftermath

label aftermath:
    play music "music/David_Szesztay_-_Paranoid.mp3" fadein 1.0 fadeout 1.0
    scene black
    #nvl set up
    nvl clear
    window show

    nvlmc "I make my way through the hole in the wall. This place is pitch black. It makes me a little anxious that I might have gone blind."
    nvlmc "As if understanding that, small willow the wisps appear around me, lighting the way. It looks like they want me to follow them. They're just leading me around by the nose, aren't they? "
    nvlmc "This is pissing me off. "
    nvlmc "Green is gone. I have no idea how the others are doing. But despite that, I can't stop here."
    nvlmc "At the very least, I need to make that damned witch cry before I head home."

    #escape nvl mode
    nvl clear
    window hide

    jump thirdfloor #And then we go to the 3rd chapter!
#return #We're done with 2nd chapter!
