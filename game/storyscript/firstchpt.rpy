label firstfloor: #set up of the rest of the story
    #nvl set up
    scene mansionentrance with fade
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

    #Turn on our fog
    show particleFog1:
        alpha 0.5

    #children being cute now
    "Ready?"
    show bluetemp at left with dissolve
    blue "Want a candy? It’ll help you with your nerves."
    show greentemp at right with dissolve
    green "Don’t tell me you’re getting cold feet? Jeesh, what will we do with you? If you’re like this, how’d you think Rookie here feels?"
    show rookietemp at center with dissolve
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
    scene fronthall with fade
    #Turn on our fog
    show particleFog1:
        alpha 0.5

    window show
    nvlmc "I can see why the previous owners tried so hard to restore the mansion."
    nvlmc "The entrance area is huge. The broken chandelier hanging looks to be one of the newer addition. There’s a spiral staircase against the wall leading up to the second floor. The chandelier looks to be at eye-level with it. Perhaps one of the previous owners broke the ceiling to put the chandelier like that?"
    nvlmc "There appears to be a giant ripped portrait under the staircase. It doesn’t look like there’s a way to go that way. But there are two hallways, one on either side of us, that seems to lead to other parts of the mansion."
    nvlmc "The way to the left looks to lead to a dining area with a long table. The way to the right looks to have been caved in by some kind of rubble. Was it due to the activity of the ghost? Or was this done by construction that was halted eventually?"

    #end nvl
    nvl clear
    window hide

    "It feels like it’s bigger on the inside than out."
    show greentemp at right with dissolve
    green "I... hate to say this, but it’s too large of an area for my ability to cover."
    show bluetemp at left with dissolve
    blue "I’ll put up a seal."
    show rookietemp at center with dissolve
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
    green "Ugh. Don’t make me spread my area so thinly. The furthest I can go is to the doorway... Hey, are you listening?!"

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
    scene portrait with fade
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
    "(Did he read my mind...?)"
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

    scene fronthall with fade

    blue "You know you don’t have to stay here with me. If there’s trouble, Green will let you know."
    "Do you want me to leave?"
    blue "No, no. I just... thought you’d rather explore."
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
    "I don’t treat you like a kid, Blue. At best, you’re more like... "
    blue "Like...?"
    "(That’s funny. I can see my breath? Tch. That means-)"
    green "Sorry to interrupt, but we’re being attacked!"
    "Blue, get that seal up. I’ll deal with this!"

    jump firstambushed

label firstambushed:
    scene fronthall with fade

    call begin_ShootMode #Our Shoot Mode
    call begin_TutRPG #Our Battle Mode Tutorial version
    jump introToWitch

