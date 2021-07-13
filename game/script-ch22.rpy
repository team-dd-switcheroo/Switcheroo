label ch22_main:
    stop music fadeout 2.0
    scene bg club_act2
    with wipeleft_scene
    play music t6_2

    $ consolehistory = []
    call updateconsole("", "")
    call updateconsole("pip upgrade autopilot", "Successfully installed autopilot-3.0")

    call hideconsole

    $renpy.pause(1,hard=True)


    show yuuri 1aw at t11
    y "Hi, [player]!"
    "Yuuri seems energenic today dispite appearing a bit disheveled."
    y 1aaw "I've been waiting for you."
    y 3aah "Are you ready to continue reading?"
    y 1aaj "I brought my best tea today--"
    show yuuri at t22
    show natsuko 4w at f21
    n "Satori, did you move my..."
    show yuuri 1aab
    n 4k "Eh?"
    n 5c "Where is he?"
    n "He's never been late before..."
    show natsuko at t21
    show yuuri at f22
    y 1aak "Ugh... inconsiderate as usual, Natsuko."
    show yuuri at t22
    show natsuko at f21
    n 5g "..."
    n 7b "I know you're not talking to me..."
    show natsuko at t21
    show yuuri at f22
    y 3az "Well, who else is constantly interrupting my conversations with his incessant yelling?"
    show yuuri at t22
    show natsuko at f21
    n 3b "Okay, first of all..."
    n 5w "This is literally the first time I've interrupted any of your conversations."
    n 5b "So knock off the exaggerating."
    show yuuri 6ax
    n 3w "And secondly..."
    n 3f "Watch how you talk to me."
    n 5b "Because I'm the Vice President, in case you forgot."
    n "And Satori and I decided yesterday that we're going to be doing something for the festival."
    n 7g "I'm sorry, but that's how it is."
    show natsuko at t21
    show yuuri at f22
    y 1aay "Natsuko..."
    $ style.say_dialogue = style.edited
    y 6yandere13 "Nobody cares."
    show natsuko 7k
    y "Why don't you go play with your hair in the girls' bathroom or something?"
    $ style.say_dialogue = style.normal
    show yuuri at t22
    show natsuko at f21
    n 6p "WHAT?!"
    show natsuko at t21
    n 6o "..."
    show yuuri 6aak
    n 6r "..."
    show natsuko at thide
    hide natsuko
    show yuuri at t11
    "Natsuko suddenly stalks off to the back of the room towards the closet."
    show satori 3aab at f21
    show yuuri at t22
    s "Well, looks like I'm the last one here."
    show satori at t21 zorder 1
    show yuuri at f22 zorder 2
    y 4ay "What was holding you up?"
    show yuuri at t22 zorder 1
    show satori 1aai zorder 1
    "Satori briefly looks at me."
    show satori at f21 zorder 2
    s 1aah "I was talking to the Student Council President again, trying to get us that room sooner."
    s 1aan "But he said we have to wait until Monday. What an asshole."
    s 5aac "Anyway, I'm surprised to see you back in here, [player]."
    s 5aas "Thought this room creeped you out."
    show satori at t21 zorder 1
    mc "Hm? Well it's kinda dark and it smells like mildew."
    mc "But it's not so bad."
    show satori at f21 zorder 2
    s 5aat "Well... I'm glad you ended up seeing things my way."
    show satori at t21 zorder 1
    mc "..."
    show satori at t31 zorder 1
    show yuuri at t32 zorder 1
    show natsuko 5f at t33 zorder 1
    "I'm not really sure what Satori is referring to, but I don't have much time to think about it as I notice Natsuko return, carrying one of his larger boxes of manga."
    show natsuko at f33 zorder 2
    n "Hey, Yuuri."
    show natsuko at t33 zorder 1
    show satori 1aag zorder 1
    y 6aal "...?"
    show yuuri at f32 zorder 2
    y 4az "What do you want now?"
    show yuuri at t32 zorder 1
    show natsuko 6o zorder 1
    "Natsuko suddenly hurls the box of books through the air."
    #screen_glitch
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show yuuri 7aad
    show satori 1aax
    "It connects hard with the side of Yuuri's head."
    play sound "sfx/smack.ogg" # play_smack_audio
    play sound scatter_books
    show yuuri at f32 zorder 2
    y "ACK!"
    show yuuri at t32 zorder 1
    show satori 5aay
    "Satori ducks out of the way and I jump back with my hands up as the books scatter everywhere."
    show yuuri 7aaa
    "Yuuri retracts, holding his hand to the side of his head, moaning intensely."
    show natsuko at f33 zorder 2
    n 6p "I TOLD YOU TO WATCH HOW YOU TALK TO ME, FUCK-FACE!!!"
    show natsuko at t33 zorder 1
    #screen_glitch [x 2]
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show satori at f31 zorder 2
    s 5aab "Natsuko!!"
    s "What the hell is your problem??"
    show satori at t31 zorder 1
    show natsuko at f33 zorder 2
    n 6aac "HE'S MY PROBLEM!"
    n "HE NEVER RESPECTS ME AND I'M SICK OF IT!"
    show natsuko at t33 zorder 1
    #screen_glitch
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show satori at f31 zorder 2
    s 9aaq "This is not how you resolve that issue!!"
    s 8aaj "For God's sake, you just yeeted a box of books at his head!"
    show satori at t31 zorder 1
    show natsuko at f33 zorder 2
    n 6aad "YEAH, NEXT TIME, IT'LL BE A DESK!"
    show natsuko at t33 zorder 1
    show yuuri at f32 zorder 2
    y 6aac "Why you foul-tempered little shit..."
    y fight "I should snap you in half!!"
    show yuuri at t32 zorder 1
    #screen_glitch
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    "Yuuri suddenly stands up to his full height."
    show satori 1aax
    "He's unbelievably intimidating, and I disappear into his shadow."
    #screen_glitch [x 2]
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    "But small as he is, Natsuko doesn't seem to be bothered in the least."
    show natsuko fight at f33 zorder 2
    n "COME AT ME, DRACULA!!!"
    show natsuko at t33 zorder 1
    # screen_glitch [x 2]
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    #screen_pop

    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    hide noise onlayer front
    hide glitch_color onlayer front

    # I interpreted the "Textbox glitch"es as "When FeMC talks the textbox is glitched"
    $ style.say_window = style.window_monika
    $ style.say_dialogue = style.edited
    mc "THAT'S ENOUGH!" #[bold]
    $ style.say_dialogue = style.normal
    show yuuri 6aaf
    show natsuko 6h
    show satori 1aam
    $ style.say_window = style.window
    "I snatch one of the books from off the ground and hurl it between them, catching everyone's attention."
    "I point to Natsuko."
    $ style.say_dialogue = style.edited
    $ style.say_window = style.window_monika
    mc "You: outside. Now." # [bold]
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window
    n 6p "...!"
    show natsuko at f33 zorder 2
    n "But...but..."
    show natsuko at t33 zorder 1
    $ style.say_window = style.window_monika
    $ style.say_dialogue = style.edited
    mc "I SAID GET OUTSIDE!!" # [bold]
    $ style.say_window = style.window
    $ style.say_dialogue = style.normal

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    n 6c "..."
    n 6m "..."
    "Finally, Natsuko relents."
    show natsuko at f33 zorder 2
    n 7w "Fine! I'll do that!"
    n 7r "It'll spare me from having to look at his dumb face..."
    show natsuko at thide
    hide natsuko
    show yuuri at t22 zorder 1
    show satori at t21
    "With that, Natsuko storms out the door."
    "I then point to Satori."
    $ style.say_window = style.window_monika
    $ style.say_dialogue = style.edited
    mc "Go with him and calm him down." #[bold]
    $ style.say_window = style.window
    $ style.say_dialogue = style.normal
    show satori at f21 zorder 2
    s 7aas "Pfftt...you can't tell me what to...-"
    show satori at t21 zorder 1
    $ style.say_window = style.window_monika

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ style.say_dialogue = style.edited
    mc "GET THE FUCK OUT OF HERE NOW.....{cps=*4}" # [bold] {fast}
    $ style.say_dialogue = style.normal

    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    hide noise onlayer front
    hide glitch_color onlayer front

    show yuuri 6aam
    s 4aam "..."
    s 1aai "..."
    show satori at f21 zorder 2
    s 1aao "Ugh. Whatever."
    show satori at thide zorder 1
    hide satori
    show yuuri at t11
    "Satori reluctantly follows Natsuko outside."
    show yuuri 6aal
    "Yuuri takes a step towards the door."
    $ style.say_window = style.window_monika
    mc "Yuuri..."
    $ style.say_window = style.window
    y 6aax "[player], I..."
    mc "..."
    mc "Your head..."
    show yuuri 6aai
    "I notice a little bit of blood seeping from a small cut above Yuuri's left eyebrow."
    show yuuri 6aaa
    "Yuuri gently lifts his hand towards the injury and visibly winces as he brushes his fingers across it."
    y 6aam "It's fine. It didn't hurt as much as it looked..."
    "He must not realize he's bleeding."
    mc "Sit down, please."
    y 6aal "..."
    y 1aar "..."
    "He looks like he wants to object at first, but then he appears to change his mind."
    show yuuri at thide
    hide yuuri
    "He passivley takes a seat at one of the desks."
    "I approach his left side and brush some of his hair out of the way."
    show yuuri 6aad at t11
    y "...!"
    y 7aam "[player]..."
    mc "It's okay... I've got it."
    $ style.say_window = style.window_monika
    show yuuri at thide
    hide yuuri
    "I flick my tongue out and gently lick the blood away."
    $ style.say_window = style.window
    "Yuuri groans a little, but remains still." 
    "I take a closer look at the wound."
    "It's just a little cut."
    "The bruise around it is bigger than the cut itself."
    "But Yuuri's whimper of pain lets me know it still hurts."
    mc "Here...let me just..."
    show yuuri 7aaf at t11
    "I lean in close to his face and focus a small stream of breath directly onto the cut, gently blowing on it."
    mc "There we go."
    mc "Does that feel better?"
    "Yuuri just gazes up at me wordlessly."
    "I smile and giggle a little."
    mc "So..."
    mc "Do you still wanna read with me?"
    mc "I'm already engaged in the story, and..."
    y 6yandere11 "Yes! We can do whatever you want!"
    y 6aap "...Ah, I mean..."
    y 1aar "That sounds delightful."
    y 3aan "I'll get the book."

    $ nextscene = poemwinner[0] + "_exclusive2_" + "2"
    call expression nextscene

    return


