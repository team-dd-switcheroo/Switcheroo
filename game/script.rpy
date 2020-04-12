


label start:

    $ anticheat = persistent.anticheat
    $ chapter = 0
    $ _dismiss_pause = config.developer

    $ s_name = "Satori"
    $ m_name = "Mateo"
    $ n_name = "Natsuko"
    $ y_name = "Yuuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal

    # Controls whether Sayori is Dead. Leave this alone
    $ in_sayori_kill = None
    
    # Controls whether we allow skipping.
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:
        call cgtest

        # $ chapter = 0
        # call ch0_main
        # call poem

        # $ chapter = 1
        # call ch1_main
        # call poemresponse_start
        # call ch1_end

        # call poem

        # $ chapter = 2
        # call ch2_main
        # call poemresponse_start
        # call ch2_end

        # call poem

        # $ chapter = 3
        # call ch3_main
        # call poemresponse_start
        # call ch3_end

        # $ chapter = 4
        # call ch4_main

        # python:
        #     try: renpy.file(config.basedir + "/hxppy thxughts.png")
        #     except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        # $ chapter = 5
        # call ch5_policy

        call endgame
        
        return

    if persistent.playthrough == 1:

        #call cgtest

        $ chapter = 0
        call ch20_main
        call poem

        $ chapter = 1
        call ch21_main
        call poemresponse2_start
        call ch21_end

        call endgame

        return
    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

label ch5_policy:
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch5_main_special
    else:
        call ch5_main
    return
    