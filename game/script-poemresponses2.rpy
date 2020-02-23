label poemresponse2_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse2_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_act2
        else:
            scene bg club_act2
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse2_start2:
        $ skip_poem = False
        $ pt = "2"
        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        menu:
            "[menutext]"

            "Satori." if not s_readpoem:
                $ s_readpoem = True
                call poemresponse2_sayori
            "Natsuko." if not n_readpoem:
                $ n_readpoem = True
                call poemresponse2_natsuki
            "Yuuri." if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                call poemresponse2_yuri
        $ poemsread += 1
        if poemsread < 3:
            jump poemresponse2_loop

    # Reset variables for next time
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label poemresponse2_natsuki:
    scene bg club_act2
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene
    return

label poemresponse2_yuri:
    scene bg club_act2
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene
    return

label poemresponse2_sayori:
    scene bg club_act2
    with wipeleft_scene
    $ nextscene = "ch" + pt + str(chapter) + "_s_start"
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene
    return



label ch21_s_start:
    show satori 7aac at t11
    s "So, [player]...having fun so far?"
    mc "Um, yeah. Absolutely." 
    s 1aac "Great."
    s "Anyway, do you want to share your poem with me?"
    mc "It's kinda embarrassing, but it's what I agreed to."
    s 1aai "..."
    s 7aah "You didn't have to stay, you know."
    mc "...?"
    s 1aag "You could've quit at any time."
    mc "That's not really what I meant..."
    s 7aao "I wasn't talking to you."
    $ style.say_window = style.window_monika
    mc "Oh..."
    s 1aai "..."
    $ style.say_window = style.window
    mc "..."
    s 1aal "..."
    s 4aaw "{b}Well, are you going to show me your poem or not!?{/b}"
    mc "...!"
    $ style.say_window = style.window_monika
    mc "Y-yes! Of course..."
    $ style.say_window = style.window
    "I quickly hand Satori my poem."
    $ style.say_window = style.window_monika
    s 1aai "Hm..."
    $ style.say_window = style.window
    mc "Do you like it?"
    s 1aag "...What language is this?"
    mc "...!"
    mc "What do you mean what language is it?"
    mc "It's the same as everyone else!"
    "Satori rolls his eyes and hands my poem back to me."
    s 7aao "I can't read this chicken scratch."
    s 1aah "Next time, make sure it's actually legible."
    s "Otherwise, I'll count it as a missed assignment."
    s 7aah "If you get two of them, you're out of the club."
    mc "...I'm sorry..."
    "I look away, embarrassed." 
    s 1aap "Well, whatever."
    s "Here's my poem."

    return

label ch21_s_end:
    call showpoem(poem_s21)

    show satori 1aac
    s "So...what do you think?"
    $ style.say_window = style.window_monika
    mc "Um...It's very... freeform, if that's what you call it."
    $ style.say_window = style.window
    mc "Sorry, I'm not really the best person to offer criticism."
    s 7aat "I wasn't looking for criticism."
    s "It's not like you could offer anything constructive anyway, seeing that you don't even know what you're doing."
    mc "...I guess that's true..."
    $ style.say_window = style.window_monika
    mc "So, what was the inspiration behind this poem?"
    s 1aac "Well..."
    $ style.say_window = style.window
    s 7aac "I guess you can say I had some kind of epiphany recently."
    s "It's been influencing my poems a bit."
    mc "An epiphany?"
    s 1aav "Yes, an epiphany."
    s 7aau "If you don't know what it means, go look at the dictionary on the shelf."
    $ style.say_window = style.window_monika
    mc "I know what an epiphany is."
    if y_ranaway:
        "Suddenly, the door swings open."
        $ style.say_window = style.window
        show satori 1aap at t22
        show yuuri 6a at t21
        mc "Hey, Yuuri!"
        s 1aas "Ah..."
        s 10aae "Feeling better, McStroke?"
        y 6ab "..."
        y 6ad "Don't be crass."
        y 1ae "I was simply getting a drink of water."
        s 1aaf "Sure you were."
        y 1ac "...I see you've already started sharing poems..."
        y 6ab "...Without me."
        s 4aac "Yes, we have."
        s 7aas "Perhaps if you spent more time in the club and less time repainting the bathroom stalls, you'd have been here on time."
        y 7ag "..."
        y 6ab "I'll go get my poem."
        "Yuuri's voice rumbles deeply as he slinks off to retrieve his poem."
        show yuuri at thide
        hide yuuri
        show satori at t11
        $ y_ranaway = False
    else:
        s 1aac "Good for you."
        $ style.say_window = style.window
        mc "Also, I'm sorry for screaming earlier."
        mc "I was startled."
        mc "I didn't mean to be so loud."
        s 1aad "That must've been one hairy, ugly spider you saw."
        s 7aat "They're everywhere up here, so try to get used to it for now."
        s 7aau "Another squeal like that might shatter these brittle windows."
        s 1aat "It's only slightly higher in pitch than Natsuko's girly scream."
        s 1aac "Thankfully, he's been conditioned to control it."
        s 3aan "That shrill squeal of his should be reserved for his home life, where it belongs, with all of his other feminine behaviors."
    s 1aag "Anyway..."
    s "We're done here."
    mc "Um..."
    s 1aah "What?"
    mc "To be honest, I didn't really learn anything from you..."
    mc "Do you maybe have any helpful writing tips for me?"
    show satori 1aan
    "Satori thinks for a moment."
    s 1aao "Writing tips, huh?"
    mc "That's right."
    mc "This way I can walk away with at least some useful knowledge after each of these sessions."
    s 7aak "You want a tip?"
    s "Okay, here's one."
    s 4aah "Next time you write a poem, don't suck at it."
    s 7aac "That's my advice for today!"
    s 4aao "Now, get out of my face."

    return