label poem_show:

    $style.say_window = style.window
    $quick_menu = True

    scene bg club2_act2
    with dissolve_scene_half 
    play music t5_2 # Okay everyone 2


    menu:
        "Who should I show my poem to first?"
        "Yuri":
            pass


    show yuuri 6aw at t11
    y "At last..."
    y 6aav "Ahaha..."
    show yuuri 6aaw at t11
    "Yuuri sighs as he reads my poem. Afterwards, he holds it against the lower half of his face and gently inhales."
    show yuuri at t11
    y 1aaw "I love it."
    y "I love everything about it."
    y 6aah "[player], please let me take this home."
    y 3aar "I must have it."
    y 3aaq "I need it."
    show yuuri at t11
    mc "Sure, I don't mind."
    show yuuri at t11
    y 1aau "You're far too nice to me, [player]..."
    y 1aaw "I've never met anyone quite like you."
    show yuuri at t11
    "Yuuri slowly lowers my poem to his chest."
    show yuuri at t11
    y 1aah "I'm going to take this home with me and keep it in my room, right next to my bed."
    y 1aai "Do you like the thought of that?"
    y 1aag "I'll take very good care of it."
    $ style.say_dialogue = style.edited
    y 6yandere12 "When I get home, I'm gonna read it again while touching myself over and over." #[bold text]
    y 6yandere13 "I'll set it on fire and press the ashes into my fresh, open burns." #[bold text]
    $ style.say_dialogue = style.normal
    y 1aaw "I hope you'll want my poem, too."
    y 3aax "I mean... after you read it, I'm sure you'll want to take it home with you."

    $ currentpos = get_pos(channel="music")
    call showpoem (poem_empty, track="bgm/5_yuri2.ogg", revert_music=False, paper="mod_assets/images/bg/blood_poem.png", img="yuuri crazy", where=yface)

    show vignette zorder 100:
        alpha 0.0
        linear 2.0 alpha 1

    y "Do you like it??"
    show yuuri 1aah at t11
    y "I wrote it for you!"
    y 1aaj "I wrote this one with your pen too."
    y 1aar "I put a lot of... intimacy... into this poem."
    y 1aan "I was thinking of you the entire time."
    $ style.say_dialogue = style.edited
    y 1yandere12 "I think of you... all the time..." #{bold}
    $ style.say_dialogue = style.normal
    show yuuri at t11
    
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    hide vignette
    $ audio.t5_2 = "<from " + str(currentpos) + " loop 7.444>mod_assets/audio/okay_everyone_2.ogg"
    stop music_poem
    $ renpy.music.play(audio.t5_2)

    y 6aao "Ah!"
    y 6aam "Oh my..."
    y 7aao "Please excuse me!"

    show yuuri at thide
    hide yuuri

    "Yuuri rushes out the door right past Satori and Natsuko, who are just entering."
    show natsuko 1c at f11
    n "Jeez, what's his problem?"
    show natsuko at t21
    show satori 7aak at f22
    s "What were you two doing in here alone this whole time, [player]?"
    show satori at t22
    mc "Eh? Well, we started sharing our poems..."
    show natsuko at f21
    n 6p "What?"
    n 7w "Great, thanks for waiting for us!"
    show natsuko at thide
    hide natsuko
    show satori at t11
    "Natsuko slinks off to get his poem."
    show satori at f11
    s 9aao "Meh, I didn't write one last night."
    s 1aav "I'll start caring again on Monday."
    show satori at thide
    hide satori

    show natsuko 5q at f11
    n "Your dedication is staggering, Satori."
    n 5k "So, where's your poem, [player]?"
    show natsuko at t11
    mc "Ah, I let Yuuri have it."
    show natsuko 6o
    "Natsuko scowls, visibly upset."
    show natsuko at f11
    n 7x "Gross!"
    n 7r "Well, it's not like I wanted to read a Yuuri suck-up poem anyway!"
    n 5b "But I'm still going to make you read mine."
    show natsuko 5s at t11
    $ renpy.pause(0.1)
    show natsuko 5g at t11
    "Natsuko looks around nervously and lowers his voice."
    show natsuko at f11
    n 5aab "There's a reason."
    n 5n "I really had to do this..."
    n 5m "I'm sure you'll understand."
    n 7g "Just... read it carefully, okay?"

    call showpoem(poem_n23)

    show natsuko 7n at t11
    stop music

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    mc "..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    $ renpy.pause(0.1,hard=True)
    $ style.say_window = style.window
    # textbox_glitch
    # red_screen
    show darkred onlayer front:
        parallel:
            alpha 0.0
            linear 5 alpha 0.7
    $ config.allow_skipping = False
    $ quick_menu = False

    $ style.say_dialogue = style.edited
    mc "Natsuko..."
    show natsuko 5k at t11

    $ style.say_window = style.window_monika
    $ quick_menu = False
    mc "You must be completely insane if you think I believe this garbage."
    show natsuko 5m at t11
    mc "Forget everything you wrote down."
    mc "There's no point in trying to do anything."
    show natsuko 6aab zorder 2 at t11
    mc "If everyone is acting weird, it's because of you and your child-like imagination."
    mc "Do you hear me, Natsuko?"
    show noise zorder 1:
        parallel:
            alpha 0.0
            linear 5 alpha 0.7
    mc "This room is perfect and this club is perfect."
    show natsuko 6m zorder 2 at t11
    mc "Are you just trying to drive everyone away?"
    mc "This room is the only place we can be safe."
    mc "Don't ruin that for us."
    mc "Don't you dare fucking ruin it."
    mc "We're all staying here."
    mc "No one's escaping."
    show natsuko 6k zorder 2 at t11
    mc "Not even you."
    mc "You're not going anywhere, understand?"
    show natsuko 6aaa zorder 2 at t11
    mc "You're not going anywhere."

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide darkred onlayer front
    hide noise onlayer front

    play sound "sfx/crack.ogg"
    show natsuko scream_blood1


    mc "YOU'RE NOT GOING ANYWHERE!{cps=*2}"
    $ style.say_dialogue = style.normal
    window hide(None)
    $ style.say_window = style.window

    $ renpy.pause (2.5,hard=True)
    play sound "sfx/crack.ogg"
    show natsuko scream_blood2
    $ renpy.pause (2.5,hard=True)

    play sound "sfx/run.ogg"
    play sound "sfx/run.ogg"
    show natsuko at og_jmp_scare
    $ pause(0.25)
    hide natsuko
    scene black
    with None
    window auto
    scene black
    $ pause(0.5)
    show end:
        xzoom -1
    with dissolve_cg
    $ pause(2.0)
    scene black
    with None
    $ quick_menu = True
    return

