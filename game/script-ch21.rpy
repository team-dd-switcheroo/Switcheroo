
init python:
    def auto_hist(w):
        while w != w:
            _history_list.pop()

label ch21_main:
    stop music fadeout 2.0
    scene bg club_act2
    with dissolve_scene_half 
    play music t3
    show satori 1aac at t11
    s "Huh. You came back..."
    $ style.say_window = style.window_monika
    mc "Yep."   
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "I told you I'm serious about this."
    mc "It might be a little strange for me, but at least I keep my word."
    show satori at thide
    hide satori
    "Well, I'm back at the Literature Club. I'm the last one to come in so everyone else is already hanging out."
    show yuuri 1ap at t11
    y "Thank you for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."  
    y 1u "Making you dive head first into literature when you're not accustomed to it..."
    show yuuri at t22
    show natsuko 7b at t21
    n "Jeez, Yuuri. It's literature, not open-heart surgery." 
    n 5c "The world isn't gonna end just because she doesn't take it seriously." 
    y 4r "Of course it doesn't hold the importance of heart surgery, but literature IS important nonetheless, Natsuko."
    y 6ac "You'd think the Vice President of the Literature Club would understand that..."
    show yuuri at thide
    hide yuuri
    "Annoyed, Yuuri sinks into his seat."
    show natsuko at t11
    n 5l "Don't worry, [player]."
    n "We'll make sure to put your comfort first, okay?"
    show natsuko 7g
    "Natsuko shoots Yuuri with an irate glare."
    show natsuko ghost_glitch
    $ pause(0.2)
    mc "Thanks, Natsu."
    n 5t "Um, anyway...now that you're in the club and all, it would be a good time for you to find something to read."
    mc "Well, I can't really say no either way."
    mc "Like you said, I'm in the club now."
    mc "So it only makes sense that I find a book to read, since that's one of the main club activities."
    n 5z "Glad to hear!"
    n 3ah "And as Vice President of the club, I should help you get started!"
    show yuuri 4b at t21
    show natsuko 5h at t22
    y "Actually, Natsuko, about that..."
    "Yuuri reaches into his bag and pulls out a book."
    y "I didn't want [player] to feel left out..."
    y 4d "So I picked up a book I thought she might enjoy."
    show natsuko at thide
    hide natsuko
    show yuuri at t11
    "Yuuri turns to me."
    y 1b "It's a short read, so it should keep your attention, even if you don't usually read."
    y 1j "I was hoping after you finished it..."
    y 1i "We could..."
    y 1u "You know..."
    $ style.say_window = style.window_monika
    y 1s "Discuss it..."
    $ style.say_window = style.window
    $ _history_list.pop()
    y 1ar "If you wanted."
    "He smiles amorously."
    "I sigh."
    "As if this guy wasn't cute enough already."
    "I can't believe he brought me a book he thought I'd enjoy despite me not reading much."
    "What a gentleman."
    "I suppose reading it is the least I could do."
    mc "Wow, Yuuri, thank you so much!"
    mc "I'll definitely read this!" 
    "I enthusiastically take the book and slip it into my bag."
    y 3d "Well, you can read it at your own pace."
    y 3ap "I look forward to hearing what you think." 
    show yuuri at thide
    hide yuuri
    "Now that everyone is settled in, I expect Satori to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Satori appears to be sitting idly at the back of the room."
    "Yuuri's face is already buried in a book."
    "I can't help but notice his intense expression, like he was waiting for this chance."
    "Meanwhile, Natsuko is rummaging around in the closet."

    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    return

