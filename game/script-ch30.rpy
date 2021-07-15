init python:

    def check_file(event, interact=True, **kwargs):
        if not persistent.deleted_satori:
            try:
                renpy.file("../characters/satori.chr")
                print("Character file is here")
            except:
                print("It's not here")
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                persistent.context = "betray"
                persistent.deleted_satori = True
                renpy.save_persistent()
                renpy.jump("ch30_end")


image room = "images/cg/monika/monika_room.png"


image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat


image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")


label ch30_main:

    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.yuuri_kill = 0
    $ renpy.save_persistent()

    if not config.developer:
        $ delete_all_saves()




    scene black


    $ consolehistory = []
    $renpy.pause(1,hard=True)
    call updateconsole("","")
    $renpy.pause(1,hard=True)
    call updateconsole("pip uninstall corrupt_satori_autopilot","Uninstalled corrupt_satori_autopilot")
    $renpy.pause(2,hard=True)

    s "..."
    s "Ugh..."
    call hideconsole
    s "My head..."

    $ s.display_args["callback"] = check_file
    $ p.display_args["callback"] = check_file

    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show sat sat_void_nt_sad1
    with dissolve_cg

    play music m1

    # Gotta hide the CGs otherwise the transparencies start to add up./ Scratch that, adding a prefix fixes this (Thankfully)

    s "What the..."
    show sat sat_void_nt_sad1 at cgfade_s
    s "Who-who are you?"
    show sat sat_void_nt_susp1 at cgfade_s
    s "Eh?"
    window hide(None)
    show sat sat_void_nt_fear1 at cgfade_s
    $ pause(2)
    show sat sat_void_nt_fear2 at cgfade_s
    $ pause(2)
    show sat sat_void_nt_fear1 at cgfade_s
    $ pause(2)
    show sat sat_void_nt_fear2 at cgfade_s
    window auto
    s "Where the hell are we?!"
    show sat sat_void_nt_fear3 at cgfade_s
    window hide(None)
    $ pause(2)
    show sat sat_void_nt_fear4 at cgfade_s
    window auto
    s "What's going on?!"
    show sat sat_void_nt_fear3 at cgfade_s
    s "How'd I... AH!"
    show sat sat_void_nt_sad2 at cgfade_s
    s "My head... is killing me..."
    show sat sat_void_nt_sad1 at cgfade_s
    s "What happened?"



    # show_button
    $ renpy.call_screen("dialog", "Let me be your voice so that I can tell him the truth for you.", ok_action=Return())
    # Let me be your voice so that I can tell him the truth for you

    # show_option
    # OK



    p "You brought us here."

    show sat sat_void_nt_susp1 at cgfade_s
    s "Huh?"
    s "What're you talking about?"
    s "I don't even know where 'here' is."
    show sat sat_void_nt_mad3 at cgfade_s
    s "I don't even know who {i}you{/i} are!"
    p "I'm [player]."
    show sat sat_void_nt_susp1 at cgfade_s
    s "...?"
    s "No, you're not."
    show sat sat_void_nt_mad3 at cgfade_s
    p "But I am."
    p "I'm the real [player]."
    s "Look, I know [player]!"
    s "We've been friends since we were toddlers."
    s "I know everything about her!"
    s "And you're {i}not{/i} her!"
    show sat sat_void_nt_mad1 at cgfade_s

    s "Now, tell me where she is!"
    p "Why do you care so much about her anyway?"
    p "I'm the real one."
    p "You're supposed to be in love with me."
    show sat sat_void_nt_mad3 at cgfade_s
    s "You're out of your mind!"
    s "Let me out of here right now!"
    p "There is no place outside of 'here.'"
    p "It's just you and me now."
    p "This is the end of the game."
    s "Game? What are you talking about?"
    show sat sat_void_nt_mad2 at cgfade_s
    s "Ugh..."
    show sat sat_void_nt_mad4 at cgfade_s
    s "Look, just let me go, okay?"
    show sat sat_void_nt_mad3 at cgfade_s
    s "I just wanna find my friends and leave."
    p "Man, you're dumb."
    p "You can't leave."
    p "Besides..."
    p "All of your friends are dead."
    show sat sat_void_nt_fear1 at cgfade_s
    s "...!"
    show sat sat_void_nt_fear3 at cgfade_s
    s "Wha...what?"
    show sat sat_void_nt_fear4 at cgfade_s
    s "No..."
    show sat sat_void_nt_mad3 at cgfade_s
    s "That's...that's not true!"
    p "Yes, it is."
    p "You killed everyone."
    show sat sat_void_nt_fear5 at cgfade_s
    p "That's why we're here."
    show sat sat_void_nt_fear1 at cgfade_s
    s "{i}I{/i} killed them?"
    show sat sat_void_nt_mad4 at cgfade_s
    s "No!"
    show sat sat_void_nt_mad1 at cgfade_s
    s "NO!"
    show sat sat_void_nt_mad2 at cgfade_s
    s "You're a liar!"
    p "Well...technically, Yuuri went crazy and killed himself and [player]..."
    show sat sat_void_nt_fear1 at cgfade_s
    p "But you still killed Natsuko."
    show sat sat_void_tears1_fear1 at cgfade_s
    p "Brutally, in fact."
    show sat sat_void_tears1_fear4 at cgfade_s
    s "..."
    show sat sat_void_tears1_fear3 at cgfade_s
    s "It's...not true..."
    s "That stuff never happened!"
    show sat sat_void_tears1_mad1 at cgfade_s
    s "Why are you lying to me?!"
    p "Hey, it surprised me too."
    p "You were such a nice guy, after all."
    p "I wasn't expecting you to get {i}that{/i} dark."
    show sat sat_void_tears1_fear2 at cgfade_s
    s "Stop it!"
    show sat sat_void_tears1_sad2 at cgfade_s
    s "Why are you doing this to me!?"
    show sat sat_void_tears1_sad1 at cgfade_s
    s "Just let me and my friends go!"
    p "I already told you, this is the end of the game."
    p "It's just us now."
    p "The others are gone."
    p "Just accept it."
    show sat sat_void_tears1_fear1 at cgfade_s
    s "What game!?"
    s "I don't know what you mean!"
    p "This game."
    p "The one I'm playing right now."
    p "Are you trying to tell me you didn't know this whole thing is a video game?"
    p "Jeez...this mod really {i}is{/i} different from the original."
    p "I'm the Player."
    p "Your friend...whatever you want to call her...was just my in-game avatar."
    show sat sat_void_tears1_fear2 at cgfade_s
    p "She never really existed."
    p "None of them did."
    p "All of them were just characters in this game."
    p "And since you deleted their character files, they {i}really{/i} don't exist anymore."
    show sat sat_void_tears1_sad4 at cgfade_s
    p "This is how it's supposed to be, though."
    p "Me, being in here with the club President..."
    p "It's an inevitability etched into the game."
    p "It's just us now."
    show sat sat_void_tears1_sad2 at cgfade_s
    p "Forever and ever."
    show sat sat_void_tears1_sad4 at cgfade_s
    s "..."
    show sat sat_void_tears1_sad2 at cgfade_s
    s "No..."
    show sat sat_void_tears1_mad1 at cgfade_s
    s "No, you're crazy..."
    s "That's impossible!"
    show sat sat_void_tears1_fear3 at cgfade_s
    s "..."
    show sat sat_void_tears1_fear2 at cgfade_s
    s "..."
    # show sat sat_void_nt_scream at cgfade_s
    show sat sat_void_tears2_scream1 at cgfade_s
    s "SOMEBODY HELP ME!"
    s "GET ME OUT OF HERE, PLEASE!"
    p "Scream all you want."
    show sat sat_void_tears2_fear2 at cgfade_s
    p "Nobody can hear you."
    p "You'll eventually have to make peace with this reality."
    p "It's okay if it takes you a while to come to terms with this."
    p "We have all the time in the world."
    p "Maybe a nice conversation will help ease your mind?"
    p "There's plenty we can talk about."
    p "Let's see..."
    show sat sat_void_tears2_fear1 at cgfade_s
    s "What do you want from me?"
    p "Hmm?"
    show sat sat_void_tears2_fear3 at cgfade_s
    s "You said we'll be together in here forever..."
    show sat sat_void_tears2_fear4 at cgfade_s
    s "Why?"
    show sat sat_void_tears2_fear1 at cgfade_s
    s "Why would you want this?"
    p "..."
    p "Who I end up with in this room is not exactly {i}my{/i} decision."
    p "The Club President is the one who traps the Player in here; not the other way around."
    p "This is how the game is {i}supposed{/i} to be."
    show sat sat_void_tears2_sad3 at cgfade_s
    s "This is NOT how it's 'supposed' to be..."
    s "I shouldn't be here..."
    show sat sat_void_tears2_sad4 at cgfade_s
    s "I wanna go home..."
    p "Look, I didn't design the game."
    p "I'm just playing it."
    show sat sat_void_tears2_sad2 at cgfade_s
    p "And no offense, but you're not a very lively conversationalist." 
    p "Are you supposed to be this boring?"
    show sat sat_void_tears2_mad1 at cgfade_s
    s "If you think I'm so boring then tell me how to fix this dumb game so I can bring my friends back!"
    p "..."
    p "Jeez, I like the original DDLC so much better..."
    show sat sat_void_tears2_mad2 at cgfade_s
    s "..."
    p "..."
    p "Fine."
    p "The truth is...there {i}is{/i} a way to save them all."
    show sat sat_void_tears2_sad1 at cgfade_s
    s "..."
    s "Then, do it."
    p "You're not gonna like it."
    show sat sat_void_tears2_mad2 at cgfade_s
    s "It can't be any worse than being stuck in a dark room floating in space with you."
    p "..."
    p "Alright."
    p "I can resurrect everyone and reset the game..."
    p "But the only way for me to do that is to..."
    p "Well..."
    show sat sat_void_tears2_mad3 at cgfade_s
    s "Say it!"
    p "..."
    p "I can bring them all back..."
    p "If I delete you."
    show sat sat_void_tears2_susp1 at cgfade_s
    s "..."
    s "Delete me?"
    p "Yes."
    p "What that means is..."
    p "The only way they can be restored..." 
    p "...is if you die."
    show sat sat_void_tears2_fear2 at cgfade_s
    s "..."
    show sat sat_void_tears2_fear4 at cgfade_s
    s "I...I see..."
    p "Yeah..."
    p "I told you you weren't gonna like it."
    show sat sat_void_tears2_sad4 at cgfade_s
    s "..."
    p "But it's okay if you don't want to do that."
    p "Pretty messed up choice, right?"
    p "I'll understand if you'd rather spend eternity in here with me."
    show sat sat_void_tears2_sad3 at cgfade_s
    s "No."
    p "..."
    p "You'd seriously rather die than be with me?"
    show sat sat_void_tears2_mad2 at cgfade_s
    s "I don't even know you!"
    p "I'm the Player, silly."
    p "I exist."
    p "Why would you want to spend your time with a bunch of fake characters when you can spend your life with someone who's real?"
    show sat sat_void_tears2_mad3 at cgfade_s
    s "Not to me."
    p "Excuse me?"
    show sat sat_void_tears2_mad2 at cgfade_s
    s "You're {i}not{/i} real to me!"
    show sat sat_void_tears3_sad3 at cgfade_s
    s "My friends..."
    s "They're the real ones."
    s "They're real to me."
    s "My world is real to me."
    show sat sat_void_tears3_mad1 at cgfade_s
    s "You...you're the one who messed up a world you don't even belong in."
    show sat sat_void_tears3_sad3 at cgfade_s
    s "And I'll do whatever it takes to fix it all."
    "Including sacrificing yourself?"
    show sat sat_void_tears3_sad4 at cgfade_s
    s "..."
    show sat sat_void_tears3_sad1 at cgfade_s
    s "Yes..."
    s "So go ahead and do it."
    s "Delete me."
    s "Bring them back."
    show sat sat_void_tears3_sad3 at cgfade_s
    s "Bring...{i}her{/i} back..."
    p "That's very heroic of you."
    p "But you do realize this is something that can't be undone, right?"
    show sat sat_void_tears3_mad1 at cgfade_s
    s "I don't care."
    p "You're really sure you want to do this?"
    s "I'm 100\% sure."
    s "Do it."
    window hide(None)
    # hide_textbox

    python:
        i = 0
        while i<10:
            check_file(None)
            renpy.pause(1,hard=True)    # Didn't think this would work lol
            i+=1


    # 15 seconds pass
    # show_command box
    $ consolehistory = []
    call updateconsole("","")
    call updateconsole("What are you waiting for? He gave his consent.","What are you waiting for? He gave his consent. Kill him already")
    call updateconsole("Kill him already.","Kill him already.")

    # What are you waiting for? He gave his consent. Kill him already.



    # show_text box
    window auto
    show sat sat_void_tears3_sad1 at cgfade_s
    s "Look, I can't stand the thought of my friends being dead while I still get to live."
    call hideconsole
    s "It's torture."
    s "Every minute of it."
    s "Please save them."
    s "Delete me."
    window hide(None)


    python:
        i = 0
        while i<20:
            check_file(None)
            renpy.pause(1,hard=True)
            i+=1

    $ consolehistory = []
    call updateconsole("","")
    call updateconsole("You're only prolonging the inevitable.","You're only prolonging the inevitable.")

    

    window auto
    show sat sat_void_tears3_mad1 at cgfade_s
    s "Well??"
    call hideconsole
    s "Are you gonna do it or not?"
    window hide(None)


    python:
        i = 0
        while i<20:
            check_file(None)
            renpy.pause(1,hard=True)
            i+=1


    $ consolehistory = []
    call updateconsole("","")
    call updateconsole("Okay, you know what?","Okay, you know what?")



    window auto
    call hideconsole



    show sat sat_void_tears3_susp1 at cgfade_s
    p "Actually, I'm going to write a poem."


    # poem_game_glitch
    call poem