label ch22_end:
    $ config.allow_skipping = True
    $ quick_menu = True
    # stop music fadeout 1
    scene bg club2_act2
    with dissolve_scene_half
    play music t3g fadein 3



    show satori 4aaa at f11
    s "Alright, guys."
    s "Time to make weekend plans for festival preparations."
    s 7aan "Chop-chop. I don't have all day."
    show satori at t21
    show natsuko 5z at f22
    n "Sweet! I've been waiting for this!"
    show natsuko at t22
    show satori at f21
    s 4aak "I assume you'll be handling the task of supplying the donuts, cupcake boy?"
    show natsuko 5c
    s 4aae "I know you're at least good at that."
    show satori at t21
    show natsuko at f22
    n 6f "..."
    n 7w "That's right."
    n 7r "I assume you'll be handling the task of being an asshole to everyone?"
    show satori 1aac
    n "I know you're at least good at that."
    show natsuko at t22
    show satori at f21
    s 1aat "Yes. Also, I'll be making poetry pamphlets."
    s 7aaa "As for Yuuri and [player]..."
    s 7aao "Well, you're both useless."
    show natsuko 7c at t32
    show yuuri 6aac at t33
    show satori at f31
    s 7aak "Feel free to be useless together, I suppose."
    show satori at t31
    show yuuri at f33
    y 6aak "I beg your pardon, Satori."
    y "But we're not useless."
    y 4aak "We can't very well have a successful poetry event without the right atmosphere."
    y 3ay "So I'll be handling the decorations."
    y 1az "It will be very meticulous work, so I would be more than happy to have [player]'s assistance."
    show yuuri at t33
    show natsuko at f32
    n 6p "Whoa, whoa, whoa!"
    n 6o "Hang on a second!"
    n 4b "Baking is pretty meticulous work too!"
    show natsuko at t32
    show yuuri at f33
    y 1aab "What, your donuts? Please."
    show yuuri at t33
    show natsuko at f32
    n 6f "And how the fuck would you know?"
    show natsuko at t32
    show satori at f31 zorder 2
    s 9aao "Hey, you know what?"
    s "I'll stop this bickering once and for all."
    s 4aaa "[player] will be helping {i}me{/i} this weekend."
    show satori at t31
    show natsuko at f32
    n 5b "Uh... like hell she is!"
    show natsuko at t32
    show yuuri at f33
    y 6aak "That's right!"
    y "Satori, your job is most suitable for one person."
    y 4aal "Wouldn't it make more sense for her to help one of us?"
    show yuuri at t33
    show satori at f31
    s 9aas "It would make way more sense."
    s 9aav "But I really don't feel like hearing you two bitching about who gets to work with her."
    s 6aas "Here's an idea... why don't you help each other?"
    s 7aas "Spend the weekend together and work out some of that sexual tension."
    show natsuko 5o
    show yuuri 6aaf
    s 1aak "It is actually scary how bad you two want each other."
    show natsuko 6p
    show yuuri 7aac
    show satori at t31
    show natsuko at f32
    show yuuri at f33
    ny "...!"
    show natsuko at t32
    show yuuri at t33
    show satori at f31
    s 3aae "There. Are we done?"
    show satori at t31 zorder 1
    show yuuri at f33
    y 6yandere14 "We sure as hell are {i}not{/i} done!"
    show yuuri at t33
    show natsuko at f32 zorder 2
    n 4p "Yeah! In fact, why don't we let [player] choose who she wants to work with instead of abusing your power?"
    show natsuko at t32 zorder 1
    show satori at f31 zorder 2
    s 9aab "Oh come on!"
    s 3aah "Does she really look like she cares?"
    s 3aag "She's been standing there dead-eyed for the past 5 minutes."
    s 7aav "You bore her as much as you bore me."
    show satori at t31
    show natsuko at f32
    n 7x "Satori, will you just shut the fuck up and let her make the choice?"
    show natsuko at t32
    show satori at f31
    s 4aal "You shut up."
    show satori at t31
    show yuuri at f33 zorder 3
    y 6az "Jesus Christ..."
    y 4ay "[player] please just choose one of us."
    show satori 1aai at t31
    show natsuko 7g at t32
    show yuuri 6aab at t33


    menu:
        " ":
            pass
        " ":
            pass
        " ":
            pass

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear


    mc "..."
    $ style.say_window = style.window_monika
    mc "Actually..."
    mc "I have plans this weekend."
    show satori 1aam
    show natsuko 6m
    show yuuri 6aaf
    mc "Sorry, I won't be able to help any of you."
    show natsuko at f32
    n 6v "Are you fucking kidding me?!"
    show natsuko at t32
    show satori at f31
    s 5aaf "Ahahahahaha!!!!"
    s "Well, there you have it!"
    show satori at t31
    show natsuko at f32
    n 6o "This isn't fair at all!"
    show natsuko at t32
    show satori at f31
    s 3aao "That's too damn bad."
    s "You wanted her to have a choice."
    show satori at t31
    show yuuri at f33
    y 4aak "Perhaps her plans can be changed?"
    y "It'd be awful to have to do all this work ourselves."
    show yuuri at t33 zorder 2
    show natsuko at f32 zorder 3
    n 4w "Nobody gave you any work, Yuuri."
    n "You decided it for yourself."
    show yuuri 6ax
    n 5b "I'm the one with the actual workload."
    n 7r "If she should be helping anyone, it's me."
    show natsuko at t32
    show yuuri at t33
    y 6yandere20 "..."
    y 6yandere13 "You?"
    stop music fadeout 3.0
    y 6yandere19 "Natsuko... I can't believe how delusional and self important you are."
    show satori 1aag
    show yuuri at t33
    show natsuko at f32
    n 5c "Excuse me?"
    show natsuko at t32 zorder 2
    show yuuri at f33 zorder 3
    y 4yandere15 "Did you ever think that she might have made up that excuse because she doesn't want to be around a pathetic child all day?"
    y 4yandere16 "Why you'd think anyone would want to be around an obnoxious little twerp like you boggles the mind."
    show natsuko 5o
    y 6yandere18 "Besides... it's obvious you hate yourself just as much as everyone else hates you."
    show natsuko 5h
    y 4yandere12 "Here's a suggestion...have you considered killing yourself?"
    show natsuko 5k
    show satori 1aam
    y 4yandere13 "It's not like anyone would miss you."
    y 6yandere15 "Plus, it would be beneficial to your mental health."
    show yuuri at t33
    show natsuko at f32
    n 5o "..."
    show natsuko at t32
    show satori at f31
    s 10aap "Dude..."
    show natsuko 6r
    show satori at t31
    "Natsuko clenches his fists in rage."
    "He looks like he's actually about to throw a desk at Yuuri's head."
    show natsuko 7r
    "But to my surprise, he actually takes a step back."
    show satori at thide
    hide satori

    show yuuri at t22
    show natsuko at f21
    n 7q "You know what?"
    n 7i "You're not even worth my time, you sick freak."
    "Natsuko snatches his book bag."
    n 5s "I'm going home."
    show natsuko at t21
    show yuuri at f22
    y 6yandere16 "That's right."
    y "Go home crying to your mommy."
    show natsuko 7r
    y 1yandere15 "Don't leave tear stains on your pretty new dress."
    show natsuko 7f
    show yuuri at t22
    "Natsuko pauses with an indignant huff."
    show natsuko at thide
    hide natsuko
    show yuuri at thide
    hide yuuri

    "He shoots Yuuri with one last glance of seething hatred before heading out the door."
    "Satori follows."
    $ style.say_window = style.window
    show satori 1aag at f11
    s "Hey, [player]..."
    s 4aak "Have a good weekend."
    show satori at thide
    hide satori
    "Satori flashes a sly smirk as Yuuri pushes him out the door."
    $ style.say_window = style.window_monika
    $ style.say_dialogue = style.edited
    "....GAH DON'T LEAVE ME ALONE WITH HIM!!{cps=*2}" #[bold] [fast]
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    python:
        try: renpy.file(config.basedir + "/It's getting hot in here!")
        except: open(config.basedir + "/It's getting hot in here!", "w").write("")

    return




