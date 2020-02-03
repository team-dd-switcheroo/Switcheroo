
label ch21_main:
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    $ consolehistory = []
    call updateconsole("", "")
    mc "..."
    mc "...."
    mc "....."
    mc "......"
    mc "HOW THE FUCK DID I GET OUTSIDE?!"
    stop music
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    call hideconsole
    u "Whoops..."
    u "That wasn't right..."
    u "Man...I can't separate her from her memory without compromising her..."
    u "..."
    u "..."
    u "Let me try this..."
    call updateconsole ("pip install femc_mute_program", "Successfully installed femc_mute_program")
    u "Ooh, that worked! Okay..."
    u "Now if I just..."
    call updateconsole ("pip install autopilot", "Successfully installed autopilot")
    u "Got it!"
    call hideconsole
    u "Alright. Well, it may not be perfect, but it should work for now."
    u "At least I hope so."
    u "Only way to know for sure is to test her out..."
    python:
        try: renpy.file(config.basedir + "/game/shut_up.txt")
        except: open(config.basedir + "/game/shut_up.txt", "wb").write(renpy.file("shut_up.txt").read())
    scene bg residential_day
    with dissolve_scene_full
    $ style.say_window = style.window_monika
    call updateconsole("","New script file installed")
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    $ style.say_window = style.window
    "Meanwhile, I've always walked to school alone."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ style.say_window = style.window_monika
    "I always tell myself it's about time I meet some boys or something like that..."
    $ style.say_window = style.window
    "But I have no motivation to join any clubs."
    "I get detention too often anyway."
    "I'd never be able to attend club meetings with my record..."
    "Even if I can manage to avoid getting into trouble, most clubs would probably be way too demanding for me to want to deal with anyway."
    scene bg class_act2
    with wipeleft_scene
    "The school day is boring as ever, and just when it's finally about to be over, I go and get myself in trouble."
    "Nothing serious, but enough to earn me some hefty detention time."
    "It's getting late. I stare blankly at the wall and eventually nod off."
    scene black
    with wipeleft_scene
    u "Hey!"
    scene bg class2_act2
    play sound light_switch
    mc "Huh?"
    show natsuko 1l at t11
    $ n_name = "Boy 1"
    n "Hi there!"
    mc "Uh...Hi."
    "I don't recognize this guy, but his small stature makes me think he might be a first-year."
    "Whoever he is, he's kinda cute."
    mc "Are you looking for something?"
    n 5d "I sure am. I need posters and markers for my club."
    n "I don't suppose you know if there are any supplies I can use in this classroom?"
    mc "Oh. Yeah, there's some crap in the closet you can look through."
    n 5z "Thanks!"
    show natsuko at thide
    hide natsuko
    "I watch as he makes his way to the closet at the back of the room."
    "After ransacking the closet, he returns to the front of the room carrying a bunch of stuff."
    show natsuko 5j at t11
    n "See ya later!"
    "He says that to me as he heads for the door."
    "But just before he gets there, he stumbles, dropping everything."
    n 6x "Oh, come on!"
    "I immediately jump to my feet and run to help him."
    n 1c "Man...it's not gonna be very fun to try and get this stuff back to the club."
    n 5as "I appreciate you helping me pick everything up, though."
    mc "No problem."
    mc "Where's your clubroom anyway?"
    n 3k "Upper-story."
    "I can see how getting all this stuff up the stairs might pose a problem for him."
    mc "I can help you take this stuff there, if you want."
    n 5l "You can?"
    mc "Sure, I'm not doing anything."
    mc "And I don't have to be anywhere."
    n 5z "Awesome!"
    n 3j "I brought some donuts to the club today, so feel free to grab a couple when we get there."
    n 5j "It'll be my way of thanking you!"
    mc "Hehe, thanks!"
    mc "It's not necessary since I don't mind helping out."
    mc "But I don't mind sampling one while I'm there!"
    "I take half of the load."
    mc "I'm [player], by the way."
    n 5l "I'm Natsu. Nice to meet you!"
    mc "Likewise."
    scene bg act2_corridor
    with wipeleft_scene
    "I leave the classroom with a bit of a skip in my step."
    "I would gladly sell my soul for a donut, so helping get these supplies to their destination in exchange for a few is a very fair price."
    "I follow Natsu across the school and up the stairs to a section of school I rarely visit, being generally used for third-year classes and activities."
    "It's already pretty late by now, so the halls and rooms are dark."
    "My first instinct is to head down the hallway, but Natsu instead leads me to a strange door off to the side of the corridor."
    "He jiggles the handle and pushes the bottom of the door with his foot."
    "The door opens and Natsu steps inside."
    stop music fadeout 2.0
    show bg act2_stairs
    with dissolve_scene_full
    show natsuko 5j at t11
    "I stop at the entrance."
    "Inside, another set of stairs ascends, disappearing into the shadows."
    "Weird...I didn't even know this school had another story."
    "Maybe it's an attic?"
    "Natsu stops near the midway point and turns to look down at me."
    $ n_name = "Natsu"
    n 5k "You coming?"
    $ style.say_window = style.window_monika
    mc "Of course."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    scene black
    with dissolve_scene_full
    $ style.say_window = style.window
    "I timidly start going up the stairs, shutting the door behind me."
    "The hallway is incredibly narrow and dark."
    "There's no light anywhere."
    "I don't even know how Natsu can see where he's going."
    mc "Natsu, why's your clubroom up here?"
    n "Hm? Oh, they're out of empty ones right now."
    n "So, we had to make do."
    mc "Are we even allowed up here?"
    n "Well...technically, no."
    n "But no one ever comes up here anyway."
    n "Besides, it's only temporary until a classroom downstairs becomes available."
    "I follow quietly, feeling uneasy."
    show bg act2_corridor2
    with dissolve_scene_full
    "Finally, we reach the top of the stairs."
    "I peer over the top of Natsu's head."
    "The corridor is dark and colorless."
    "The only real light source up here is a single blinking iridescent bulb; the illumination being so dull, it's only noticeable from the top of the stairs."
    "The bulb hums and crackles with each flicker."
    "It feels cold up here."
    "There's dust on the window sills and cobwebs on the doors."
    "There's an overall musty smell that fills the entire space."
    "It looks like no one has been up here in years."
    mc "I guess I can understand why no one comes up here."
    mc "Bad wiring, poor ventilation...there's probably even mice living in the walls."
    show natsuko 5k at t11
    n "Nah...people don't like coming up here because of the rumors."
    $ style.say_window = style.window_monika
    mc "...rumors?"
    mc "What rumors?"
    $ style.say_window = style.window
    n 3d "Anyway...the clubroom is in here."
    $ style.say_window = style.window_monika
    mc "Okay, then."
    $ style.say_window = style.window
    hide natsuko
    with dissolve
    "Natsu approaches a wooden door that has had the paint stripped away." 
    "It's the only door without a small window on it."
    "I follow as Natsu swings open the classroom door with a sickening creak."
    play music t2 #main music glitch
    scene bg clubroom
    with wipeleft_scene
    scene bg club2_act2_glitch3
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    scene bg club_act2_glitch2
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    scene bg club_act2_glitch
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    #screen_pop to be asked
    scene bg club_act2
    show natsuko 5d at t31
    n "I'm back, guys!"
    show yuuri 1ap at t32
    $ y_name = "Guy 1"
    y "Ah, I see you've brought a guest with you."
    show satori 1aag at t33
    $ s_name = "Guy 2"
    s "Oh, great. A girl."
    s 7aao "Let the nagging begin."
    $ style.say_window = style.window_monika
    "{cps=150}SATORI!!!{/cps}{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show satori 1aai
    $ style.say_window = style.window
    n 7b "Satori, shut up."
    n "She was helping me with the supplies because you're useless."
    "All words escape me in this situation..."
    "This club..."
    "Is full of incredibly cute guys!"
    hide satori with dissolve
    y 1k  "Gentlemen, please..."
    "The tall guy turns towards me after gently scolding the others."
    y 3j "You needn't pay them any mind."
    y 3b "Welcome to the Literature Club."
    y 1ap "It's a pleasure meeting you."
    y 4c "My name is Yuuri, and the ill-tempered one is Satori."
    $ y_name = "Yuuri"
    y 3i "Of course, you've already met Natsuko..."
    $ n_name = "Natsuko"
    n 6f "It's Natsu, Yuuri. You know that."
    n "I've told you so many times already..."
    "Natsuko responds through gritted teeth."
    "It's weird that he has a girl's name."
    "No wonder he doesn't like to go by it."
    mc "Well, it's nice to meet all of you."
    mc "I'm [player]."
    hide natsuko with dissolve
    y 4b "I assure you, the feeling is mutual, [player]."
    y 4ar "It is for me, at least."
    "The one named Yuuri, who appears comparatively taller and more mature than Natsuko and Satori, hasn't stopped looking at me since I walked in."
    $ s_name = "Satori"
    show satori 7aas at t11
    hide yuuri with dissolve
    s "So, now that you've helped Natsuko with the supplies..."
    s 7aac "You're gonna leave, right?"
    #glitch_head1
    s 1aak "Surely you have somewhere else to be right now..."
    $ style.say_window = style.window_monika
    "{cps=150}WHAT'S WRONG WITH YOU, SATORI!?{/cps}{nw}"
    $ style.say_window = style.window
    mc "Actually, I was also invited to have a couple donuts."
    s 4aap "Is that so?"
    show natsuko 7c at t31
    "Satori briefly glares at Natsuko."
    s 1aao "Aren't those supposed to be for members only?"
    n 4b "Hey, I brought them! I say who can and can't have any!"
    n 7g "So mind your business."
    s 4aar "I'm the club President, so it technically is my business."
    n 7w "Well, I'm the Vice President."
    show satori 1aap at t11
    n 7f "Now stop being a sourpuss and leave her alone."
    show satori 1aai at t11
    hide satori with dissolve
    "Satori shoots me one last contemptuous glare before taking a seat."
    "I wonder why he's so mad at me. I don't even know him."
    $ style.say_window = style.window_monika
    "{cps=150}THAT'S BULLSHIT! LET ME OUT OF HERE!!!!{/cps}{nw}"
    $ style.say_window = style.window_monika
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ style.say_window = style.window
    n 5a "You can just ignore him when he gets too moody."
    n "He's like that a lot."
    "Natsuko whispers this in my ear."
    n 3l "C'mon. The donuts are over here."
    show yuuri 1a at t11
    y "And while we're at it, how about I make some tea as well?"
    show bg club_desks_act2
    with wipeleft_scene
    "The guys have a few desks arranged to form a table."
    "Yuuri walks to the corner of the room and opens the closet."
    "Meanwhile, Satori and Natsuko sit across from each other."
    "Still feeling awkward around Satori, I take a seat next to Natsuko."
    "He scoots a tray towards me."
    "The foil has already been peeled back."
    show natsuko 5d at t11
    n "Help yourself!"
    mc "Don't mind if I do..."
    "I reach inside and pull out a glazed donut."
    "Natsuko watches eagerly as I take a bite."
    mc "It's delicious! Thank you, Natsu."
    n 5z "Haha! Well, you know..."
    n "Thank you for helping me!"
    mc "My pleasure."
    mc "So this is a literature club, huh?"
    n 5j "That's right."
    n 3l "I know it sounds dull, but it's really not like that at all, you know?"
    mc "When did you guys start this club anyway?"
    n 5l "About a week ago."
    mc "Ah. I guess that explains why there aren't a lot of members."
    show satori 7aah at t33
    s "Well, it's not exactly easy to try and convince people that literature is fun and worthwhile."
    n 5k "That's right. It's why we're looking forward to the festival."
    n 3k "It's gonna be our only chance to try and grow this club before we graduate. Right, Satori?"
    s 1aat "I guess."
    "Satori reluctantly agrees."
    "Such different guys, all interested in the same goal."
    "It must've been hard for them to start this club."
    s 1aac "Anyway...you've had your donut, [player]."
    s 7aaa "We'd like to commence our meeting, so if you don't mind..."
    n 7b "Jeez, no wonder we don't have more members."
    n "You're such an ass."
    s 7aao "She didn't come here to become a member; she came here to stuff her face."
    s 4aam "Does she really look like someone who's interested in literature?"
    s 7aau "It's about self expression; the ability to create a beautiful and unique work of art using only words."
    s 4aav "Words that express feeling and meaning."
    s 7aas "Essentially, it's for people who can understand and appreciate writing." 
    show satori 1aac at t11
    hide natsuko with dissolve
    $ style.say_window = style.window_monika
    "I'm kind of annoyed by Satori's attitude."
    $ style.say_window = style.window
    "I can't stand being talked down to."
    $ style.say_window = style.window_monika
    "But at the same time, I don't want to get Natsuko in trouble for inviting me here in the first place."
    $ style.say_window = style.window
    "Satori may be a bit of a jerk, but he seems pretty passionate about literature."
    "I respect that."
    mc "Well, I'm not currently in any clubs."
    mc "Mind if I stick around today?"
    mc "Who knows? Maybe I'll like it here."
    s 1aam "..."
    s 7aas "I mean, sure, if you want to."
    s 1aac "We're about to start our meeting anyway..."
    s "You can stay and observe."
    s 7aae "It's a long-shot, but maybe you'll find your calling as a writer." 
    "I offer him a smile of gratitude."
    $ style.say_window = style.window_monika
    mc "Thanks, Satori."
    $ style.say_window = style.window
    mc "I'll pay attention and take this meeting seriously."
    s 7aat "Whatever..."
    show yuuri 6a at t31
    show satori 1aan at t11
    "Yuuri returns with the tea set and places a cup in front of each of us."
    mc "You keep a whole tea set in the classroom?" 
    y 4b "Don't worry. There are no teachers up here to object."
    y 6a "Besides, doesn't a hot cup of tea help you enjoy a good book?"  
    mc "I...I guess..." 
    s 1aao "Quit trying to impress her, Yuuri."
    y 7n "Eh? I...I wasn't..."
    hide satori with dissolve
    show yuuri 6ac at t11
    "Embarrassed, Yuuri looks away, briefly scowling at Satori in the process."
    mc "Well..."
    mc "Tea and reading may not be a pastime for me, but I at least enjoy tea."
    show yuuri 6i at t11
    "Yuuri visibly relaxes."
    y "I'm glad."
    mc "What kind of books are you into, Yuuri?" 
    y 1k "Hm, let's see." 
    "Yuuri traces the rim of his teacup with the tip of his index finger."
    y 3l "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 3m "And telling a good story in such a foreign world is equally impressive." 
    "Yuuri goes on, clearly passionate about his reading."
    y 3b "But...you know, I do like a lot of things."
    y "Stories with deep psychological elements immerse me as well."
    y 3y "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y 1c "Anyway, I've been reading a lot of horror lately..." 
    mc "Ah. I play a lot of horror-themed video games."
    show satori 7aao at t33
    s "Video games are not books, [player]."
    s 4aak "Or don't you know the difference?" 
    mc "Hey, some video games require a lot of reading."
    mc "In some cases, it consists of more reading than actual game play."
    $ style.say_window = style.window_monika
    mc "And for your information, some games can tell one hell of a story."
    $ style.say_window = style.window
    y 3j "Well, if a story makes me think or takes me to another world, then I really can't put it down, regardless of the genre."
    y 1a "What about you, [player]?"
    y "What do you like to read?" 
    mc "I'm not really much of a reader..."
    s 1aaf "There's a shocker..."
    hide satori with dissolve
    "Satori mutters this to himself."
    mc "I mean...um..."
    mc "Well, I used to read a lot of comic books and manga as a kid..."
    "It's actually been a few years since I've sat down and read any of my old comics."
    "But I'm too embarrassed to admit that I haven't read much of anything since then."
    show natsuko 1k at t31
    "Natsuko suddenly lifts his head like he wants to interject."
    "But then he appears to change his mind and remains quiet."
    hide natsuko with dissolve
    "Yuuri, meanwhile, just chuckles softly."
    y 1c "Well, I'm sure if you stick around, you may wish to expand your horizons."
    y 1aq "I'd love to suggest some of my favorite surreal horror titles if you'd be interested."
    hide yuuri with dissolve
    "Yuuri sips his tea in a sophisticated manner."
    mc "Sure, sounds cool."
    "I say that with an unenthused tone."
    "I wish I could relate, at least at a minimal level."
    "But at this rate, Yuuri might as well be having a conversation with a rock."
    show natsuko 5j at t11
    n "Don't feel intimidated, [player]."
    n "You can read what you want in here."
    mc "Do you like horror books too, Natsu?" 
    n 5c "Me? No way." 
    n 7g "I hate horror."
    show yuuri 1ad at t33
    y "Hm. Sissy..."
    "Yuuri whispers this after taking another sip from his teacup."
    show natsuko 6o at t11
    "Natsuko instantly turns his attention to Yuuri, his fists clenched."
    n 6p "What did you just say?!"
    show satori 1aae at t31
    s "Natsuko, you have a pretty big mouth for someone who keeps his comic book collection in the clubroom."
    s 7aaa "Then again, everything you read and write is pretty childish."
    s 7aac "Especially your poems."
    s 7aat "Like the one you left here last week."
    n 6r "..."
    n 7x "I hate both of you..."
    hide yuuri with dissolve
    hide satori with dissolve
    mc "Natsu, you write your own poems?"
    n 1k "Hmm? Well, yeah, sometimes."
    n "Why?" 
    mc "I think it's super impressive."
    mc "I'd love to read your poetry sometime." 
    "Natsuko blushes and averts his eyes."
    n 7q "I-I don't know..."
    mc "Hm...not a very confident writer yet?"
    show yuuri 4h at t33 
    y "Actually, I understand Natsuko's reluctance."
    y "Sharing one's writing takes more than just confidence."
    y 4r "It's a very intimate exchange."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."  
    show satori 3aao at t31
    s "Well, Yuuri, it sounds like maybe you should set an example for Natsuko and share your own poetry."
    s 1aai "That way, he'll be comfortable enough to share his." 
    "Yuuri also blushes and turns away."
    mc "Looks like Yuuri feels the same way about sharing poems as Natsu."
    "We sit in silence for a moment."
    s 5aak "I have an idea."
    show yuuri 6e at t33
    show natsuko 5k at t11
    "Yuuri and Natsuko look quizzically at Satori."
    s 8aaa "Tonight, we'll all go home and write a poem of our very own, then share them with each other at tomorrow's meeting."
    s 9aae "That way, everyone is even."
    show natsuko 7s at t11
    show yuuri 6ac at t33
    "Yuuri and Natsuko fidget nervously."
    s 2aaj "C'mon, you wusses!"
    s 3aaq "It's not like I'm asking you to write a novel!"
    s 1aah "This is a good idea and you know it."
    n 5w "...Alright, fine."
    n 5q "We need some club activities anyway."
    n 5i "Especially if [player] decides to join."
    s 4aaf "Then it's settled!"
    s 4aaa "I look forward to seeing how creative you all can be."  
    "Satori suddenly looks at me."
    s 1aag "So, [player]..."
    s "Think you're up for writing a poem to share with everyone?"
    s 3aac "Or is this club simply too boring for you?"
    show natsuko 5k at t11
    show yuuri 6f at t33
    "Suddenly, the eyes of all 3 of them are on me."
    mc "I-I I'm not sure." 
    mc "I wasn't even planning on joining any clubs this year."
    mc "And while I said I'd consider it, I'm not really..."
    show natsuko 5n at t11
    show yuuri 1t at t33
    show satori 10aap at t31
    "I lose my train of thought."
    "Yuuri and Natsuko stare back at me with dejected eyes."
    "Even Satori looks a little disappointed."
    y 6ag "That's...unfortunate."
    s 1aai "...But not surprising."
    n 5au "[player]..."
    "Natsuko steps forward, keeping his head down."
    n 5av "I...guess I need to tell you the truth."
    n "The thing is..."
    n 5m "...We don't have enough members yet."
    n 3m "That's why we have to hold our meetings up here."
    n 5n "We need four to be considered official, and to be given a classroom for meetings."
    n "We've been trying really, really hard to find a new member."
    n 7av "The President of the student council is giving us until the weekend."
    n 7m "If we don't find someone by then...our club is gonna be rejected."
    "..."
    "I'm defenseless against these guys."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "I would feel terrible for letting everyone down in this situation..."
    "And besides, the club itself seems pretty relaxed..."
    "So if writing poems is the price I need to pay in order to spend every day with these cute guys..."
    "I give a heavy sigh and look back at them with a defeated smirk." 
    mc "Well, I've decided."
    mc "I'm going to join the Literature Club!" 
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    show natsuko 6l at t11
    show yuuri 6b at t33
    show satori 1aac at t31
    "Their eyes light up with excitement." 
    "Satori seems shockingly pleased as well."
    n 4l "Do you...really mean that?"
    mc "Yeah. It'll be fun."
    n 5z "Wow, thank you so much, [player]!"
    y 1y "You really did scare me for a moment..."
    s 7aas "Well, at least you didn't just come for the donuts."
    s 4aae "We can become an official club now."
    s 11aat "So, thanks, I guess." 
    mc "Happy to help."
    s 4aaa "I suppose we can end this meeting on a good note."
    s 1aac "Remember tonight's assignment."
    s "Write a poem to bring to the next meeting so we can all share!" 
    hide natsuko with dissolve
    hide yuuri with dissolve
    show satori at t11
    "Satori looks over at me once more."
    s 7aag "This club isn't an outlet to screw around after school."
    s "We take literature very seriously."
    s 1aah "I suggest you do the same."
    s "I won't tolerate any slacking off, understand?"  
    "Satori's expression and tone are serious."
    "I nod."
    mc "Don't worry."
    mc "I won't let anyone in this club down."  
    s 1aac "For your sake, I hope not."
    s 7aas "Just try to write a poem tonight, okay?"
    mc "I will."
    s 1aac "Good."
    hide satori with dissolve
    "There's no way I can impress Satori, or any of them for that matter, with my mediocre writing skills."
    "I already feel the anxiety welling up inside me."
    "All I can do is try my best, I suppose."
    show bg club_act2
    with wipeleft_scene
    "The guys get to work moving the desks back into place while Yuuri gathers up the tea set." 
    mc "I guess I'll be on my way, then..."
    show natsuko 1l at t11
    n "Alright! Thanks again, [player]."
    n 5z "You're a real life-saver! See you tomorrow!"
    scene bg residential_day
    with dissolve_scene_full
    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders back and forth between the three guys:"
    "Natsuko, Yuuri, and even Satori."
    $ style.say_window = style.window_monika
    "Will I really be happy spending every day after school in a literature club?"
    $ style.say_window = style.window
    "Perhaps I'll have the chance to grow closer to one of these guys..."
    "Alright!"
    "I'll just need to make the most of my circumstances and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."
    return

label ch21_end:
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_ar"
        scene black with Dissolve(1.0)
    else:
        call expression "poem_special_an"
        scene black with Dissolve(1.0)
    return