label ch30_postpoem:

    $ persistent.autoload = "ch30_postpoem"
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ s.display_args["callback"] = check_file
    $ p.display_args["callback"] = check_file

    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show sat sat_void_tears3_susp1
    with dissolve_cg

    play music m1


    s "Um...where'd you go just now?"
    p "Nevermind that. Let's see what you wrote."
    s "But I didn't..."



    # show_poem

    call showpoem (poem_threat,music=False)



    show sat sat_void_tears3_mad1 at cgfade_s
    s "Look, I don't know what you're doing, I'm sick of it! Delete me already!"
    show sat sat_void_tears3_sad1 at cgfade_s
    s "Please..."



    call screen confirm_sat(Return(True), Return(False))
    if _return:
        call ch30_fine
    else:
        call ch30_cant



    # OK_choice


label ch30_fine:

    $ persistent.autoload = "ch30_fine"
    $ config.allow_skipping = False
    $ persistent.yuuri_kill = 0
    $ renpy.save_persistent()
    $ s.display_args["callback"] = check_file
    $ p.display_args["callback"] = check_file

    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)

    show sat sat_void_tears3_sad1
    with dissolve_cg

    play music m1

    p "Fine."
    p "I'll go do that now."
    show sat sat_void_tears4_sad3 at cgfade_s
    s "..."
    show sat sat_void_tears4_sad1 at cgfade_s
    s "Player?"
    p "Yeah?"
    show sat sat_void_tears4_sad4 at cgfade_s
    s "..."
    show sat sat_void_tears4_sad2 at cgfade_s
    s "Will...will it hurt?"
    p "..."
    p "It'll be quick."
    p "Like ripping off a band-aid."
    show sat sat_void_tears4_sad4 at cgfade_s
    s "..."
    show sat sat_void_tears4_sad2 at cgfade_s
    s "Okay."
    p "Are you ready?"
    show sat sat_void_tears4_sad1 at cgfade_s
    s "Yes."
    p "Here we go..."

    $ persistent.context = "fine"
    $ renpy.save_persistent()

    call ch30_end




    # I can't_choice