label yuuri_confession:

    $ quick_menu = False
    $ config.allow_skipping = False

    play music t10y

    show yuuri 1aat at t11
    y "Finally..."
    y 6aav "Finally."
    y 6aw "This is what we both wanted, isn't it?"
    y 1aaw "[player]..."
    y 1aar "I've noticed you've been very forceful towards me the past few days."
    y 3aan "Pressing yourself against me when we read... pulling me in the closet with you... saying crazy, passionate things..."
    y 1aar "I want you to know..."
    y 1aah "I get the hint."
    y 1aai "And the answer is yes."
    mc "..."
    $ style.say_window = style.window_monika
    "WHAT THE HELL WAS THE QUESTION???{cps=*2}"
    $ style.say_window = style.window
    y 4aah "I wasn't sure I was picking up on your cues correctly at first."
    y 4aan "I didn't want to make any assumptions and accidentally come off as a lecher."
    y 6aar "But now that I know for sure, I can finally share my true feelings."
    y 1aaj "I have a confession to make..."
    y 1aar "The truth is..."
    y 1aaw "I'm madly in love with you!"
    y 6aah "It feels like every inch of my body-- every drop of blood in me-- is screaming your name."
    y 6aw "It's been making it impossible for me to focus on anything."
    y "I get aroused just being in the same room as you!"
    y 4aw "I think about you all the time."
    $ style.say_dialogue = style.edited
    y 6yandere13 "I even sodomize myself with the pen I stole from you." #{bold}
    $ style.say_window = style.window_monika
    "EW IT'S NOT EVEN MY PEN!{cps=*2}"
    $ style.say_window = style.window
    $ style.say_dialogue = style.normal
    y 1aaw "I love you so much, I've even burned your name into my arm."
    y 6yandere12 "I just want to shove you into an open oven and crawl inside to savor the flames with you."
    y 1aaw "Doesn't it feel nice to have someone want to revolve their entire life around you?"
    y 7aap "I dunno... maybe there's something wrong with me."
    mc "..."
    $ style.say_window = style.window_monika
    $ style.say_dialogue = style.edited
    "NO FUCKING WAY.{cps=*2}"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window
    y 7yandere13 "But I don't care anymore."
    y 6yandere17 "I don't even care if the ghost in here is listening!"
    show yuuri glitch
    $renpy.pause(3,hard=True)
    y 1yandere13 "[player], I just want you to be mine."
    y 1yandere18 "And I will be only yours."
    y 1yandere15 "Doesn't that sound nice?"
    y 6yandere13 "Tell me, [player]..."
    y 1aar "Will you be my lover?"
    y 1aah "Please say you accept my confession."

    window hide
    menu:
        "Okay":
            pass
        "Hell no":
            pass

    $ renpy.pause(1,hard=True)
    $ consolehistory = []
    call updateconsole("", "")
    $ renpy.pause(0.5,hard=True)
    call updateconsole("pip uninstall autopilot", "Uninstalled autopilot_program")
    $ renpy.pause(0.5,hard=True)
    call hideconsole

    stop music
    show yuuri 1yandere19 at t11

    window auto
    mc "Wha... I'm... back? I'm back! *sniff sniff* What the... I smell... lighter fluid? Oh, God...--Yuuri, listen to me..."
    y 1yandere15 "Hahahahaha!"
    mc "No no no no no... Just calm down..."
    y 1aat "Hahahahahahahahahahahaha!"
    mc "For the love of God, Yuuri..."
    y 1aav "Hahahahahahahahahahahahahahahahahahahahahaha!"
    mc "I'm fucking begging you!"
    $ style.say_dialogue = style.edited
    y 6yandere11 "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA!!! {cps=*3}"
    $ style.say_dialogue = style.normal
    window hide

    play music t6_2f

    show yuuri ligther at t11 zorder 1
    $ renpy.pause(2,hard=True)

    mc "NO!!!"

    play sound growing_fire
    show flames at t11 zorder 2
    show flames_mask onlayer front:
        additive 0.2
    play sound shrieking_audio
    $ renpy.pause(4.0,hard=True)
    stop music
    play sound "sfx/run.ogg"
    show flames at og_jmp_scare_y zorder 2
    show yuuri 6yandere19 at og_jmp_scare_y zorder 1
    $ pause(0.25)
    play sound "sfx/run.ogg"
    $ pause(0.25)
    play sound "sfx/run.ogg"
    $ pause(0.25)

    hide flames_mask onlayer front
    hide yuuri
    hide flames

    scene black
    with dissolve
    $ renpy.pause(3.0)

    return

