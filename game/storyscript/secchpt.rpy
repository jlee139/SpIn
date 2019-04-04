label secondfloor: #2nd chapter start!
    #First, we have the children joking around
    #scene bg stairway with fade

    show g temp at right with dissolve
    green "By the way, Rookie, you know that the whole 'SpIn' thing is a joke, right? No one actually calls us that."
    show r temp at center with dissolve
    rookie "... I... was not aware."
    show bl temp at left with dissolve
    blue "How many times do I have to tell you to stop confusing people? It's not a joke. SpIn is silly sounding, but it is still our name."
    "It's on our uniform. Why would you lie about something so obvious?"
    green "Oh, shut up! It's a stupid name! I can't believe it stuck! "

    #Since we already explained boss
    if trueend:
        rookie "But is it not the name that Boss gave?"
        "It is. And most people are respectful enough to keep saying SpIn."
        green "It's so undignified!"
        blue "No one cares what you think, Green."
        rookie "Excuse me for asking, but is there something wrong with Boss?"
        green "..."
        blue "Well, you'll hear more about it in detail later. But the gneral gist is-"
        "Let me explain."

    else:
        blue "No matter how stupid it is or how silly it sounds, respect Boss's wish for wanting that to be our name."
        rookie "Boss? He is the one who gathered the Supernatural Investigators, correct?"
        green "Oh, that's right. You probably haven't met him, huh?"
        rookie "What kind of person is he?"

    "He was the one who used the codename 'Red' first. And because of how short-staffed we were, he and I parntered up to take care of missions..."

    #nvl set up
    nvl clear
    window show

    nvlmc "I don’t want to think about it. I don’t want to remember what happened. But if I don’t keep it clear in my own head, then that witch’s curse will come to fruition."
    nvlmc "On one of our missions, we were interrupted by a witch. Since the mission was time sensitive, we decided to ignore that witch for the time being to complete the mission."
    nvlmc "That was our mistake."
    nvlmc "The witch was personally offended by us and began to stalk us. I didn’t even notice. But he did."
    nvlmc "He went out of his way to never use our names.But I assumed that he was fooling around as usual. The witch just had to wait until I said his name. And the curse was cast."

    nvl clear

    nvlmc "What was the curse? Well, if I knew that, it would make breaking it much easier."
    nvlmc "We think it's the curse that put Boss in his coma-like state. But it's also possible that he's actually on a middle of a mission in the dream world or whatever, too. Since none of us are sure about that, we've just taken to leaving him alone in his room."
    nvlmc "But what we do know for certain is that none of us can remember Boss's name. We tried looking it up in the Supernatural Investigation Database that Boss put together, but his name comes up all scrambled and wrong. All the paperwork he signed comes up the same way."
    nvlmc "Giving one's name away is a huge deal as it is. But to have it stolen like this? The best case will be that he wakes up and everything is fine. The typical cases like this, though, ends with the one whose name has been stolen never waking up. And the worst case would be that the person's body becomes a puppet for the caster of the curse."

    #escape nvl mode
    nvl clear
    window hide

    "And then as if to mock us all for this, the witch scrambled our memories of that time. We all know that there was a witch and a curse was casted on Boss. But none of us can tell you more details outside of that."
    rookie "That... sounds rough."
    blue "But if we are dealing with a witch here, then it's quite perfect for us."
    rookie "How so?"
    "We might be able to... {i}convince{/i} her to help us break the curse."
    green "H-hey, your face looks super evil right now!"
    blue "Or we might be able to prod her into figuring out which witch cursed one of our own."
    rookie "I thought Boss was just a recluse who had too much paperwork. There was actually a reason why he never left his room."
    green "..."
    blue "..."
    "..."
    rookie "..."
    rookie "T-That was a joke."
    "H-huh?! You can tell jokes?"
    "(Ack, maybe that was too mean. He won't meet my eyes.)"
    blue "W-well anyways, let's just focus on getting to that witch for now."

    #nvl set up
    nvl clear
    window show

    nvlmc "We climb up the stairs to the second floor. The wood of the mansion look old and rickety. To be honest, I’m shocked that they can hold our weight. "

    window hide
    #scene bg upstairsent with fade

    window show

    nvlmc "Although the air on the first floor didn’t feel stale thanks to some form of air flow, it didn’t seem to be the case for the second floor. I make the others wait at the top of the stair. Then I turn my attention to the wooden floor. Taking a deep breath, I take a tentative step forward."
    nvlmc "The good news is that the floor thus far seems to be able to hold my weight. I motion to the others that it’s safe enough. They slowly make their way over."
    nvlmc "There are three doors in the hallway before us. Although it looks as if there should be more rooms, it looks like there’s something preventing us from seeing more than this."

    #escape nvl mode
    nvl clear
    window hide

    blue "Looks like they’re welcoming us with a trap."
    green "Nothing we’re not used to."
    "Since there’s three doors, one of us should double up."
    "(I want to tell Rookie to stay behind. But I don’t think he’ll listen to me if I say it.)"
    blue "Red, you broke your necklace earlier, right? Why don’t you decide which of us you’d rather go with?"
    "H-huh? Me?"
    green "Can’t have our precious tank get a boo-boo. "
    "Ugh. You have the worst phrasing."
    blue "But it’s the truth. It’ll be best that you pick someone you feel the most comfortable fighting alongside."
    rookie "Sounds good to me."

    menu:
        "Alright, then... "
        "Green, you’ll cause the least amount of trouble next to me.":
            $ greenap+= 1
            jump secgreen
        "Blue, I trust you the most.":
            $ blueap+= 1
            jump secblue
        "Rookie, would you be alright with me?":
            $ rookieap+= 1
            jump secrook
        "I’ll be fine on my own." if trueend:
            $bossap+=1
            jump secsolo

    "Let's go!"


label secsolo:
    "This is only available once you've cleared everything else."
return





return #We're done with 2nd chapter!