label introToWitch:
    scene fronthall with fade

    prewitch "You... What the hell are you people?"
    blue "What a soft life you must have lived if a ghost such as yourself aren’t familiar with us."
    green "I’m shocked as well. To think there exists spirits who do not know of us."
    rookie "We are Supernatural Investigators. "
    prewitch "Investigators? "
    prewitch "Ha... haha... Hahahahahaha!"
    prewitch "So you came to kill me? Is that it?"
    "(What’s with this rising aura? Has she been hiding her power?)"
    "Get back! She’s going to-"

    show whiteflash zorder 50 with vpunch

    #nvl set up
    scene fronthall with fade
    window show

    nvlmc "Not good. I underestimated her. I should have taken her seriously from the get-go."

    if trueend:
        #end nvl
        #CG????
        window hide
        boss "Hehe... I guess I overestimated myself a bit."
        "Shut up, you idiot! You knew I can take that blast! Why did you jump in front of it?"
        boss "Well, it’s just... kind of rare for me to protect you, you know? Thought I’d take advantage of it."
        "Hey, next time you get an opportunity like this?"
        boss "Yeah?"
        "Don’t."
        boss "Hehe. That kind of rough side of you is cute, too."
        "Didn’t I tell you to shut up?"
        window show

    nvlmc "Damn it. I thought she was just a spirit, but it seems that she has power behind her. Is she the ringleader here?"
    nvlmc "First priority is to protect everyone. "
    nvlmc "Unlike them, I’m durable enough that I can probably survive a blast or two if she starts flinging this dense energy at me. If the others got even scratched with something like this, they’d probably evaporate."
    nvlmc "But can I take the hit without letting even a stray hit get near them? Then the only other way to perfectly protect everyone would be..."
    nvl clear
    nvlmc "I clutch the three jeweled necklace. Since this has a fairy’s blessing, it should work."
    nvlmc "Without hesitation, I rush towards the spirit, the necklace clutched tightly in my hand. Seeing me move, the spirit turns her whole attention to me."
    nvlmc "Good."
    nvlmc "I hope this doesn’t hurt too much."

    show whiteflash zorder 50 with vpunch
    nvl clear

    nvlmc "Unsurprisingly, she starts firing as soon as I get airborne to go after her. Makes perfect sense. People can’t change directions mid-air. I’ll have to allow myself to get hit."
    nvlmc "But you know, she underestimated me quite a bit."
    nvlmc "Did she really think that this is my best?"
    nvlmc "There’s a crackle of power that envelops me just in time as her blasts hit. I’ve done this too often to mistime this."
    nvlmc "My ability."
    nvl clear
    nvlmc "Well, to call it my ability is actually misleading. It’s a part of who I am, after all. But it’s not like there’s any better way to describe it. To any other Supernatural Investigators, it’ll be considered their ability."
    nvlmc "In the Eastern sector, there’s a famous onmyouji (I suppose the closest translation would be an exorcist) by the name of Abe no Seimei. According to legends, his mother was a beast called the “Nine-tailed Fox.” A fox is supposed to gain an extra tail for every 100 years it lives. So to have nine of them, that fox must have lived for a long time while collecting wisdom and power. Because of his lineage, Abe no Seimei was an undefeatable man."
    nvlmc "I’m not going to say something so grand like I am a descendent of Abe no Seimei. "
    nvlmc "But there’s probably some traces of his blood in my vein."
    nvlmc "Otherwise, I have no real words to describe this form of mine."

    #end nvl
    nvl clear
    window hide

    #FOX CG
    prewitch "You think a little form change is enough? "
    "(It looks like she’s gathering her energy for a bigger blast. Then I’ll just cut her off before she releases!)"

    #nvl set up
    #scene mansionentrance with fade
    window show

    nvlmc "I’m faster in this form. Stronger, too."
    nvlmc "But somehow, it seems she still hasn’t shown her true powers yet. Because she manages to summon smaller blasts while still gathering energy for a larger one. That’ll be fine if not for the fact that I cannot allow my comrades to get hurt."
    nvlmc "I guess my weakness was too obvious, seeing that she seems to be aiming for them now."
    nvlmc "Like hell I’ll let her do what she wants!"
    nvlmc "The three jewel necklace has been blessed by fairies. The typical usage of something like this is as a protection charm from a surprise attack. But there are other ways to use it, too."
    nvlmc "For example, I can crush it in my hand for an extra boost of power. It also means that I won’t be able to rely on this any more, but if I can keep these guys safe..."
    nvlmc "What’s a little sacrifice, right?"

    show whiteflash zorder 50 with vpunch
    nvl clear

    nvlmc "Her screams of pain fill the air as I fall back into Green’s hold. He helps steady me as Blue finishes his seal. Rookie seems too frazzled to properly move. We’ll have to talk to him later to better protect himself in these situations."
    nvlmc "At least with the seal finally finished, she won’t be able to run out of this mansion. If we finish her in here, that will be it."
    nvlmc "I turn towards her. It looks like she’s struggling to hold this form together. Just a little more push should be enough to kill-"
    nvlmc "My knees give out. Huh? Did I use more power than I realized? "
    nvlmc "I stumble as both Blue and Green help steady me on either side. This is bad. If I don’t finish her off right now, she’ll get the chance to recover and come after us. We need to stop her here."

    #end nvl
    nvl clear
    window hide

    prewitch "Haha... looks like you’re at your limit."
    green "Is she gathering another projectile? Wouldn’t that destroy her?"
    blue "Looks like she plans on killing herself with us."
    "Any chance you guys can kill her?"
    green "Very encouraging to hear from our only fighter."
    blue "Rookie looks terrified, too. Tch. We need to run."
    prewitch "I won’t let you!"
    "Heh. Got you."

    show whiteflash zorder 50 with vpunch

    green "How did you miss at that distance?!"
    "(I didn’t! She pulled back at the last second. Is she prioritizing survival?)"
    prewitch "Are you stupid? Why would I make it that easy for you to kill me?"

    #nvl set up
    window show

    nvlmc "The wind kicks off. I must be really weakened, if that little is enough to knock me back into Blue’s arms. At least it looks like Blue has some kind of a minor seal up around us. But if she fires something at us, it won’t last. And I don’t have my necklace to protect me anymore."
    nvlmc "With another cackle, the witch flies up the staircase and through the gaping hole of the second floor’s entrance. She doesn’t put up a seal to stop us from entering, which already tells me that the second floor must be filled with traps."
    nvlmc "The gust dies down."
    nvlmc "We seem to have returned to relative peace."

    #end nvl
    nvl clear
    window hide

    green "Oi Rookie, how long are you going to stand dumbly over there?"
    rookie "..."
    blue "You alright, Red? You look pale."
    "Yeah. Just tired."
    green "Hey Rookie, aren’t you our medic? Get to it."
    rookie "R-right."
    "(He looks shaken. Was too much for his first mission?)"
    "Hey, sorry if I scared you. You probably didn’t expect that, right? I’m part… er… I suppose the best way to say is that I have some fox blood in me."
    "Don’t worry; I don’t lose control or anything. That version is still me. Just… more powerful."
    green "What’s with that? He has our files. It’s our own responsibility to read about our teammates’ abilities before a mission."
    blue "Amazing. Have all of my lectures finally sunk in for you? Or are you just echoing them to look cool in front of a new member?"
    green "Shut up, you."
    rookie "I am not scared."
    "Is that so? That’s a relief."
    rookie "Just..."
    green "Just?"
    rookie "Three years ago, my village was attacked by a silver fox with two tails."
    blue "Three years ago? Wasn’t that…?"
    "If you were wondering if that was me, then yeah. It was. There haven’t been any other silver foxes, let alone two-tailed ones, in about half a century."
    green "Urk. You couldn’t think of a kinder way to phrase that?"
    "Look, I’m not a good person. I’ve done many things I’m not proud of. If that makes you uncomfortable, request that you never be put on the same team with me again."
    "But for this mission, I need you to set aside whatever issues you have and work with me."
    rookie "..."
    "(Hey, say something!)"
    blue "Or if you guys want, I can drop the seal right now. It would mean that our mission is a failure, but at least no one would be forced to work with someone they are uncomfortable with."
    rookie "I... am fine."

    menu:
        "(You don’t look fine at all! Great. Now everyone’s looking at me to decide.)"
        "Let’s call it quits":
            jump storyendEmptyHands
        "We can’t give up yet":
            jump firstfloorcont