label ch21_y_good:
    show yuuri 1a at t11
    y 1e "..."
    "As he reads through my poem, I notice his eyes lighten." 
    y "Exceptional..."
    mc "Yeah?" 
    mc "You really think so?"
    y 1y "It's truly amazing, [player]"
    y 1b "What kind of experience do you have?" 
    y 1c "Your use of metaphors and imagery indicate you've done a lot of writing before."
    mc "That's a really huge compliment coming from you." 
    mc "This is actually my first time writing."
    show yuuri 1e
    "Yuuri looks at me quizzically before looking over my poem again."
    y 6g "Interesting..."
    "Yuuri traces the words of my poem with his finger, as if breaking it down more thoroughly."
    y 6h "The thing is..." 
    y 4f "There are specific writing habits that are usually typical of new writers." 
    y 4h "Having been through that myself, I've learned how to pick up on them." 
    y 3k "See, new writers try to make their style more deliberate, often picking a subject matter different from the style and then just form-fitting them together." 
    y 3h "The end result is that both the style and the expressiveness are weakened."
    "Once Yuuri finds his train of thought, his demeanor does a complete 180." 
    "His stammering disappears and he sounds more like a teacher than a student."
    y 1f "Now, this is not something the new writer can be blamed for, of course." 
    y 3f "There are many techniques that can go into writing even a simple poem." 
    y 3k "Not just finding them and building them, but getting them to work together is probably the most challenging part." 
    y 3m "All of this comes with practice, learning from example and trying new things." 
    y 3b "That's why I thought you were experienced." 
    y 3d "Because I see none of these mistakes in your poem."
    mc "It's probably just beginner's luck." 
    mc "Please don't be disappointed if tomorrow's doesn't come out as good."
    y 1a "It's okay." 
    y 1b "You're new, so I expect you to try to new things." 
    y 4m "Receiving valuable feedback from everyone else will influence you as well." 
    y 6h "Natsuko can be a bit biased, though..."
    mc "Biased? How?"
    y 6h "Ah...well..."
    y 6i "I suppose you'll see what I mean eventually."
    mc "Alright..."
    mc "So, how about I check out your poem now?"
    y 1c "Yes, of course!" 
    y 1d "I would love to share my thought process behind it."
    "Yuuri smiles dreamily as he hands me his poem." 

    return

label ch21_y_end:
    call showpoem(poem_y1)

    show yuuri 1a
    y "What are your thoughts?"
    mc "I really liked it."
    mc "I like the imagery and the atmosphere of it all."
    mc "I like how it made me feel while I was reading it."
    mc "I like how it was short, yet descriptive."
    y 1f "It wasn't too short, was it?"
    y 4q "I mean...I do prefer shorter poems..."
    y 1s "But I can write a longer one next time if you'd prefer."
    mc "I like your style just the way it is."
    y 1c "I really appreciate that."
    y 1b "Since it's our first time sharing, I wanted to write something a little more mild."
    y 1d "Something easy to digest, I suppose." 
    y 4b "I like when my readers derive their own meaning out of my writing."
    mc "You sure know a lot about this."
    y 1c "It's nothing, really."
    y 1a "Remember, it won't be long before you pick up on these things too."
    mc "Well, I could definitely learn a thing or two from you."
    y 1d "I hope so." 

    return



label ch21_n_bad:
    show natsuko 1g at t11
    n "...Hmm..."
    mc "...?"
    n 7w "Well, it doesn't blow me away."
    mc "Ah...sorry, I'm not very good."
    n 5k "Hey, it's cool." 
    n "You're not a writer." 
    n "I get it." 
    n 3l "Cheer up, I'm sure you'll improve eventually." 
    n 1k "I'd point out what you need to work on, but you're better off just trying again from scratch."
    mc "Fair enough." 
    mc "To each their own, I guess."
    n 5y "Here, check out my poem."
    n 7z "You'll be able to see what I mean."

    return

label ch21_n_end:
    call showpoem(poem_n1)

    n 7y "Impressive, right?"
    mc "Yeah, it's good."
    n 5z "Yeah, I knew you'd love it."
    n 7k "Most everyone in high school thinks writing has to be all sophisticated and stuff."
    n 7m "So, people usually don't take my writing seriously."
    n 3d "But you seem like the type who understands how effective simple writing can be."
    mc "Well, the point of writing is for people to express themselves."
    mc "A person's writing style wouldn't make their message any less valid."
    n 5l "Yes, exactly!"
    n "I knew you'd understand!"
    n 3l "I like when something is easy to read..."
    n "But it hits you hard. Like in this poem."
    n 3m "Seeing everyone around you do great things can be really disheartening."
    n 1k "So I decided to write about it."
    n 3l "The other nice thing about simple writing is that it puts more weight on the wordplay."
    n 5z "And, to me, nothing brings out feeling like poems that rhyme!"
    mc "Wow, more went into this than I realized."
    n 7y "That's what it means to be a pro!"
    n 7d "I'm glad I was able to teach you something!"
    n 5d "I bet you didn't expect that from me, did you?"
    mc "I guess not. Thank you for the lesson."
    "I decide to humor him with that last comment."
    "I'm not sure what he meant by that."
    "But if Natsuko is feeling proud, then I won't take that away from him."

    return