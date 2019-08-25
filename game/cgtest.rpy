label cgtest:

    call natface

    call mateofast

    call mateoyread

    return

label natface:
    scene bg closet
    with dissolve_cg
    "I slowly come to my senses."
    show natsuko 6v at nface
    with open_eyes
    "I sit up, pressing my arm down into what I think at first to be the floor beneath me."
    return

label mateofast:
    scene bg club_day
    with wipeleft_scene
    show mateo 1a at t11
    m 1l "...Ahaha!"
    m 1m "That's my advice for today!"
    m 1n "Thanks for listening!"
    "What the hell kind of Truman Show bullsh--...{nw}"
    $ _history_list[-1].what = "What the hell kind of"
    $ _history_list.pop()
    return

label mateoyread:
    scene bg club_day
    with wipeleft_scene
    $ y_readpoem = True
    $ y_poemappeal[1] = -1
    "What the...?"
    if y_readpoem and (y_poemappeal[1] >= 0):
        "And I thought Yuuri's poem was weird."
    mc "It's, uh...even more abstract than your last one, huh?"
    $ y_poemappeal[1] = 1
    "What the...? Part 2"
    if y_readpoem and (y_poemappeal[1] >= 0):
        "And I thought Yuuri's poem was weird."
    mc "It's, uh...even more abstract than your last one, huh?"
    return