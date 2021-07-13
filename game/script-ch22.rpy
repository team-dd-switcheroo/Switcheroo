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

    # if appeal_n_day1:
    #     call appeal_n_day1
    # else:
    #     call appeal_y_day1

    menu:
        "appeal_n_day1":
            call appeal_n_day1
        "appeal_y_day1":
            call appeal_y_day1


    call poem_show
    call ch22_end
    call yuuri_confession
    call yuuri_death

    return

label appeal_n_day1:
    scene bg club2_act2
    with wipeleft
    # play music t6_2 fadein 2.0


    show yuuri 1aag at t11
    y "Actually, I have a request." 
    y "Do you mind if I make some tea first?"
    mc "Not at all."
    y 1aaw "Thanks very much!" 
    y 3aaj "If there's one thing that can make my reading time here any better, it's a nice cup of tea." 
    y "Not to mention for yourself as well."
    show yuuri at thide
    hide yuuri
    "Yuuri stands up and walks to the closet." 
    "I follow and watch as he retrieves a pitcher from the shelf-- the kind with a filter inside."
    show yuuri 4aak at t11
    y "Could you hold this for a second?"
    "Yuuri hands me the pitcher and fetches an electric kettle." 
    y 4aaj "I'm going to plug this in at the teacher's desk and then I'll go get some water."
    show yuuri at thide
    hide yuuri
    "He walks past me and sets the kettle on the teacher's desk." 
    "I simply watch his movements." 
    "His broad shoulders and long torso make Yuuri appear elegant, yet masculine, and methodical."
    show yuuri 1aaj at t11
    y "Okay, may I have the water pitcher?"
    mc "Here you go."
    y 1aaw "Thanks. I'll be right back." 
    mc "Ah, I might as well go with you..."
    y 1aam "Oh...don't trouble yourself!"
    y 1aan "You stay here."
    y 1aar "I won't be long."
    show yuuri at thide
    hide yuuri
    "Pitcher in hand, Yuuri hurries out of the classroom."


    show black
    with dissolve_scene
    stop music fadeout 8.0


    "..."
    "..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    "..."
    "..."
    $ style.say_window = style.window
    # textbox_glitch
    # playaudio growing_fire
    play sound growing_fire fadein 3.0
    "..."
    "..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    "...What's that sound...?"
    # $ currentpos = get_pos(channel="music")
    # stop music fadeout 1.0



    # scene tilted bg club2_act2 with slow zoom-in
    scene bg club2_act2 at truecenter:
        subpixel True
        rotate -3
        zoom 1.2
    with wipeleft

    show layer master at truecenter:
        ease 10 zoom 1.265

    # stop music fadeout 1.0

    $ config.allow_skipping = False

    # play sound hb
    $ renpy.pause(0.2, hard=True)
    show flames_mask onlayer front:
        additive 0.2
    $ renpy.pause(5, hard=True)

    $ config.allow_skipping = True

    play music t6_2
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
    hide flames_mask onlayer front

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

    $ renpy.pause(1) # Gotta let the screen pop breath

    
    scene black
    # with dissolve

    
    mc "KYYYYYYYAAAAAA!!"


    scene bg club2_act2
    with wipeleft


    show yuuri 7aaf at h11
    y "Goodness!"
    "Yuuri jumps back, almost spilling the water in the pitcher he's holding."
    $ style.say_window = style.window
    # textbox_glitch
    mc "...!"
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "You're back."
    show yuuri 7aaf
    y "..."
    y 1aal "Ah--... yes!"
    y 3aaj "There's no running water up here, so I had to go downstairs to fill the pitcher."
    y 1aam "..."
    y 1aan "I admit... I kind of got turned around and, well... forgot what I went down there for in the first place..."
    y 7aao "Um... I'm sorry, I didn't realize I'd been gone for over 10 minutes."
    y 6aaq "I can see why you dozed off."
    mc "..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "So what kind of tea did you bring?"
    show yuuri 6ay
    # textbox_glitch
    $ style.say_window = style.window_monika

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    # screen_glitch
    y 6ax "Well... I thought it'd be nice to have some oolong tea today."
    y 4aaw "Wouldn't you agree?"
    mc "Sure."
    y 4aar "Very well."
    "Yuuri sets the temperature on the kettle to 200 degrees."
    y 4aaj "Now it's time to get the teapot."
    mc "You really do this properly, don't you?"
    y 4aag "Of course..."
    y "I shouldn't do any less when I'm making tea for others."
    y 1aah "Especially you..."
    mc "Even if I'm not an expert on tea or anything...?"
    y 1aaw "Haha."
    y 1aar "In that case, you'll only be even more impressed."
    mc "Ah... perhaps I will!"
    show yuuri at thide
    hide yuuri
    "Yuuri fetches the teapot and begins measuring the tea leaves."
    "To my surprise, he even starts humming a little to himself."
    mc "You must be in a good mood now..."
    show yuuri 1aaw at t11
    y "Is that so?"
    y 1aat "I was letting it show..."
    y 1aai "And you noticed."
    y 1aah "I was doing a bit of thinking..."
    y 1aaw "And I decided that I would try expressing myself a little bit more."
    y 3aax "It turns out it's not very hard for me to do..."
    y 1aar "When it's you who's around, anyway."
    mc "Ah..."
    mc "That's great, Yuuri!"
    mc "Just don't push yourself too much."
    y 1aau "You're always worrying about me, [player]..."
    y 1aar "It's very endearing."
    mc "That's..."
    show yuuri at thide
    hide yuuri
    "Yuuri wasn't kidding..."
    "I don't even know if I can keep up with this...!"
    "I watch Yuuri pour a cup of tea for each of us."
    show yuuri 4aag at t11
    y "[player], I have an idea."
    y "How about we sit on the floor today?"
    mc "Um, yeah, that's fine."
    mc "Any particular reason why?"
    y 3aaj "Well... I think it may be more comfortable for you considering your figure."
    show yuuri 1aar
    "His eyes slowly travel down to my chest."
    y 3aah "It's probably not very good for your lower back to be reading while slouched over a desk."
    y "Sitting on the floor will improve your posture."
    show yuuri 1aaj
    "His gaze finally returns to my face."
    mc "Ah... I-I suppose that makes sense."
    show yuuri at thide
    hide yuuri
    "Yuuri and I then sit against the wall, teacups at our sides."
    "He opens the book and I find I'm having a very difficult time seeing the text from here."
    mc "I can't really see."
    show yuuri 4aah at t11
    y "Oh? Is this better?"
    show yuuri at thide
    hide yuuri
    "He scoots closer until he's pressed against me."
    "He holds the book so that I don't have any harder of a time reading from it."
    "But as a result, my left arm is practically resting on top of his leg."
    "How am I supposed to focus on reading like this...?!"
    $ style.say_window = style.window
    # textbox_glitch
    "How is HE supposed to focus on reading like this?{cps=*4}" # Fast
    # textbox_glitch
    $ style.say_window = style.window_monika
    "We both make an attempt to put on intense reading expressions."
    "After a few moments, we both relax a little."



    scene yuuri_day2_act2_cg1
    with dissolve_cg



    "We read quietly for a while."
    "Suddenly, I feel a chilly breeze nip the back of my neck."
    "I shudder a bit."
    show yuuri_day2_act2_cg3 at cgfade
    "It must've been more than I thought, as it seems to have caught his attention."
    show yuuri_day2_act2_cg4 at cgfade
    y "Are you alright?"
    mc "Yeah. Sorry, I just felt a random chill in the air."
    show yuuri_day2_act2_cg3 at cgfade
    y "A random chill, you say?"
    show yuuri_day2_act2_cg7 at cgfade
    y "Interesting."
    y "Perhaps the rumor is true..."
    mc "The one about the girl who killed herself up here?"
    show yuuri_day2_act2_cg8 at cgfade
    y "Ah, you know the story?"
    mc "Yeah. Natsu told me the other day."
    show yuuri_day2_act2_cg1 at cgfade
    y "Do you believe it, [player]?"
    "He smiles knowingly."
    mc "I'm... not sure."
    mc "Do you?"
    show yuuri_day2_act2_cg4 at cgfade
    y "Well..."
    y "I can\'t say for sure whether or not it happened..."
    y "It would be very unfortunate if it was true, though."
    y "The poor girl..."
    mc "Do you believe in ghosts, Yuuri?"
    "A chill runs down my spine as I ask that."
    $ style.say_window = style.window
    # textbox_glitch
    "...And I suddenly remember just how creepy this room really is."
    "Why did I even come back here?"
    show yuuri_day2_act2_cg6 at cgfade
    y "Hm..."
    y "I\'ve never experienced an encounter with one."
    show yuuri_day2_act2_cg16 at cgfade
    y "But that doesn\'t mean they don\'t exist."
    show yuuri_day2_act2_cg6 at cgfade
    y "That said..."
    y "I don't think this room is haunted, per se."
    y "There can be many explanations for the strange things that happen up here."
    show yuuri_day2_act2_cg4 at cgfade
    y "The scratching on the windows is just the overgrown tree branches outside scraping against the glass."
    y "The sounds of scuttering in the walls are just mice, or a raccoon, at most."
    y "The eerie whistling can be attributed to the wind blowing in through the cracks in the windows."
    y "The chilly bite in the air..."
    show yuuri_day2_act2_cg16 at cgfade
    y "Just a breeze."
    y "The damp smell comes from the mildew."
    y "All of it can be explained."
    show yuuri_day2_act2_cg1 at cgfade
    y "So you see, the creepiness in this room..."
    show yuuri_day2_act2_cg16 at cgfade
    y "Is just your imagination."
    show yuuri_day2_act2_cg1 at cgfade
    y "Even if someone did die up here..."
    y "It just adds to the ambiance of it all."
    show yuuri_day2_act2_cg4 at cgfade
    y "To be completely honest..." 
    y "Everyone else might want a newer, nicer room downstairs..."
    show yuuri_day2_act2_cg1 at cgfade
    y "But I kind of like it up here."
    mc "..."
    mc "You like it up here?"
    show yuuri_day2_act2_cg11 at cgfade
    "Yuuri laughs a little."
    y "Of course..."
    y "It doesn't bother you, does it?"
    mc "Well, no..."
    show yuuri_day2_act2_cg1 at cgfade
    y "And... if there is a ghost up here..."
    y "I'd like to talk to her..."
    show yuuri_day2_act2_cg16 at cgfade
    y "It would be immensely fascinating to chat with an apparition."
    y "Don't you think?"
    show yuuri_day2_act2_cg6 at cgfade
    y "It may even be interesting to... to..."
    show yuuri_day2_act2_cg11 at cgfade
    y "Be possessed by the spirit..."
    mc "...!"
    show yuuri_day2_act2_cg7 at cgfade
    y "Oh..."
    show yuuri_day2_act2_cg8 at cgfade
    y "I didn't frighten you, did I?"
    mc "N-n-no. Of course not."
    "Again, the bitter cold chill runs across my neck."
    "Without thinking, I lean into Yuuri even more."
    show yuuri_day2_act2_cg3 at cgfade
    mc "S-sorry."
    mc "It's just cold in here and..."
    mc "You're...you're just really...warm..."
    show yuuri_day2_act2_cg2 at cgfade
    stop audio
    "Yuuri's expression breaks."
    "He starts to tremble."
    show yuuri_day2_act2_cg12 at cgfade
    y "A-Ah..."
    show yuuri_day2_act2_cg13 at cgfade
    "He starts to breathe heavily."
    y "I..."
    y "I can't..."
    y "[player]..."
    mc "Shh...Yuuri..."
    # textbox_glitch
    $ style.say_window = style.window_monika

    scene black
    with wipeleft_scene
    stop music fadeout 1.0


    $ style.say_window = style.window
    # textbox_glitch
    "Suddenly, I forcefully grab Yuuri and pull him to his feet."
    # textbox_glitch
    $ style.say_window = style.window_monika
    "Our teacups get knocked over."
    $ style.say_window = style.window
    # textbox_glitch


    show bg closet_act2
    with wipeleft



    show yuuri 6aam at t11
    y "[player]..."


    play sound closet_close

    show dark zorder 100:
        alpha 0.7


    # textbox_glitch
    $ style.say_window = style.window_monika
    "Once in the closet, I press myself against Yuuri's torso, wrapping my fingers around the sides of his jacket."
    mc "Yuuri..."
    play music hb
    show layer master at heartbeat
    $ style.say_window = style.window
    # textbox_glitch
    $ style.say_dialogue = style.edited
    mc "I've felt this..." #{bold from here on}
    show yuuri 6aaf
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "I've felt it since the day I joined this club." 
    # textbox_glitch
    mc "There's something wrong with this room, Yuuri." 
    # textbox_glitch
    mc "I don't know what it is."
    # textbox_glitch
    mc "But every time I come up to this room, my heart starts pounding."
    # textbox_glitch
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    mc "You feel it too, don't you?" 
    # textbox_glitch
    mc "It's driving me crazy."
    # textbox_glitch
    mc "I can't focus on anything."
    # textbox_glitch
    mc "But...I just..."
    # textbox_glitch
    mc "Feel so safe...in your arms..."
    show yuuri at m_yface # up-close
    # textbox_glitch
    mc "Will you keep me safe, Yuuri?"
    # textbox_glitch
    mc "Will you..."
    # textbox_glitch
    mc "Keep me..."
    # textbox_glitch
    mc "Safe?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window
    # textbox_glitch # Stop bold
    $ renpy.pause(0.2)
    $ style.say_window = style.window_monika
    $ renpy.pause(0.2)
    # textbox_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ style.say_window = style.window
    # textbox_glitch
    # screen_glitch
    y 6aam "Haah..."
    y 6aan "[player]... I..."
    y 6yandere20 "... I... I--..."



    stop music
    play sound closet_open

    show layer master

    hide dark

    show yuuri 7aao at t11 with None

    mc "Gah!"
    "A gust of wind whips through the room, yanking open the closet door."
    "Startled, both Yuuri and I leap away from each other."
    "I look around, confused."
    "I'm not sure what happened that caused us to find ourselves in such a compromising position, but I can tell Yuuri seems just as confused and shaken up as I am."
    mc "Um..."
    y 7aao "[player]... I-I'm sorry..."
    mc "It's fine, Yuuri."
    mc "Why don't we share our poems now?"
    y 7aan "Y-yes."
    y 6aaq "Let's do that."

   

    scene black
    with dissolve_scene_full

    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))

    if _return:
        call expression "poem_special_a4m"    # Anything for mother
        scene black with Dissolve(1.0)
    else:
        call expression "poem_special_dyr"    # FeMC's diary
        scene black with Dissolve(1.0)

    return


