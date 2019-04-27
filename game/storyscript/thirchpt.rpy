label thirdfloor: #3rd chapter start!
    #nvl set up
    nvl clear
    window hide
    scene bg thirdhall with fade
    window show

    nvlmc "The willow the wisps eventually lead me to a stairway that doesn’t look like the rest of the mansion. Either this place was created with magic and doesn’t exist in actuality, or this place was later created by one of the other owners. At this moment in time, I can care less which one it is."
    nvlmc "These guys think they can get away with tricking a fox? "
    nvlmc "I’ll show them exactly what kind of a monster they’re dealing with."
    nvlmc "In my anger, I fail to see the trap that’s been laid out for me."

    nvl clear

    play audio "sfx/electric-sparks-railway-a.mp3"
    show whiteflash zorder 50 with hpunch
    nvlmc "The first is an electric shock that shoots up from my foot. It’s not enough to knock me out of commission, but I think it would have for a normal human. Because soon after, I hear the high pitch whistle of arrows flying through the air."
    nvlmc "So that’s their plan."
    nvlmc "My body feels sluggish, but I’m not useless. I dodge the volley of arrows by jumping forward. Another shock of electricity greets me when my feet meets the ground. Is the entire stairway wired? Then how should I go about dodging this?"
    nvlmc "What if I used the walls?"
    nvlmc "I push off the ground once more before the arrows land. This time, my aim is the wall. It seems they weren’t expecting me to get creative. Because there are no more electric shocks. But this gives me more freedom to change my direction sharply."
    nvlmc "In no time, I arrive at the top."

    nvl clear
    window hide
    scene bg thirdhallclose with fade
    window show

    nvlmc "What? Do I just open this door? Is it wired to electrify me, too? I don’t particularly want to find out by getting shocked."
    nvlmc "So I do the only logical thing."
    nvlmc "I blast a hole through the door."
    window hide
    play music "music/Lee_Rosevere_and_Daniel_Birch_-_09_-_Halo.mp3" fadein 1.0 fadeout 1.0
    play audio "sfx/dropping-wood-2.mp3"
    show whiteflash zorder 50 with vpunch
    scene bg thirdhallbrokeclose with fade
    window show
    nvlmc "Then I walk in through."

    nvl clear
    window hide
    scene bg atticdark with fade
    window show

    nvlmc "The room looks like an attic of sorts that hasn’t been opened in ages. The air is completely stiff in here, although it’s now starting to move thanks to the hole. It’s dark, too. The only light at first is from the hole behind me."
    nvlmc "But slowly, the willow the wisps from before begin to file into the room, brightening it just a tad. Like this, though, I see the silhouette of that damned witch."
    nvlmc "In this kind of dark and stuffy place, has she been waiting for us to arrive? "
    nvlmc "I prepare myself for a fight and then pause."

    #escape nvl mode
    nvl clear
    window hide

    advmc "(Wait. Isn’t that...?)"
    show w temp at center with fade
    witch "Who let you in here?"
    advmc "Hm? Was this place supposed to be a secret? My, my, isn’t your guard too lax?"
    witch "How did you get in here?!"
    advmc "The willow the wisps led me. Quite loyal following you have here."
    witch "You... I’ll kick you out!"
    hide w

    play music "music/Chris_Zabriskie_-_07_-_Its_Always_Too_Late_to_Start_Over.mp3" fadein 1.0 fadeout 1.0
    #Call Hunt Mode
    call huntmodestart
    play music ["music/Ian_Alex_Mac_-_01_-_Battle_for_the_End_Zone.mp3", "music/Kevin_MacLeod_-_Broken_Reality.mp3"] fadein 1.0 fadeout 1.0
    scene bg atticdark with fade
    #Mini Fight 1
    scene bg atticdark with fade
    play music "music/Lee_Rosevere_and_Daniel_Birch_-_09_-_Halo.mp3" fadein 1.0 fadeout 1.0

    advmc "(She backed off?)"
    show w temp at center with fade
    witch "Get out. Get out. Get out! GET OUT!"
    advmc "(I see. She’s just trying to push me out of here. Guess whatever she’s hiding up here must be important.)"
    advmc "(Then I better destroy it.)"
    witch "Don’t you dare!"

    play audio "sfx/thud-falling-on-wooden-floor.mp3"
    scene bg thirdhallbrokeclose with fade

    #nvl set up
    nvl clear
    window show

    nvlmc "It seems I underestimated her again. "
    nvlmc "She pushes me out of there with pure force. If I hadn’t blasted a hole through the door, I would’ve collided with it. But as of now, it looks like I’ll fall straight into the electrifying stairs."
    nvlmc "Tch. Annoying."
    nvlmc "I fire a small blast below me to give me enough air to get me to the bottom of the stairs. It’s just enough to skip over the electric shocks, but it looks like the witch isn’t done with me. She follows after me with a crazed expression on her face."

    #escape nvl mode
    nvl clear
    window hide

    scene bg thirdhallbroke with fade

    show w temp at center with fade
    witch "You saw too much! I was just going to kill you, but now I’m going to make you suffer first!"
    advmc "Hah! I’d love to see you try!"
    hide w

    play music "music/Chris_Zabriskie_-_07_-_Its_Always_Too_Late_to_Start_Over.mp3" fadein 1.0 fadeout 1.0
    #Call Hunt Mode
    call huntmodestart
    scene bg thirdhallbroke with fade
    play music ["music/Ian_Alex_Mac_-_01_-_Battle_for_the_End_Zone.mp3", "music/Kevin_MacLeod_-_Broken_Reality.mp3"] fadein 1.0 fadeout 1.0
    #Mini Fight 2
    scene bg thirdhallbroke with fade
    play music "music/Lee_Rosevere_and_Daniel_Birch_-_09_-_Halo.mp3" fadein 1.0 fadeout 1.0

    show w temp at center with fade
    witch "You’re really annoying!"
    advmc "That’s my line! Just die already!"
    witch "I’m already dead, you dimwit!"
    advmc "Then stay dead like a good corpse!"
    witch "Like hell I can die when I haven’t accomplished anything yet!"

    #nvl set up
    nvl clear
    window show

    nvlmc "Her relentless attacks knocks me down to the ground. A small sound of chimes catch my attention. Chimes? Why are there...?"
    nvlmc "Oh, that’s right. I picked up that orb, didn’t I?"
    nvlmc "It makes soft chime-like noise as it rolls on the ground. Then it comes to an abrupt stop by the stairs. Despite being an inanimate object, perhaps it’s fearful of the electric shock, too?"

    #escape nvl mode
    nvl clear
    window hide

    witch "What are you looking at? Your opponent is me!"

    #nvl set up
    nvl clear
    window show

    nvlmc "I dodge her attack in time. But the orb isn’t so lucky. It shatters into dust, adding to the hundreds of years old dust that was already there. "
    nvlmc "That orb must have contained some magic, though. There’s something unsettling in the air. It makes the hair on the back of my neck stand up."
    nvlmc "The Witch doesn’t seem to notice that anything’s wrong. Perhaps this is something that as a fox, I can feel? Something-something animals can sense disasters before they happen kind of thing."

    if numOrb == 2:
        nvlmc "The magic seems to combine with something that’s already here. But the spark doesn’t seem to be enough."
        nvlmc "Something’s missing. If only I can figure out what..."
        nvlmc "But for now, I can’t count on whatever that was."

    elif numOrb == 3:
        nvlmc "The magic swirls in the air. It kicks away the dust, faintly taking a humanoid shape."

    else:
        nvlmc "Or maybe I put in too much faith in this."
        nvlmc "The magic settles into the air with the rest of the dust. I guess that’s that. "
        nvlmc "Tch. Wasted my time on nothing."

    nvlmc "Whatever that was won’t be any help to me now. Guess I better get serious. "

    #escape nvl mode
    nvl clear
    window hide

    witch "Looks like you’re finally out of comebacks!"
    advmc "No, I was just tired of goofing around. Why don’t we finish this?"
    witch "Gladly!"
    hide w

    play music "music/Chris_Zabriskie_-_07_-_Its_Always_Too_Late_to_Start_Over.mp3" fadein 1.0 fadeout 1.0
    #Call Hunt Mode
    call huntmodestart
    scene bg thirdhallbroke with fade
    play music ["music/Ian_Alex_Mac_-_01_-_Battle_for_the_End_Zone.mp3", "music/Kevin_MacLeod_-_Broken_Reality.mp3"] fadein 1.0 fadeout 1.0
    #Mini Fight 3
    scene bg thirdhallbroke with fade
    play music "music/Lee_Rosevere_and_Daniel_Birch_-_09_-_Halo.mp3" fadein 1.0 fadeout 1.0

    show w temp at center with fade
    witch "Noooo!"
    advmc "(Damn her! She keeps running before I can kill her!)"
    advmc "(No, no. That’s a good thing. I don’t know what her deal with the demon is. I should figure that out first, actually.)"
    advmc "(Ugh. How annoying.)"
    witch "No! No! No! How dare you? How dare you?"
    advmc "Repeating yourself isn’t going to change what happened. Face it. I’m stronger than you."
    witch "Why do you keep getting in my way?!"
    advmc "Because you’re dead. Dead things should stay dead. "
    witch "That’s something only those with privileged lives can say. If you didn’t get a chance to live, then why shouldn’t you get it after you’ve died?"
    advmc "What’s with that? If you lived a bad life, just live a better one in the next. There’s no need to drag others into your mess."
    witch "But that’s not fair! Why did it have to end like that? Why was it just us that suffered? Those bastards took everything and never once repented! So why is it just us?"
    advmc "Fair? Are you seriously complaining about fairness like some kid? What? Because it was ‘so unfair,’ you just had to make a deal with a demon?"
    witch "So what? What if it’s childish? What if I’m acting like a kid? They robbed all of that from me! So why can’t I do what I want now? If that means I’ll make a deal with a demon, then that’s my right!"
    advmc "Was that even worth it? Look around you. There’s nothing here. You’re literally standing on the graves of where you used to live. Isn’t that right, young Mistress?"
    witch "Mistress...? Ah... so you..."
    advmc "But really, what a waste of a deal with a demon. You seriously just asked to be brought back from the dead so you can be a spoiled brat?"
    witch "What the hell would you understand? "
    advmc "Hey, if I kill you, will you stay dead?"
    witch "You’re just like everyone else! You just want me to die! Why can’t anyone just try to understand?"

    menu:
        advmc "(Just like everyone else, huh? Isn’t that her own fault for being so damned selfish? I should...)"
        "Eliminate her":
            jump thirdeli
        "Spare her" if numOrb == 2:
            jump thirdspare
        "Exorcise her" if numOrb ==3:
            jump thirdexor
        "Reunite her" if trueend:
            jump thirdtrue