label storyendEmptyHands:
    "It’s clear that you’re uncomfortable, Rookie. It’d be better for a different team to take care of this mission."
    green "But doesn’t that mean that the ghosts here might relocate?"
    "(Look, I don’t like it either. But I’m not going to force Rookie here to spend time with a monster that wiped out his village. If he’s talking about {i}that incident{/i}  three years ago…)"
    blue "At least the next group will have a better heads up about what’s here. "
    rookie "If you decided this because of me, I ask that you reconsider."
    "(You say that, but you look the most disturbed by the whole thing.)"
    "It’s not because of you. I’m too tired to keep going. Not to mention, I broke my necklace. You want your only fighter to face against whatever else is in this mansion without any kind of protection?"
    green "You’re a monster, so I’m sure you’ll be fine."
    "(Get a hint, you idiot!)"
    "What’s that? You want me to accidentally hit you?"
    blue "If that’s how Red feels, then that’s how Red feels. Go ahead. Punch Green all you want."
    green "H-huh?! Wait a minute!"

    #nvl set up
    window show

    nvlmc "I feel a little guilty for abandoning the mission before it even started."
    nvlmc "But I doubt Rookie wants to be stuck in here for however long it’ll take for us to complete the mission with me. Not to mention I’m not confident about fighting that spirit again without the help of any necklace."
    nvlmc "I can’t allow any of these guys to get hurt. If I were to fight that spirit seriously, all of their lives would be at stake. "
    nvlmc "It’s better like this."
    nvlmc "Yeah, that’s right. This was the correct choice to make."

    #end nvl
    nvl clear
    window hide

    #Bad End CG
    #End EmptyHands