label yuuri_death:
    if not config.developer:
        $ delete_all_saves()
    $ persistent.yuuri_kill = 0
    play music t6s
    $ config.allow_skipping = True
    $ quick_menu = True
    $ persistent.autoload = "yuuri_loop"
    $ renpy.save_persistent()
    label yuuri_loop:
        $ style.say_dialogue = style.edited
        $ config.allow_skipping = True
        $ quick_menu = True
        $ renpy.save_persistent()
        $ _history_list = []
        scene black
        window show(None)
        if not renpy.music.get_playing(channel='music') == audio.t6s:
            $ audiostart = str(renpy.random.random() * 360)
            $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
            play music t6s
        show y_kill at cgfade
        while True:
            if persistent.yuuri_kill <= 460:
                $ _history_list = []
                $ m.add_history(None, "","""What... what happened? What is this? Who... oh. Oh my God! OH MY GOD YUURI WHAT DID YOU DO?? OH MY GOD! OH MY GOD! SOMEBODY HELP! Why can't I move? AH! AH!!!! FFFFSSSSSSS.... AUGH, IT HURTS! Every part of my body is in excruciating pain! Oh my God...my skin...my skin is burned... I'm burned up! I'M ALL BURNED UP!! SOMEBODY PLEASE HELP ME!! AH... why can't I hear myself? Why can't I scream?  Oh my God.... somebody come find me please! Please... it hurts... so... much... [[Uncontrollable sobbing]. Please!! Please help me...""")
            elif persistent.yuuri_kill <= 660:
                $ _history_list = []
                $ m.add_history(None, "","""...Why would you do this? How could you do this? Now you're dead. You're fucking dead! AND I'M STUCK STARING AT YOUR DEAD FACE IN THE GRIP OF YOUR DEAD HANDS! YOU'RE SO LUCKY YOU DIED. I WASN'T SO LUCKY. I'M STILL ALIVE!!! AAAAUUUGGGHHH!!!! IT HURTS! ANYBODY, PLEASE, HELP!!!! WHY ISN'T ANYONE LOOKING FOR ME?! I'M HERE! I'M UP HERE! SOMEBODY, PLEASE!! Help me! HEL-...! [[Uncontrollable coughing/gagging] [[Uncontrollable sobbing]""")
            elif persistent.yuuri_kill <= 920:
                $ _history_list = []
                $ m.add_history(None, "",""" ... ... ... Satori... Come... find... me... I don't know... how much longer... I can hold on... I'm so weak. I'm so thirsty. And the smell... it's overwhelming. The smoke is thick and nauseating. Every breath burns my lungs. My throat is raw from trying to scream. I can't scream. I can bearly move. Every single twitch or shift in weight is agonizing. I can't get up. I can't crawl. With maximum effort, I can stretch my neck and lift my head ever so slightly, and not without excruciating pain as my consequence. I can't see anything. I don't know if I ever will again. I don't know know how long I've been here. The smoke scent is disappearing. I smell a new scent. It's distracting me from the pain. Why... why... why do I smell...bacon? Oh my God. It's making me so hungry. You make me so hungry, Yuuri... You're still... so cute... ... ... I could just... Eat. You. Up.""")
                if not played_sound:
                    play sound tearing_flesh
                    $ played_sound = True
            else:
                $ _history_list = []
                $ m.add_history(None, "","""Hey there, Player! Welcome to the Literature Club! It's been a dream of mine to be a part of a DDLC mod that will take you back to the world and amazing story we all love. If you'd like to be a club member as well, then prepare to relive the dream in this cute genderswitch game! Every day will be full of chit chat and fun activities with all of the handsome and unique club members! Satori, the cute and funny mellow dude who values your happiness the most; Natsuko, the fiesty short guy who's adorably flirty; Yuuri, the shy and intelligent gentleman who finds comfort in the world of books; And, of course, me, Mateo, the confident and witty leader of the Club! I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all of us. But I can tell you're already excited to get started! Will you promise to make her spend time with me? I mean...since you're here anyway, you might as well be of some use to me.""")
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            y "[gtext]"
            # $ _history_list.pop()

            if persistent.yuuri_kill >= 1400:
                jump monday

            $ persistent.yuuri_kill += 1

