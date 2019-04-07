#Green Route Here
label secgreen:
    show greenapprove at appsprite

    green "Your phrasing is worse! Can’t you just say that you’re dazzled by my ruggedly good looks instead?"

    menu:
        "(Oh, please! Like you're all that!)"
        "Rookie, here’s another patient for you!":
            show greenapprove at appsprite
            $ greenap+= 1
            green "So you don’t deny my good looks!"
            "You’ll never be able to settle down if you treat everyone you meet like this!"
            green "It’s fine since you’ll be with me."
            "Says who?!"
            green "Oh jee, I don’t know… Maybe the little fox who is determined to save my life?"
            "I-I’m trying to save everyone, n-not just you!"
            green "Haha! You’re stuttering! That’s adorable!"
            blue "If you guys can please focus. You're scaring Rookie."
            rookie "I am fine."
        "Like hell. If you’re good looking, then I pity those who are considered ugly.":
            $ greenap-= 1
            green "What’s with that? I’m plenty good looking! You just have rotten eyes."
            "You sure it’s not your senses that’s rotten?"
            blue "Stop fighting, children."
            "We’re not children!"
            green "Red’s the one being rude. Stop blaming it on me."
            rookie "Would you rather pick someone else?"
            "(Ah, what am I doing, worrying Rookie? Tch. What was I thinking, picking this idiot of a guy?)"
            "Don’t worry about it. We’re always like this."


    green "Alright, then we’ll take this door. Try not to slow me down, Red."
    "Hilarious coming from the guy who could barely keep up with my pace."
    blue "Are you two sure you want to team up?"
    rookie "If you want to change-"
    "We’ll be fine. Sorry for worrying you."

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
        alpha 0.8

    #escape nvl mode
    nvl clear
    window hide

    "Green!"

    menu:
        "(Hehe. Green's weakness is-)"
        "I’ll go with you to that concert you talked about!":
            "..."
            "(Did it not work?)"
            show g temp at center with dissolve
            green "Hey… Didn’t I already tell you? Someone with zero music sense like you will never fit in at a concert."
            "(I guess it worked. But why does he look so mad?)"
            $ greenap-= 1
        "I know who broke your favorite figurine!":
            "(Ugh. What horrid stench. That must be-)"
            show g temp at center with dissolve
            green "Who was it? It was that damned Zero, wasn’t it?"
            "(... his cigarette.)"
            "(Sorry, Zero! I’ll make it up to you when we see each other again!)"
            "You already knew, huh?"
            show greenapprove at appsprite
            $ greenap+= 1
            green "I’m going to kill that brat!!"

    green "But why are you in here already? I didn’t give you any signal to come in."
    "What are you talking about? I heard you call out for help."
    green "Me? Ask for help? What dimension are you living in?"
    "This coming from the guy who screamed like a little girl when we were watching a horror movie?"
    green "Hey! Jump scares are a different thing!"
    "(... The fog around us thickened just now, didn’t it? Ah, how troublesome. I hate fighting blind.)"
    green "Red..."
    "Yeah. This fog isn’t yours, is it?"
    #Butler
    prebut "Astute observation, my esteemed guests."
    green "Alas, my smoke isn’t that thick. I’m not the type to keep things in until I can’t take it anymore, after all."
    "If that was supposed to be a dirty joke, I’m afraid it flew over my head."
    green "But you recognized it as a dirty joke. So it’s my victory, I’m afraid."
    prebut "Ahem."
    "But can you really claim victory when your jokes fall this flat?"
    green "You’re such a sore loser! Why can’t you just admit that I won?"
    "When you’ve actually won, I’ll acknowledge it. Until then, keep trying!"
    prebut "Hello? Do you not see me?"
    green "Do you not have eyes or something? Can’t you see that we’re talking? "
    "Honestly, have some more manners!"
    prebut "I-I apologize."
    "(Huh? Wait. There shouldn’t be a third person here!)"
    "Who are you? Are you the cause of this fog?"
    prebut "Astute observation, my esteemed guest!"
    green "Didn’t you already say that?"
    prebut "You noticed? But you didn’t say anything? My, the esteemed guests this time seems to like cruel jokes."
    "I prefer the term ‘rude.’"
    green "Of course, you would."
    "It’s what I use to describe you, after all."
    green "Hilarious coming from the fox who bites people’s fingers."
    "I told you to stop trying to put your finger in my mouth when I’m sleeping! I gave you a warning!"
    prebut "Can we please move on…?"
    "You done yet?"
    green "I’ve been done for a while, actually."

    menu:
        "(Then say it sooner!)"
        "Why wouldn’t you say that earlier?!":
            $ greenap-= 1
            green "It was obviously to see how good you are at keeping up with me. Unfortunately, Red, you failed."
            "Consider the people who have to put up with your prattles the next time you decide to keep silent."

        "Are you stupid? That could’ve put both our lives in danger!":
            show greenapprove at appsprite
            $ greenap+= 1
            green "B-but you’re… You’re you. There’s no way that this little can put our lives in danger."
            "D-don’t just suddenly flatter me! "

    prebut "Ahem. As I was saying-"

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
    nvlmc "It’s not teleportation. It can’t be. At least, if it was, I’d have been forced to go along with him, since I made contact. The more likely scenario is that he was never standing in front of me in the first place."
    nvlmc "In other words, a fake. "
    nvlmc "Just how shot are my senses from this dense fog that I made such an elementary mistake?"

    #escape nvl mode
    nvl clear
    window hide

    green "Seeing that the fog is still here, I’m assuming you missed?"
    "No, I hit."
    prebut "Indeed, you did hit my puppet. But as you can see, it doesn’t mean much."

    #nvl set up
    nvl clear
    window show

    nvlmc "From the distance of the dense fog, I see bunch of silhouettes staggering towards us. Their movement is slow. I can only assume that these “puppets” as this guy had said can’t move too fast. Are they zombies? Ghouls? Are they really there or is it an illusion trick of the fog?"
    nvlmc "Just to check, I lunge forward to attack. The minute an attack hits, the “puppet” disappears in a puff of smoke. "
    nvlmc "Nothing solid, then. But it didn’t feel like just an illusion either. I get the feeling that they could actually do some damage to me if I let them get too close. "
    nvlmc "Feeling uneasy, I rush back to Green and pick him up. He’s heavier than he looks. But there’s no time to dwell on that. It’s important to see if I can get away from this mob approaching us."

    #escape nvl mode
    nvl clear
    window hide

    green "Hey! What the hell? P-put me down!"
    "Shut up, I’m trying to save our lives!"
    green "I dropped my cigarette. My Zone-"
    "With this much fog, marking your Zone with smoke is a bad plan!"

    #nvl set up
    nvl clear
    window show

    nvlmc "I think I finally found a wall. There’s no sign of the door, so it’s probably not in the direction that we came in from. Jeesh, just how big is this room? It didn’t look like much when we were outside."
    nvlmc "Green squirms in my grasp, so I finally set him down. He looks like he’s very much offended by the whole thing, but it can’t be helped. Saving lives comes before dignity."
    nvlmc "From here, the mob seems to be taking their time to come towards us. Their speed is too slow to actually be threatening, though. Then we should use this precious few time to figure out a way to defeat them."

    #escape nvl mode
    nvl clear
    window hide

    green "My Zone isn’t working, is it?"
    "Why are you asking me? Shouldn’t you know that best? It’s your ability."
    green "I can’t feel that mob. I didn’t even feel that guy when he appeared either. "
    "Is it the fog? Is it interfering with your ability?"
    green "Yeah, I think so."

    menu:
        "(He looks pretty down about this.)"
        "Ehhhh? So there are things that even the great you can’t do, huh?":
            show greenapprove at appsprite
            $ greenap+= 1
            green "Can you not? I’m serious here."
            "It's fine. We’re a team. Our purpose is to cover each others’ backs."
            green "… Yeah. You’re right. Guess I’m being sensitive for no reason."
        "It is what it is.":
            $ greenap-= 1
            "Yeah. I guess so."
            "(Huh? He seems upset about something. Jeesh, what a kid, being this sensitive.) "

    "Well, we should focus on figuring out how to defeat that guy anyways."
    green "I bet this place is his Zone, and we walked in without another thought. If he has already established it, then it explains why I wasn’t able to."
    "Hey, can you create those zombie like creatures?"
    green "Maybe if I had something more physical to work with… H-hey, you don’t think…?"
    "They disappear too easily to be made out of corpses. "
    prebut "That’s correct! My esteemed guests this time around are so smart. "
    "How long have you been there?"
    prebut "A good butler like myself is never too far from providing a necessary service!"
    green "A butler, huh? What? You used to work here or something? "
    butler "I am troubled to correct you, my esteemed guests, that I am still an employee of this mansion. If you have any issues, please feel free to inform me or any of my fellow butlers."
    "How do we get out of here?"
    butler "Oh, how terribly hurtful! My esteemed guests are already planning on leaving! Tell me, was our hospitality not enough? What should we do to improve the situation?"
    green "Hey, since you’re a Butler, aren’t you supposed to serve us tea and snacks?"

    menu:
        "(Huh? What’s this guy trying to do?)"
        "(Play along)":
            "I prefer coffee and cake. If the coffee isn’t bitter, I’ll send it back."
            show greenapprove at appsprite
            $ greenap+= 1
            green "Oh? Bitter coffee? Didn’t think you were the type to prefer bitter things. Are you trying to be an adult?"
            "Have you forgotten just how many tails I have?"
            green "Weren’t you asleep for a good 300 of those years? "
            "That’s still 100 more than you!"
            green "Haha! You have no idea how to do basic calculations, do you? "
            "S-shut up!"
        "(Stay Focused)":
            "What are you talking about, Green? Now is not the time to play around."
            $ greenap-= 1
            green "You have no tactical brain, do you? This is why you’ll never be more than a grunt worker."
            "As if you can go through missions like this by yourself. "
            butler "My dearest esteemed guests, I insist that you stay for tea!"
            "(Great. Way to go, Green. Now this guy is going to chase us to drink tea!)"
            "Alright. Fine. Get me the bitterest coffee."

    butler "Then please, leave it to us!"









return #We're done with 2nd chapter!