label appeal_y_day1:


    scene bg club2_act2
    with wipeleft

    # play music t6_2 fadein 2.0


    show yuuri 1aag at t11
    y "Actually, I have a request." 
    y "Do you mind if I make some tea first?"
    mc "..."
    mc "Maybe later."
    mc "I'd like to start reading now, if you don't mind."
    y 1aaf "Ah..."
    y 1aal "Very well."
    y 3aar "In that case, where would you like to read today, [player]?"
    mc "I don't mind sitting on the floor again."
    y 1aaw "As you wish."
    show yuuri at thide
    hide yuuri
    "Like yesterday, Yuuri and I take a seat on the floor."
    "Within moments, we're both engrossed in the story."



    scene yuuri_day2_act2_cg1
    with dissolve_cg


    # textbox_glitch
    $ style.say_window = style.window_monika
    "I smile to myself a little and Yuuri notices."
    y "You seem to be in a good mood today."
    $ style.say_window = style.window
    # textbox_glitch
    mc "It's just nice...you know...to have the room to ourselves."
    # textbox_glitch
    $ style.say_window = style.window_monika
    "Yuuri smiles at me in return."
    show yuuri_day2_act2_cg16 at cgfade
    y "Yes...it is nice, isn't it?"
    mc "I'm just trying to enjoy it while it lasts."
    $ style.say_window = style.window
    # textbox_glitch
    show yuuri_day2_act2_cg1 at cgfade
    mc "Actually...I was doing a bit of thinking..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "I want to try expressing myself a little bit more."
    $ style.say_window = style.window
    # textbox_glitch
    show yuuri_day2_act2_cg11 at cgfade
    y "Something tells me that won't be very hard for you to do."
    mc "Well, it's easier for me when it's you who's around..."
    show yuuri_day2_act2_cg2 at cgfade
    # textbox_glitch
    $ style.say_window = style.window_monika
    show yuuri_day2_act2_cg3 at cgfade
    y "Ah..."
    show yuuri_day2_act2_cg12 at cgfade
    y "That's..."
    show yuuri_day2_act2_cg11 at cgfade
    y "I'm...glad you feel that way, [player]."
    y "I like to see you happy."
    mc "You worry about my happiness..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "That's so endearing."
    # textbox_glitch
    $ style.say_window = style.window_monika
    show yuuri_day2_act2_cg3 at cgfade
    y "..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show yuuri_day2_act2_cg4 at cgfade
    y "Haven't we had this conversation before...but, switched up?"
    $ style.say_window = style.window
    # textbox_glitch
    mc "Yeah, you're feeling this weird deja vu too, right?"
    # textbox_glitch
    $ style.say_window = style.window_monika
    "We sit quietly for a moment, equally confused."
    show yuuri_day2_act2_cg3 at cgfade
    "A breeze causes the tree branches outside to slam against the window, making me a jump a little."
    $ style.say_window = style.window
    # textbox_glitch
    "...And I suddenly remember just how creepy this room really is." #{bold}
    # textbox_glitch
    $ style.say_window = style.window_monika
    "Why did I even come back here?"
    $ style.say_window = style.window
    # textbox_glitch
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    stop music fadeout 1.0
    "My head has been so fuzzy lately, I don't know what I'm doing anymore."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "I think I need some fresh air."
    $ style.say_window = style.window
    # textbox_glitch
    "I go to stand up, holding onto Yuuri's arm to steady myself."
    show yuuri_day2_act2_cg7 at cgfade
    y "Khhhhh--!"
    "Yuuri inhales sharply, as though he's in pain."


    scene bg club2_act2
    with dissolve_scene

    show yuuri 7aaa at t11
    "I immediately release his arm and jump to my feet, startled."
    mc "Oh!"
    mc "I'm sorry! Are you okay?"
    y 7aao "I-I'm fine!"
    y 7aap "D-don't worry about it!"
    show yuuri 7aam
    "He anxiously rubs his arm, where I grabbed him."
    "I can't understand how my weight could have hurt him..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    "..."
    $ style.say_window = style.window
    # textbox_glitch
    "I suddenly remember what Natsuko told me yesterday."
    # textbox_glitch
    $ style.say_window = style.window_monika
    "About Yuuri burning himself."
    $ style.say_window = style.window
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    # textbox_glitch
    $ style.say_window = style.window_monika
    "I didn't think much of the accusation at the time, but now..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "Yuuri..."
    mc "Can..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "Can I see your arms?"
    $ style.say_window = style.window
    # textbox_glitch
    show yuuri 7yandere20
    show yuuri 7aao
    "He gives me a worried look before abruptly looking away."
    y 7aan "W-why that all of a sudden?"
    mc "Just let me..."
    show yuuri 7aao
    "I reach for his sleeves but he quickly retracts."
    y "N-no!"
    y 6aai "You can't!"
    mc "Why not?"
    y 6aam "Because..."
    y 4aam "I would hate for you to think I'm weird just after we started spending time together..."
    y 6ay "I mean..."
    y 1ax "You've already seen how I can't control myself when I get too excited about something."
    y 1aam "I don't want you to know about the... other unusual things about me."
    y 3aam "After all, expressing those things so soon after meeting someone is usually seen as inappropriate... or unlikable."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "What kind of things?"
    $ style.say_window = style.window
    # textbox_glitch
    y 1aal "My obsession...with certain hobbies."
    mc "Yuuri..."
    y 6yandere13 "My obsession... is fire."
    y 4ax "It sounds strange, but you wouldn't understand if you've never seen how beautiful it can be."
    y 4aag "I... I even have a collection of lighters."
    y 1aaj "I've gotten them all from various artisans."
    y "I make sure to give them all their fair share of use."
    y 1aag "I don't want them to get lonely or anything..."
    y 1aak "Nobody deserves to be lonely..."
    mc "So... you just like looking at the fire?"
    y 7aao "I..."
    "Yuuri looks away."
    y 6aay "I think that's... personal information that I'd rather not share."
    # textbox_glitch
    $ style.say_window = style.window_monika
    # screen_glitch
    show yuuri 7aao
    "I suddenly slam my palms on a desk."
    $ style.say_window = style.window
    # textbox_glitch
    mc "Look, if you're hurting yourself, you better not be doing it because of me!" #[bold]
    y 7aam "...!"
    # textbox_glitch
    $ style.say_window = style.window_monika
    # screen_glitch
    # screen_glitch

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

    "..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "Yuuri... I'm so sorry!"
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "I didn't mean to snap like that..."
    $ style.say_window = style.window
    # textbox_glitch
    mc "It's just..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "It's this damn room."
    $ style.say_window = style.window
    # textbox_glitch
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ quick_menu = False
    mc "My heart goes crazy every time I come here."
    # textbox_glitch
    $ style.say_window = style.window_monika

    $ config.allow_skipping = False
    play music hb
    show layer master at heartbeat

    show vignette zorder 100:
        alpha 0.0
        linear 3.0 alpha 0.75


    mc "Like it's going to rip out of my chest."
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show yuri_ghost_bg
    $ style.say_window = style.window
    # textbox_glitch
    mc "It overwhelms me with energy and emotions that just come exploding out."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "It's been making me say and do weird things."
    $ style.say_window = style.window
    # textbox_glitch
    $ style.say_dialogue = style.edited
    mc "I'm not crazy, right?" #{bold} [
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    show yuuri 7aaf
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "Please tell me I'm not!"
    $ style.say_window = style.window
    # textbox_glitch
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    mc "I just want to get out of here."
    # textbox_glitch
    $ style.say_window = style.window_monika
    # screen_glitch
    mc "All of us need to get out of here."
    $ style.say_window = style.window
    # textbox_glitch
    mc "We need to leave now."
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    hide yuri_ghost_bg
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "If we wait... it might not let us leave."
    $ style.say_window = style.window
    # textbox_glitch
    mc "Yuuri, every second I'm in here makes me want to stab myself in the throat!"
    show yuuri 7aam
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    # textbox_glitch
    $ style.say_window = style.window_monika

    # ghost_yuri [layering begins slowly]
    show screen yuri_ghost
    mc "I'm not joking!"
    $ style.say_window = style.window
    # textbox_glitch
    mc "Actually, I have an idea."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "We'll go to my house!"
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ style.say_window = style.window
    # textbox_glitch
    show yuuri 7aaf
    mc "All of us..."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "We'll hide in my room."
    $ style.say_window = style.window
    # textbox_glitch
    mc "It won't be able to get us in there."
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "We'll all just stay in my room and play video games."
    $ style.say_window = style.window
    # textbox_glitch
    mc "Every day."
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    # textbox_glitch
    $ style.say_window = style.window_monika
    # screen_fade -----------------------------------------------------


    mc "That's all we need."
    show black onlayer screens zorder 1:
        alpha 0.06
    $ style.say_window = style.window
    # textbox_glitch
    mc "In fact..."
    show black onlayer screens zorder 1:
        alpha 0.12
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "Let's all quit the Literature Club!"
    show black onlayer screens zorder 1:
        alpha 0.18
    $ style.say_window = style.window
    # textbox_glitch
    mc "There's no need to be anywhere near this evil room."
    show black onlayer screens zorder 1:
        alpha 0.24
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "We just need to stick together."
    show black onlayer screens zorder 1:
        alpha 0.30
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ style.say_window = style.window
    # textbox_glitch
    mc "All of us."
    show black onlayer screens zorder 1:
        alpha 0.36
    # textbox_glitch
    $ style.say_window = style.window_monika
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    # screen snow effect
    show noise zorder 3 at noise_alpha:
    mc "Doesn't that sound perfect?"
    show black onlayer screens zorder 1:
        alpha 0.42
    $ style.say_window = style.window
    # textbox_glitch
    mc "This way, we'll all be safe."
    show black onlayer screens zorder 1:
        alpha 0.48
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "That's why I was meant to join the club in the first place, isn't it?"
    show black onlayer screens zorder 1:
        alpha 0.54
    $ style.say_window = style.window
    # textbox_glitch
    mc "It was fate."
    show black onlayer screens zorder 1:
        alpha 0.60
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "I'm meant to save you all."
    show black onlayer screens zorder 1:
        alpha 0.66
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ style.say_window = style.window
    # textbox_glitch
    mc "It'll be the happy ending we all want." 
    show black onlayer screens zorder 1:
        alpha 0.72
    # textbox_glitch
    $ style.say_window = style.window_monika
    mc "So let's go!" 
    show black onlayer screens zorder 1:
        alpha 0.78
    # screen_glitch

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    $ style.say_window = style.window
    # textbox_glitch
    mc "We have to, or it'll kill us all!"  # {fast}
    show black onlayer screens zorder 1:
        alpha 0.84
    # textbox_glitch
    $ style.say_window = style.window_monika
    $ gtext = glitchtext(40)
    mc "[gtext]" # {bold} ]  {fast}
    show black onlayer screens zorder 1:
        alpha 0.90
        linear 0.1 alpha 1
    $ style.say_dialogue = style.normal
    show layer master
    stop music
    hide vignette

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    hide black onlayer screens
    show black
    hide noise

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    # Show ghost yuuri

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear


    # show black_bg with ghost_yuri
    # ghost_yuuri_screen_rush with audio_scream

    window hide
    hide black onlayer screens
    hide screen yuri_ghost
    show yuri_ghost_img at jmp_scare
    $ renpy.pause(3, hard=True)
    play sound shrieking_audio
    $ renpy.pause(1,hard=True)
    hide yuri_ghost_img

    # scene black
    # with dissolve_scene_full
    # black_screen
    $ renpy.pause(3.0, hard=True)
    $ consolehistory = []
    call updateconsole("", "")
    # show command box
    $ renpy.pause(0.5, hard=True)
    call updateconsole("pip upgrade autopilot", "Successfully installed autopilot-4.0")
    # femc_autopilot_v4.0_successfully_installed
    $ renpy.pause(0.5,hard=True)
    call hideconsole

    $ config.allow_skipping = True


    # special_poem_unlocked
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))

    if _return:
        call expression "poem_special_a4m"   # Anything for mother
        scene black with Dissolve(1.0)
    else:
        call expression "poem_special_dyr_y" # Yuuri's diary
        scene black with Dissolve(1.0)
    $ quick_menu = True

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
    call updateconsole("DEL basedir+\"/characters/natsuko.chr\"","")
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
    call updateconsole("DEL basedir+\"/characters/femc.chr\"","")
    $ renpy.pause(0.5,hard=True)
    s "Almost done..."
    $ renpy.pause(0.5,hard=True)
    call updateconsole("DEL basedir+\"/characters/yuuri.chr\"","")
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
    # $ persistent.playthrough = 2
    # $ persistent.autoload = "ch30_main"
    # $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

    # return


label gigachad:
    scene bg club2_act2
    show giga_yuuri at truecenter
    y "Why yes, I did put your pen up my ass"