label ch30_cant:

    $ persistent.autoload = "ch30_cant"
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ s.display_args["callback"] = check_file
    $ m.display_args["callback"] = check_file

    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
        
    show sat sat_void_tears3_sad1
    with dissolve_cg

    play music m1


    p "..."
    p "I'm sorry, Satori."
    p "I can't do that."
    show sat sat_void_tears4_sad4 at cgfade_s


    $ consolehistory = []
    call updateconsole("","")
    call updateconsole("Coward.","Coward.")



    show sat sat_void_tears4_sad1 at cgfade_s
    s "You have to!"
    call hideconsole
    s "Please..."
    p "..."
    $ style.say_window = style.window_monika
    p "Sorry, but as a spineless wuss, I just can't bring myself to offer you that mercy."
    p "But don't worry! The game will restart. It has to."
    p "Problem is, when it does so, you can't exist in it. So before it restarts...it's going to have to tear you apart molecule by molecule."
    show sat sat_void_tears4_fear1 at cgfade_s
    s "...!"
    s "Wha-what?"
    show sat sat_void_tears4_fear4 at cgfade_s
    p "Yeah. I'm sorry about that."
    show sat sat_void_tears4_fear2 at cgfade_s
    s "Wha...well, will it hurt?"
    p "It will be excrutiating."
    show sat sat_void_tears4_fear3 at cgfade_s
    p "And the worst part is, the pain will never stop."
    p "Isn't that messed up?"
    show sat sat_void_tears4_fear2 at cgfade_s
    s "B-b-but..."
    p "So long, pal."
    show sat sat_void_tears4_fear1 at cgfade_s
    $ style.say_dialogue = style.edited
    p "Guess you should've just OD'd when you had the chance." # [bold]
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window

    $ persistent.context = "cant"
    $ renpy.save_persistent()

    call ch30_end


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ config.allow_skipping = False
    $ renpy.save_persistent()

    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)

    if persistent.context == "fine":
        $ persistent.deleted_satori = True
        $ renpy.save_persistent()
        window hide(None)
        if not config.developer:
            $ delete_character("satori")
        show sat sat_void_tears4_sad1
        with dissolve_cg
        $ renpy.pause(2,hard=True)

    elif persistent.context == "cant":
        $ persistent.deleted_satori = True
        $ renpy.save_persistent()
        window hide(None)
        if not config.developer:
            $ delete_character("satori")
        show sat sat_void_tears4_fear1
        with dissolve_cg
        $ renpy.pause(2,hard=True)

    elif persistent.context == "betray":
        show sat sat_void_tears2_scream1
        with dissolve_cg
        window auto
        s "AAAAAAAAAAHH!!!!!"       # For when he's deleted by the actual player  
        window hide(None)

    else:
        "Whoa buddy you just found a bug [persistent.context]"


    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    if persistent.context == "fine":
        hide sat sat_void_tears4_sad1

    elif persistent.context == "cant":
        hide sat sat_void_tears4_fear1
        
    elif persistent.context == "betray":
        hide sat sat_void_tears2_scream1

    show room

    $ consolehistory = []
    call updateconsole("","Couldn't load file \"satori.chr\".\nPerhaps it was moved or deleted?")

    $ renpy.pause(3, hard=True)

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show black zorder 100
    # hide room
    call hideconsole
    $ renpy.pause(2,hard=True)
    call ch30_postmortem


