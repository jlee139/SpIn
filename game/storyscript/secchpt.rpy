label secondfloor: #2nd chapter start!
    #First, we have the children joking around
    #scene bg stairway with fade

    show g temp at right with dissolve
    green "By the way, Rookie, you know that the whole 'SpIn' thing is a joke, right? No one actually calls us that."
    show r temp at center with dissolve
    rookie "... I... was not aware."
    show bl temp at left with dissolve
    blue "How many times do I have to tell you to stop confusing people? It's not a joke. SpIn is silly sounding, but it is still our name."
    "It's on our uniforms. Why would you lie about something so obvious?"
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

    nvlmc "On one such mission, we were interrupted by a witch. Since what we were taking care of at the time was time sensitive, we decided to ignore that witch for the time being to complete the mission."
    nvlmc "That was our mistake."
    nvlmc "The witch was personally offended by us and began to stalk "

    #escape nvl mode
    nvl clear
    window hide



return #We're done with 2nd chapter!