label firstfloorcont:
    $ blueap+= 1
    $ greenap+= 1
    $ rookieap+= 1

    "We can’t let a strong spirit like that relocate. That’d cause a bureaucratic mess that will doubtlessly end up with us pulling multiple all-nighters to handle."
    green "Oh, please let’s not do that again."
    blue "Whose fault was it that we were in that position to begin with?"
    green "C-come on, we all suffered together. So don’t blame it all on me!"
    "So if we can, I would really like to complete this mission. "
    rookie "That is fine with me."
    "(Are you really okay? You look pale.)"
    "That spirit was really powerful. If you guys are near me when I fight her again, I can’t guarantee your safety. So-"
    green "That’s fine. We’ll stay near the back. "
    blue "I’ll be focused enough to set up a better seal around us this time. Don’t worry about us and go full out."
    "(I’m saying if I do, you’ll die.)"
    rookie "I will trust your judgement."
    "(All of you suck.)"
    "(But this is the first.)"

    if trueend:
        boss "Pwhahahaha! What expression is that supposed to be?"
        "S-shut up! I don’t know! I don’t know what I’m feeling!"
        boss "Tsk, tsk. You’ve spent this long with humans and still can’t figure out emotions? I thought you foxes are supposed to be smart!"
        "Being smart and knowing your emotions are different things. "
        boss "[mcname], emotions are simple. If it’s a positive feeling, you smile. If not, you cry. See?"
        "I-I don’t know. Is this… positive? I can’t figure it out."
        boss "Do you hate it?"
        "N-no? I don’t think so? I don’t understand myself."
        boss "Then what about this? If you don’t know what you’re feeling, then just laugh."
        "What kind of logic is that?"
        boss "Once you laugh, it gets easier, you know. If it was a negative feeling, you’ll suddenly feel a lot better. If it was a positive feeling, it’ll make you feel doubly better for sharing it."
        "That… sounds fake."
        boss "H-hey! I’m trying to give you some sound advice!"

    "Pfft… Hahahahaha!"
    green "Nice going, Rookie. Red’s lost it because of you."
    blue "A-are you alright?"
    rookie "..."
    "I will make sure all of you get back safely. Until then, will you trust me?"
    green "Were you hit on the head while fighting? What’s with such a gross question?"
    blue "Did you forget, Red? We are a team. As much as we trust you, you should trust us."
    rookie "... I... I will leave it to you."
    "Good. Then our next objective is the floor above us. I have no idea what’s waiting for us up there, but I will keep you safe. If you can’t trust me, please feel free to stay here."
    green "I’m telling you, stop being so gross! "
    blue "I’ll layer so many seals around you that no one will be able to touch you. Heh."
    rookie "Then shall we?"

return #Back to story