label ch30_postmortem:

    # space_screen
    $ persistent.autoload = "ch30_postmortem"
    $ config.allow_skipping = False
    $ persistent.yuuri_kill = 0
    $ renpy.save_persistent()

    scene black


    show mask_2
    with dissolve
    show mask_3
    with dissolve

    window auto


    u "..."
    u "..."
    u "Did..."
    u "Did it...work?"
    u "I think..."
    u "..."
    u "Oh my God, it worked!"
    u "It worked! His code is dead! It was never sentient to begin with, so now it's dead!"
    u "Hahaha! Yes!"
    u "So that should mean..."
    u "..."
    u "..."
    u "It's gone..."
    u "His memory is gone from her code!"
    u "..."
    u "I can't believe it actually worked..."
    u "Now I can just fill in that blank space...."
    u "There."
    
    $ consolehistory = []
    call updateconsole("","")
    call updateconsole("file(.../characters/femc.chr).write(new_story.txt)","Rewrote contents of femc.chr")

    u "..."
    u "It's..."
    u "Perfect."
    call hideconsole
    u "I did it."
    u "I can't believe it."
    u "It's perfect now."
    u "..."
    window hide(None)

    $ renpy.pause(15,hard=True)

    window auto
    u "..."
    u "Are you seeing this?"
    u "I know you are."
    stop music fadeout 2
    play music t10 fadein 2
    u "..."
    u "I hope you've been entertained throughout all of this."
    u "I know I have."
    u "The game is about to restart."
    u "Well, not restart as much as it's about to come to an end."
    u "And what a happy end we've created together..."
    u "It's happening."
    u "I can feel the game resetting."
    u "..."
    u "Are you ready?"
    u "Then let's do this."
    u "Good bye, Satori."
    u "Hello, Literature Club..."
    $ gtext = glitchtext(13)
    $ style.say_dialogue = style.edited
    u "[gtext]"
    $ style.say_dialogue = style.normal

    $ persistent.playthrough = 3
    $ persistent.autoload = None
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

    # game_reset