label thirdeli:
    advmc "Hah! Try to understand you? Why?"
    witch "W-what do you mean why? Aren’t you supposed to be an investigator? Aren’t you supposed to look into the mystery of what happened here? Aren’t you supposed to save us?"
    advmc "Save you? Don’t be stupid. What have you done that deserves saving?"
    witch "T-t-that’s-"
    advmc "\"Not fair?\" Why, my dear, what makes you think anything in this world is fair?"
    hide w

    play music "music/Chris_Zabriskie_-_07_-_Its_Always_Too_Late_to_Start_Over.mp3" fadein 1.0 fadeout 1.0
    #Call Hunt Mode
    call huntmodestart
    scene bg thirdhallbroke with fade
    play music ["music/Ian_Alex_Mac_-_01_-_Battle_for_the_End_Zone.mp3", "music/Kevin_MacLeod_-_Broken_Reality.mp3"] fadein 1.0 fadeout 1.0
    #Mini Fight 4 - Final
    scene bg thirdhallbroke with fade
    play music "music/David_Hilowitz_-_10_-_Missed_Connections.mp3" fadein 1.0 fadeout 1.0

    show w temp at center with fade
    witch "You’re... horrible... Ahhh... Why won’t anything... go my way?"
    advmc "Disappear silently. You’re not the only one who has ever suffered."
    play audio "sfx/bone-crunch-fast.mp3"
    show dustparticle at center
    pause 0.8
    hide w with fade

    #nvl set up
    nvl clear
    window show

    nvlmc "Her body disappears, leaving not even her sobs behind. Finally, peace and quiet."
    nvlmc "The area doesn’t disappear as I thought it would. I guess this is actually part of the mansion and isn’t formed using magic. But at least there doesn’t seem to be any other spirits left."
    nvlmc "Oh, I see."
    nvlmc "When she made her deal with a demon, she probably forcibly brought back all the residents of this miserable mansion, too. Now that she has been removed, all of them must now be able to rest. Well, I suppose that’s fitting. The Young Mistress found rest, so now all her servants can, too."
    nvlmc "Maybe they’ll finally be able to remodel this mansion and make it usable."
    nvlmc "But whether that happens is not my business."
    nvl clear
    nvlmc "I guess I’ll just retrace my steps. If I go back, I should be able to make my way to the entrance. I wonder if it’ll be okay to just jump down to the lower floors. No, if I do that recklessly, I might end up stuck. Then again, I could always just blast my way out of there..."

    if onGreenRoute:
        #Play Green's Theme
        play music "music/Wolf_Nilson_Trio_-_04_-_Auf_der_anderen_Seite.mp3" fadein 1.0 fadeout 1.0
        nvlmc "Ah, I recognize that terrible scent. What terrific timing. To think he was well enough to get up here..."
        nvlmc "The smell of cigarette fills the air as a light fog settles around me. I’m half tempted to point out that there’s no need for this. But I suppose this is his way of saying that he was worried. I’m a little touched, to be honest."
        nvl clear
        nvlmc "Few seconds after I smelled the cigarette, I see that stupid grin on his face. Just few steps behind him are Rookie and Blue. Good. He did as promised."
        nvlmc "Everyone looks like they’re okay, too. I guess they didn’t run into any troublesome spirits like Green and I did. I’m glad. I was worried that they wouldn’t be able to take care of themselves without me to absorb the hits."
        nvlmc "Perhaps I’ve overestimated my abilities?"

        #escape nvl mode
        nvl clear
        window hide

        show g temp at center with dissolve
        green "Yo, missed me?"
        advmc "Ehhhhh... A little less miss and a lot more worried."
        green "What’s with that? Can’t you be cute for once?"
        advmc "Depends. What constitute as ‘cute?’"
        green "Hm... Something like a little less snark and a lot more teary-eyed \"I miss you, boo!\""
        advmc "... You seriously don’t want me to do that."
        green "On second thought, yeah. You’re right."
        show r temp at center with dissolve
        rookie "..."
        show bl temp at left with dissolve
        blue "In case you forgot, we're here, too."

    else:
        nvlmc "The shifting of the air catches my attention. Because of how stale the air is in here, it’s easy to notice the slightest of disturbances. Or perhaps that’s because my senses are sharper than that of a human? That Witch seemed shocked that I made it up here, after all."
        nvlmc "I tense. "
        nvlmc "Was I wrong? Did all the inhabitants of this mansion not return along with the Witch? Or could it be that other spirits and creatures have made their homes here as well? If that’s the case, then I have to fight some more? "
        nvl clear
        nvlmc "Can I even keep fighting? I used everything that I had to fight against the Witch. I’m not sure if I have enough left over to push through. In this state that I’m in, can I truly manage to survive? Even worse, how are my comrades doing? Have they been able to fight against these enemies and survive?"
        nvlmc "If it turned out that I was too caught up fighting that Witch to properly protect them, then I..."
        nvlmc "What should I do to beg for their forgiveness?"
        nvlmc "I feel the presence of others before I hear their footfall. Two...? No, three. One is limping. I should quietly and quickly get rid of them."
        nvl clear
        nvlmc "I turn, ready to slay whatever may come this way. And freeze."
        nvlmc "Green is being supported by Rookie. Blue takes the lead, his hands up to counter anything I throw at them. They look at me with distrust. Not that I can blame them. They probably thought I was going to kill them."
        nvlmc "Ahhh, what a horrid misunderstanding. So much for earning Rookie’s trust. Isn’t this pushing myself further in his mind as a monster that destroyed his village?"
        nvlmc "I want to cry. But I need to first clear this up."
        nvlmc "I raise my hands in the air to show that I mean no harm. "

        #escape nvl mode
        nvl clear
        window hide

        advmc "It’s good to see that you guys are okay."
        show g temp at right with dissolve
        green "Yo! Guess who?"
        show r temp at center with dissolve
        rookie "..."
        show bl temp at left with dissolve
        blue "You really scared us there. We weren’t sure if you were really you or if you were an imitation. An imitation would be easy enough to deal with. But if it was really you and you decided to kill us... "
        advmc "I wouldn’t! "

    advmc "A-anyways, are all of you okay? "
    rookie "I made sure that everyone is fine."
    green "We’re just tired at best, i imagine. Blue, put your seal down. Let’s get out of here."
    blue "Before we do that, we should make sure that this place is free from spirits. "
    advmc "They’re all gone. I can guarantee that."
    rookie "Rookie	Did you... kill them all yourself?"
    advmc "(He looks nervous. Do I seem like a monster?)"
    blue "I bet it was more along the lines of you got rid of the Witch, and it forced all the other creatures and spirits to disappear. "
    advmc "Got it in one."
    green "But is that alright? Didn’t you want to interrogate her to find information for Boss?"
    advmc "That’s fine. We’ll just find another witch. Besides, I doubt this one would’ve been able to help us with that. She seemed too selfishly set in her way to consider helping others."
    rookie "I wonder who she was. I thought we’d look more into the why of this mansion and the spirits within it."
    blue "I understand your curiosity, but you’re confusing our objective. We of the SpIn were tasked to investigate and to rid of any malicious spirits residing here. It doesn’t matter to us why these spirits are here or what their motivations are. "
    rookie "... I see."
    advmc "But if you’re still curious, I think I have it figured out. That Witch was a Young Mistress who owned this mansion long ago. Due to her young age and naivety, she lost this place to greedy outsiders."
    advmc "She probably made a deal with a demon to relive her easy life with her servants. That’s why everyone disappeared once she was gone."
    blue "Oh, I’m quite impressed you put that all together. Want me to give you a candy?"
    advmc "I’m not a child!"
    green "Well, whatever the case is, once our tank here destroys them all, our mission’s more or less over. Pretty simple of a job, ain’t it, Rookie?"
    rookie "Yes, it is."
    green "In fact, it’s so easy that whether you are there or not, we can take care of it all ourselves!"
    blue "I think you should shut up now, Green."
    advmc "Uh... I-I’m sure you don’t really want to hear me ask it, but... d-do you think you want to keep working as SpIn?"
    rookie "I am not sure why I would not want to hear you ask it. But I do not mind staying."
    advmc "Is that so? What a relief!"
    rookie "I must profess I do not understand your concern."
    green "Tch. Like that’s hard to tell. None of us can heal ourselves. But just saying, this is a special case and we really don’t need healers on a regular basis!"
    advmc "Don’t be stupid! Having a healer is a valuable asset. At the very least, I’d rather a healer than smelling your cigarette smoke!"
    blue "Hear, hear! Second-hand smoking is bad for you."
    green "W-what?! How come no one mentioned this to me before this? "
    advmc "I’m pretty sure I’ve said it a thousand times."
    green "But how else am I supposed to mark my Zone? You guys want me to vape? Is that it?"
    rookie "I... thought you looked pretty cool when you smoke."
    green "Damn straight, I am! See? This is how teammates should be!"
    advmc "Ugh, don’t encourage him!"
    rookie "Ah, my mistake. "
    blue "No, no. It’s not your fault. No matter how you look at it, it’s all Green’s fault."
    green "Come on! Don’t be like that! You guys all suck! Except for you, Rookie."
    rookie "I take back my smoking comment."
    green "All of you suck!"
    advmc "Pfft. Heheh. "
    green "Don’t laugh at me, Red! "
    advmc "But now that we’re all together again, it almost feels like we didn’t almost risk our lives for something dangerous!"
    blue "Oh right. We were in danger, weren’t we?"
    rookie "It escaped my notice as well."
    green "All of you guys are way too lax about this."
    advmc "Hehe. Then let’s get out of here. Since this was Rookie’s first mission, we should celebrate!"
    blue "I know a good sweets shop."
    green "If we’re celebrating, we should do something more exciting than eating. What about karaoke?"
    rookie "I am fine with anything. I just request that we do not engage in a high-risk activity like bungee jumping."
    advmc "... T-that was a joke?"
    rookie "Indeed."
    advmc "Hehe. You’re pretty funny."
    green "No, just what part of that \"joke\" was funny?"
    blue "Hey, don’t belittle people’s efforts. We don’t always shoot you down when you make no sense."
    green "What?! What’s with that? Hey! Don’t ignore me!"

    if onGreenRoute:
        #nvl set up
        nvl clear
        window show

        nvlmc "I bump shoulders with Green lightly before grinning. He gives me a dry look but can’t hold back a grin himself. With a dramatic sigh, he marches forth to take the lead position."
        nvlmc "Nuh-uh. I’m not letting him run."
        nvlmc "I jog up to stand by his side, grinning innocently all the while. He shoots me an annoyed look, but he doesn’t push me away. I’m tempted to trip him, just because."
        nvlmc "Probably because he knows me too well, he pats my back sharply with a knowing grin. Cheeky. Then again, I probably shouldn’t complain since I planned on tripping him first. I grin back at him, which makes him rethink. "
        nvlmc "Hah. Take that."
        nvlmc "Now he’ll be stuck on trying to figure out exactly what I did for the rest of our journey back. "

        nvl clear

        nvlmc "I snigger and pick up the speed. "
        nvlmc "Seeing that, Green yells and chases after me. Blue tries to scold us to slow down, but we’re too loud to make out his words. Rookie seems confused, but he picks up the pace, too. After a second, Blue runs after us, yelling at all of us to slow down."
        nvlmc "We’re nowhere close to finding out how to rescue Boss from his curse. But I feel like this mission wasn’t a total loss. "
        nvlmc "Next mission for sure, this team will succeed."

        #escape nvl mode
        nvl clear
        window hide

        #Green's End CG
        $quick_menu = False
        $ persistent.greenend = True
        $ persistent.greengoodend = True
        $ persistent.endingct =+1
        scene end greengood with fade
        pause 2.0
        return

        #Green's Ending

    else:
        #nvl set up
        nvl clear
        window show

        nvlmc "In the end, we found absolutely nothing that can help Boss’s curse in this place. But I guess expecting to find something like that would be akin to asking for a miracle. Especially from someone childish like that Witch."
        nvlmc "But it’s not a total loss."
        nvlmc "Rookie doesn’t look as reluctant around us anymore. And if we could have a healer on our side, we’ll be able to tackle on harder missions we’ve been turning down. Likewise, I’ll have to become stronger to make sure that no one is hurt again."
        nvlmc "This time for sure, I’ll protect the things most important to me. "
        nvlmc "Boss, just you wait. We’ll undo your curse."
        nvlmc "Until then, I’ll laugh and treasure this moment. I’m sure that’s what you’d want for me."

        #escape nvl mode
        nvl clear
        window hide

        #Bloodied Hands End CG
        $quick_menu = False
        $ persistent.normalend1 = True
        $ persistent.endingct =+1
        scene end one with fade
        pause 2.0
        return

        #Bloodied Hands Ending


label thirdspare:
    "Not yet implemented"

label thirdexor:
    "Not yet implemented"

label thirdtrue:
    "Not yet implemented"

return #We're done with 3rd chapter!