label monday:
    $ persistent.autoload = "monday"
    if not config.developer:
        $ delete_all_saves()    #Wouldn't want people loading into yuuri_loop
    $ style.say_dialogue = style.normal

    stop music fadeout 1
    scene bg club2_act2
    with dissolve_scene_half



    show natsuko 5z at t11
    n "Alright, it's festival time!"
    n 6b "..."
    n scream "What the fuck..."
    n 6aaa "Oh my God!"
    n "Wha-wha-what happened in here?!"
    n "Ugh..."
    n scream "Oh, God..."
    n "I---I..."
    n 6aaa "I'll go get he-..."
    $ config.allow_skipping = False
    n 6v "Ah-..."
    show white onlayer front:
        alpha 1
        easeout 1.5 alpha 0
    play sound stab
    show satori kill1 at tcommon(700,0.80) zorder 1
    show natsuko death1 zorder 2
    $ renpy.pause(1.5,hard=True)

    show natsuko_stabby at t11 zorder 3
    n "..."
    window hide(None)

    $ renpy.pause(1.5,hard=True)
    show bleed at t11 zorder 3
    show natsuko death2 zorder 2
    $ renpy.pause(3,hard=True)
    show natsuko_drip at t11 zorder 3
    $ renpy.pause(3,hard=True)


    show natsuko death2 zorder 2 at dunk
    show bleed zorder 3 at dunk
    show natsuko_drip zorder 3 at dunk
    play sound fall
    hide natsuko_stabby

    $ renpy.pause(0.8,hard=True)
    hide natsuko
    hide bleed
    hide natsuko_drip
    $ renpy.pause(0.5,hard=True)
    # show command_box

    $ consolehistory = []
    call updateconsole("", "")
    $ renpy.pause(0.5,hard=True)
    call updateconsole("DEL basedir+\"/characters/natsuko.chr\"","DEL basedir+\"/characters/natsuko.chr\"")
    if not config.developer:
        $ delete_character("natsuko")
    $ renpy.pause(0.5,hard=True)
    call hideconsole

    show satori 2aak at t11
    s "Well, it's about time we got to this part."
    s "Lemme just clean up in here."
    s 1aam "..."
    s 1aaj "Ew, what the-..."
    s 1aam "Did she eat part of his face?!"
    s 5aae "Savage!"
    s 1aag "Looks like she didn't die right away. I bet it took all weekend."
    s 4aah "Man, she must've really suffered."
    s 10aap "..."
    s 10aau "I... I didn't think..."
    s 1aav "Ugh... I shouldn't dwell on it."
    s 1aao "Let me just get this going."
    $ renpy.pause(0.5,hard=True)
    call updateconsole("DEL basedir+\"/characters/femc.chr\"","DEL basedir+\"/characters/femc.chr\"")
    if not config.developer:
        $ delete_character("femc")
    $ renpy.pause(0.5,hard=True)
    s "Almost done..."
    $ renpy.pause(0.5,hard=True)
    call updateconsole("DEL basedir+\"/characters/yuuri.chr\"","DEL basedir+\"/characters/yuuri.chr\"")
    if not config.developer:
        $ delete_character("yuuri")
    $ renpy.pause(0.5,hard=True)
    s 1aav "There we go."
    call hideconsole
    s 1aau "..."
    s 1aac "Now then... how about you two get to know each other a little better?"
    s 7aaa "This will only take a second."

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    if not config.developer:
        $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.autoload = "ch30_main"
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="glitched_splashscreen")

    return