label ch21_end:

    stop music fadeout 2
    scene bg club_act2
    with wipeleft_scene
    play music t3

    "Phew."
    "I guess that's everyone."
    "I glance around the room."
    "That wasn't as stressful as I anticipated."
    "I learned what I already knew; my writing abilities are mediocre at best."
    "There's no way my poems can stand up to theirs."
    "But I still enjoyed getting to know everyone and learning about their own techniques."
    "I notice across the room, Satori is writing something in his notebook."
    show natsuko 1c at t21
    show yuuri 1g at t22
    "My eyes then land on Yuuri and Natsuko."
    "They exchange sheets of paper, sharing their respective poems."
    "As they read in tandem, I notice each of their expressions change."
    "Natsuko's eyebrows furrow in frustration."
    "Meanwhile, Yuuri smiles sadly."
    n 1q "What's with this language?" 
    y 1e "Hmm? Did you say something?" 
    n 7w "Oh, it's nothing." 
    "Natsuko dismissively returns the poem to the desk with one hand."
    n 5w "I guess you can say it's...fancy." 
    y 1j "Ah, thanks. Yours is...cute." 
    n 6f "Cute?!"
    n 5e "Did you completely miss the symbolism or something?!"
    n 5x "It's clearly about the feeling of giving up!"
    n 7e "How can that be cute?!"
    y 1h "Is... that what that was?"
    y 1g "Hmm... I guess I can see that now."
    y "But... the language..."
    n 7b "Yeah? What about it?" 
    y "Well... If I may offer a couple suggestions..."  
    n 7f "Hmph!"
    n 5w "If I was looking for suggestions, I would have asked someone who actually likes it!"
    n 7w "Which people DID by the way!"
    n 3w "[player] liked it."
    n 5e "So based on that, I'll gladly give you some suggestions of my own."
    n 3x "First of all..." 
    y 1k "Excuse me."
    y 3k "I appreciate the offer, but I've spent a long time developing my writing style."
    y "I don't expect it to change anytime soon, unless of course I come across something  particularly inspiring."
    y 1h "Which I haven't yet."
    y 1l "And [player] liked my poem too, by the way."
    y "She even said she was impressed by it." 
    stop music fadeout 2
    "Natsuko smirks and leans back in his chair, propping his feet up on the desk."
    n 1y "Oh? I didn't realize you were so invested in impressing our new member, Yuuri!"
    play music t7
    #play music t7a
    y 7n "---!" 
    y "I-I..." 
    y "You're just..."
    "Yuuri suddenly stands up."
    y 6r "Perhaps you're just jealous that [player] appreciated the advice of a mature individual more than she appreciated the views of a child." 
    n 6e "I'm the child??"
    n "Are you that full of yourself?"
    n 5b "Besides, how do you know she didn't appreciate {i}my{/i} advice more?!"
    y 6r "Full of myself, am I?"
    y 4r "You're the one who goes out of his way to make everything you do overly masculine..."
    y 6h "As though you're compensating for something..."
    n 6f "--!" 
    "Natsuko suddenly stands up."
    n 6p "And just what the hell is that supposed to mean?!" 
    y 6r "You know what it means." 
    n 6o "Well, you know what?"
    n "I'm not the one who started stuffing his pants with socks as soon as [player] started showing up!" 
    y 7p "N-Natsuko!"
    show satori 4aaj at t41
    s "Guys, shut up!"
    show yuuri 6as
    ny "MIND YOUR FUCKING BUSINESS!"
    show satori at thide
    hide satori
    #queue music t7
    $ timeleft = 19.559 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y 6r "Taking out your own insecurities on others like that...you really do act as young as you look, Natsuko!"
    n 6p "Me? Look who's talking, you pretentious dick-bag!"
    y "Pretentious?"
    y 4ad "Sorry that my maturity and intelligence are too much for someone of your mental age to comprehend!" 
    n 7y "Thank you for proving my point!"
    n 7b "You know, most people learn to get over themselves by the time they graduate middle school."
    n 5o "But your precious private tutors didn't bother to teach you that, did they?"
    y 6ae "If you want to prove anything, then stop harassing others with your sickening attitude!"
    y 6r "You think you can counterbalance your immaturity by acting like a tough guy?"
    y 6ac "That doesn't make you tough."
    y 6ab "It just makes you pathetic."
    n 7az "Whoa! Sick burn, Yuuri!"
    n "You probably should have saved it for that collection etched into your arms!"
    y 7p "D-did you just accuse me of burning myself?"
    y 6as "What the fuck is wrong with your head?!"
    n 6o "Yeah, go on!"
    n "Show [player] what really gets you hot under the collar!"
    n 5b "I'm sure she'll be head over heels for you after this!"
    show yuuri 7n
    "Suddenly, Yuuri turns towards me as if he just noticed I was sitting there."
    y 7p "[player]!"
    y "He-he's lying!"
    y 7o "He just wants to make me look bad!" 
    n 7b "That's not true! He started it!"
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}WHAT THE HELL IS HAPPENING?{/cps}{nw}"
    "{cps=*2}WHY DOES IT FEEL LIKE I'VE DONE THIS BEFORE?!{/cps}{nw}"
    "{cps=*2}WHY DON'T I HAVE ANY CONTROL OVER WHAT I SAY OR DO?!{/cps}{nw}"
    "{cps=*2}HOW COME SATORI DOESN'T REMEMBER ME?!{/cps}{nw}"
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Natsuko.":
                jump menu_click
            "Yuuri.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.2
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.2
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.2
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.2
    show satori 1aac onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.2
    $ renpy.display_menu(items=[('Natsuko.', True), ('Yuuri.', True)], interact=False, screen='choice')
    s "..."
    show layer master
    show layer screens
    show satori 1aac onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Natsuko.', True), ('Yuuri.', True)], interact=False, screen='choice')
    s "..."
    $ renpy.display_menu(items=[('Natsuko.', True), ('Yuuri.', True)], interact=False, screen='choice')
    s "..."
    show satori 1aak onlayer front at i11
    $ renpy.display_menu(items=[('Natsuko.', True), ('Yuuri.', True)], interact=False, screen='choice')
    s "Hey, [player]..."
    show satori 1aaa onlayer front at i11
    $ renpy.display_menu(items=[('Natsuko.', True), ('Yuuri.', True)], interact=False, screen='choice')
    s "I'm gonna go\nget a drink from\nthe vending machine..."
    show satori 7aae onlayer front at i11
    $ renpy.display_menu(items=[('Natsuko.', True), ('Yuuri.', True)], interact=False, screen='choice')
    s "You've got this,\nright?"
    show satori onlayer front at thide
    hide satori onlayer front
    "{cps=*2}HOW COME SATORI DOESN'T REMEMBER ME?!{/cps}{nw}"
    "{cps=*2}WHY DON'T I HAVE ANY CONTROL OVER WHAT I SAY OR DO?!{/cps}{nw}"
    "{cps=*2}WHY DOES IT FEEL LIKE I'VE DONE THIS BEFORE?!{/cps}{nw}"
    "{cps=*2}WHAT THE HELL IS HAPPENING?{/cps}{nw}"
    mc "{cps=*2}...{/cps}{nw}"
    n 7b "{cps=*2}That's not true! He started it!{/cps}{nw}"
    y 7o "{cps=*2}He just wants to make me look bad!{/cps}{nw}" 
    y "{cps=*2}He-he's lying!{/cps}{nw}"
    y 7p "{cps=*2}[player]!{/cps}{nw}"
    #resume_fight
    $ quick_menu = True
    hide noise
    hide vignette
    hide flicker
    hide screen choice
    #play music t7b
    play music t7
    show yuuri 6n
    show natsuko 6o
    $ style.say_dialogue = style.normal
    $ auto_hist(13)
    "Suddenly, Yuuri turns towards me as if he just noticed I was sitting there."
    y 7p "[player]!"
    y "He-he's lying!"
    y 7o "He just wants to make me look bad!" 
    n 7b "That's not true! He started it!"
    mc "C'mon, guys!"
    mc "Why drag me into this?"
    mc "I don't even know anything about writing!"
    y 6ad "This has nothing to do with writing."
    y 4ae "It has to do with Natsuko being an insecure little twerp who throws a fit when someone doesn't agree with him!"
    n 6o "You better watch how you talk to me, you fucking snob!"
    n 4f "Don't think for a second that I'm scared of you!"
    n 5x "I'll climb up there right now and smack the shit outta you!"
    y 6ab "I'd like to see you try it..."
    show natsuko 6r
    "Natsuko's face is blazing red."
    "He clenches his fists..."
    n 6o "[player]..."
    n "I think you should leave now."
    mc "Um...I-I really..."
    n 6p "PLEASE LEAVE NOW!"
    "Natsuko is furious."
    "I'm nervous about leaving them alone."
    $ style.say_window = style.window_monika
    "Natsuko is so much smaller than Yuuri..."
    $ style.say_window = style.window
    $ _history_list.pop()
    "Hm..."
    "Maybe it's best for me to not witness that fight."
    $ style.say_window = style.window_monika
    "I decide to leave and wait outside, hoping for the best."
    $ style.say_window = style.window
    $ _history_list.pop()

    stop music fadeout 2
    scene bg act2_corridor
    with wipeleft_scene

    show satori 7aau at t11
    s "So...are they still fighting?"
    "Satori casually takes a sip of apple juice."
    $ style.say_window = style.window_monika
    "I'm a little shocked by how calmly he's reacting to this."
    mc "Satori, don't you think you should stop them?"
    s "Why would I do that?"
    mc "Well...because...it's your job as President to diffuse any conflicts between club members."
    $ style.say_window = style.window
    $ _history_list.pop()
    s 10aav "{i}Yawn.{/i}"
    s 1aao "Oh, please."
    s "I'm not gonna waste my time worrying about that crap until we get an actual room downstairs."
    s 7aaa "Which, by the way, we're on the list for."
    s 4aac "Told the student council President this morning that we now have 4 members."
    s "So we'll have a room no later than Monday."
    s 7aae "That's when everything becomes official, so that's when I'll start breaking up fights."
    s 7aao "But while we're still stuck in this dump...they can kill each other for all I care."
    show yuuri 6ac at l31
    show satori 1aan
    "Suddenly, Yuuri rushes out of the clubroom."
    "He keeps his head down as he hurries past us and towards the exit without a single word."
    show yuuri at thide
    hide yuuri
    s 9aaf "Well, I guess they're done."
    s 1aac "Time to assess the damage."


    scene bg club_act2
    with wipeleft_scene


    "I enter the room to see Natsuko sitting at a desk with his arms crossed, staring out the window."
    "As I approach, I notice he isn't scowling..."
    "In fact, he wears a guilty expression on his face."
    mc "N-Natsu??"
    show natsuko 7u at t11
    n "I-I didn't mean it, you know."
    n 7av "He just...he made me so mad...and then I said it without thinking..."
    n 5m "But I swear, I would never actually do it..."
    mc "I believe you."
    "I have no idea what Natsuko might have said to Yuuri."
    $ style.say_window = style.window_monika
    "Or threatened to do to him."
    n 5n "I'm sorry I yelled at you, too, [player]."
    $ style.say_window = style.window
    $ _history_list.pop()
    n "I shouldn't have done that..."
    n 5s "I don't know what's wrong with me today..."
    n 7u "Maybe it's...this room."
    mc "This room?"
    $ style.say_window = style.window_monika
    n 7m "It feels so...angry in here..."
    $ style.say_window = style.window
    $ _history_list.pop()
    "I shiver a little."
    $ style.say_window = style.window_monika
    "I try to focus on the club and its members..."
    $ style.say_window = style.window
    $ _history_list.pop()
    "But there's a creepiness about this place."
    "Natsuko mentioned something about rumors yesterday that I haven't been able to get out of my head."
    $ style.say_window = style.window_monika
    "Part of me is curious to hear these rumors."
    "Another part of me, however..."
    $ style.say_window = style.window
    $ _history_list.pop()
    show satori 7aao at t31
    s "Don't blame the room for your freak-out."
    show natsuko 7s
    "Natsuko shoots Satori an annoyed glare."
    n 7x "Just forget it."
    n "You wouldn't understand."
    s 7aav "It's not that I don't understand, Natsuko."
    s 1aac "It's just that I don't care."
    "Satori looks at me."
    s 3aas "Besides, I'm sure you'll forget about this by tomorrow."
    s 1aac "Completely."
    n 7q "Yeah, I won't remember a thing."
    "Natsuko says this sarcastically, rolling his eyes."
    s 1aag "I wasn't talking to you..."
    $ style.say_window = style.window_monika
    s 7aav "Anyway, the club meeting is over."
    $ style.say_window = style.window
    $ _history_list.pop()
    s 1aai "Both of you, scram."
    s "I've been wanting to be left alone all day."
    "Natsuko briefly looks at me like he wants to say something, but quickly changes his mind."
    show natsuko at thide
    hide natsuko
    show satori at thide
    hide satori
    "He stoically grabs his stuff and heads for the door."
    "I start to follow."
    $ style.say_window = style.window_monika
    "STOP.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "..."
    $ style.say_window = style.window_monika
    "I SAID STOP!!!{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    "I stop at the threshold for some reason."
    $ style.say_window = style.window_monika
    "WE HAVE TO TRY TO TALK TO HIM.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    "..."
    "..."
    $ style.say_window = style.window_monika
    "JUST DO IT.{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    "I turn to look at Satori."
    $ style.say_window = style.window
    $ _history_list.pop()
    "I'm not sure why, but I feel compelled to talk to him."
    "We probably should address his responsibilities as club President."
    mc "Satori..."
    show satori 1aag at t11
    s "Hm? Why are you still here?"
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "..."
    mc "...About the fight..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "I hate to say this...but you really should..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "...Remember me."
    s 1aam "...?"
    s 3aah "What?"
    mc "I just...I think the club would really benefit if you would just..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "...Remember me."
    s 1aai "What on earth are you talking about?"
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "I mean...regardless of what room we're in, it's still your job to..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "...Remember me."
    mc "You have to..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "...Remember me."
    s 7aam "[player]...what's wrong with you???"
    mc "I don't mean to overstep my bounds, here..."
    mc "I just want you to..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "...Remember me."
    "He looks distressed all of a sudden..."
    s 1aax "Y-you're crazy..."
    "Flustered, I reach out and grab his hands."
    mc "It's not as difficult as you're making it out to be!"
    mc "Please, Satori..."
    mc "Just..."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME."
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "...Remember me!"
    s 1aay "..."
    mc "Do you hear me, Satori?"
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME."
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "Satori, remember me."
    $ style.say_window = style.window_monika
    "SATORI. REMEMBER ME.{nw}"
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "Satori, remember me."
    mc "Satori, remember me."
    mc "Satori, remember me."
    mc "Satori, remember me."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show satori 1aaz at t11
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "SATORI, REMEMBER ME!!!!!"
    $ gtext = glitchtext(100)
    mc "[gtext]"
    $ style.say_window = style.window_monika
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ style.say_window = style.window
    $ _history_list.pop()
    mc "From Hanaka: In this section IDK which is caged_wolf or jjj so I made a rough guess to the example code you asked for."
    mc "Let me know if it's not right. Check the game folder for this or report exceptions as always."

    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        python:
            try: renpy.file(config.basedir + "/game/caged_wolf.png")
            except: open(config.basedir + "/game/mod_assets/images/poem_special/poem_special8_both.png", "wb").write(renpy.file("caged_wolf.png").read())
        scene black with Dissolve(1.0)
    else:
        python:
            try: renpy.file(config.basedir + "/game/jjjjjjjjjjjjjjjjjjjjjjjjjjjjj.png")
            except: open(config.basedir + "/game/mod_assets/images/poem_special/special_poem7_both.png", "wb").write(renpy.file("jjjjjjjjjjjjjjjjjjjjjjjjjjjjj.png").read())
        scene black with Dissolve(1.0)
    
    return
