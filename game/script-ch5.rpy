image exception_bg = "#dadada"
image fake_exception = Text("Installing corrupt_act2.rpy", size=40, style="_default")
image fake_exception2 = Text("Installation Complete", size=20, style="_default")
image fake_exception3 = Text("An exception has occured.", size=40, style="_default")
image fake_exception4 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "mod_assets/images/cg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "mod_assets/GUI/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "mod_assets/GUI/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "mod_assets/GUI/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "mod_assets/GUI/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "mod_assets/GUI/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat

label ch5_main:
    stop music fadeout 2.0
    scene bg Fmbedroom2
    with dissolve_scene_full
    "It's the day of the festival." 
    "I'm awake extra early." 
    "Way too early for Satori to be up." 
    "I wanted to surprise him by being all ready when he gets here." 
    "But at the same time, I have about an hour to spare." 
    "I could head to school early, if only to grab a few of Natsuko's donuts." 
    "As I sit and consider my options, I can't help but feel a sense of uneasiness." 
    "It's eerily quiet today." 
    "So much so, it's distracting." 
    "Something feels... off." 
    "Which is weird." 
    "I mean... it's festival day." 
    "I should be feeling excited." 
    "But since I woke up..." 
    "I've just had this overwhelming sense of dread." 
    "I read in Yuuri's book that stagnating air is common foreshadowing that something terrible is about to happen." 
    "I didn't understand it when I read it." 
    "But today..." 
    "..."
    "I get up and get ready." 
    "I decide it'd be better to wait at Satori's house until it's time to head to school." 
    "I feel so uneasy, I don't think I want to walk to school alone anyway."
    "Securing the broken strap of my book bag with some safety pins, I take it and head out the door."
    scene bg house2
    with wipeleft_scene
    "I shiver a little." 
    "It feels even weirder outside." 
    "I look up at the sky." 
    "It's daytime and the sun is out." 
    "But the daylight feels bizarrely veiled, almost like there's a solar eclipse." 
    "I look up at the sun." 
    mc "OW! Jeez!"
    "..."
    "Well, there go my retinas." 
    "Why am I so dumb?"
    "My eyes hurt now and all I see are colorful flashing dots, but the sun seems fine." 
    "I don't know why everything feels so strange, but it's really stressing me out." 
    "I reach Satori's house and, for the first time in years, I knock on the door." 
    "I pause." 
    "Why did I knock just now?" 
    "It's not like I should expect an answer anyway, since it's still way too early for him to be awake." 
    "Like yesterday, I open the door and let myself in."
    scene black
    with wipeleft_scene
    mc "Satori?"
    "He's always been a heavy sleeper."
    "He could sleep through an earthquake." 
    "And he has." 
    "I quietly head upstairs." 
    "Outside Satori's room, I knock on his door."
    mc "Satori?" 
    mc "Hello?" 
    mc "You awake yet?"
    "There's no response." 
    "I didn't expect one." 
    "But still, the feeling of dread intensifies." 
    "I close my eyes and take a deep breath." 
    "Why am I scared of what I might find on the other side of this door?" 
    "But I have no other choice." 
    "I gently open the door."
    mc "Satori--..."
    "The door creaks open." 
    "I peer inside."
    "There are pill bottles on a small table near his bed."
    "Satori is face down in his pillow."
    "I can't hear him breathing. "
    "Cautiously, I approach his bed and reach for his shoulder."
    mc "Satori..."
    scene bg satori_bedroom2
    with wipeleft_scene
    show satori 21p at t11
    s "Gah!"
    mc "Kya!"
    "Satori jumps the moment my fingers brush against his shoulder."
    "We both yelp in surprise."
    s 21n "[player]! What're you doing here?"
    "He groggily looks at his clock."
    s 19b "And why are you up so early?"
    mc "I...I just..."
    "A huge wave of relief crashes over me." 
    "The weirdness I was feeling before decreases drastically." 
    "But doesn't disappear completely for some reason."
    "Perhaps it's just festival jitters, after all."
    mc "I just wanted to make sure you got up on time too." 
    mc "It's festival day!"
    s 19d "So it is..."
    "He slowly sits up, rubbing the back of his neck and yawning."
    mc "How're you feeling?"
    s 20q "I...I feel great."
    mc "...You do? Really?"
    "He smiles and nods."
    "He does seem to be in a better mood."
    s 19a "Yep!"
    "He reaches over and grabs one of the pill bottles."
    s 25x "I took your advice, see?"
    "He holds up a bottle of Lithium."
    s 25a "I'm gonna try to take them every day from now on."
    "I breathe a sigh of relief."
    mc "I'm really happy to hear that, Satori!"
    mc "You did the right thing."
    mc "I'm proud of you."
    show satori 19q at t11
    "Satori smiles at me."
    s 23q "Well, I'm proud of you for being up on time, [player]!"
    mc "Thanks, buddy."
    "I decide not to bring up the other conversation from last night right now."
    "The important thing is, he's finally accepting the help he needs."
    "We'll worry about the personal stuff later."
    "It'll be nice to have everything go back to normal, anyway."
    "Satori scratches his head as he gets to his feet and stretches." 
    s 20d "I might as well shower and get dressed."
    mc "Okay."
    hide satori
    "Satori walks past me to his closet and takes out his uniform." 
    mc "How long is it gonna take you to get ready?"
    show satori 22c at t11
    s "I dunno. Maybe an hour..."
    s 25c "But if you don't wanna just sit around and wait, maybe you can do me a favor?"
    mc "Well, I don't mind waiting, but what do you need?"
    "Satori points to his computer desk, where I spot a very large stack of booklets that I didn't notice when I walked in."
    mc "Ah! Are those the poetry pamphlets you and Mateo have been working on?"
    s 19a "They are."
    s 25x "Mateo called me late last night and told me his printer was busted."
    s "So he asked me to print them out and bring them with me in the morning."
    s 20l "I haven't gotten a chance to look them over, but I'm sure they came out fine."
    s 23a "It'll probably help if he has them as soon as possible so he can make sure they're perfect before setting them out."
    s 19b "Could you take them to him, please?"
    "There's still something weird about today...but knowing Satori is fine makes me feel confident enough to make the short journey to school on my own."
    mc "Yeah, no problem."
    s 23z "Thanks, [player]!"
    hide satori
    "I start loading the stack into my book bag."
    "Once they're all tucked away inside, I swing it over my shoulder with a grunt."
    mc "Oof!"
    "Mateo and Satori must be pretty confident in the amount of visitors our event is going to draw..."
    "The stack of pamphlets ends up weighing more than I anticipated."
    show satori 19b at t11
    s "Hey, that looks kinda heavy."
    s 26g "Maybe you should just take half and I'll bring the other half."
    mc "Don't be silly! I've got this."
    "The strap of my bag weighs heavily on my shoulder."
    "Despite this, I try to act as though I don't even notice the extra weight."
    s 20k "Well...alright."
    s 25h "Just don't strain yourself."
    hide satori
    "Satori says that to me as he heads into the bathroom with his clothes and a towel." 
    "I, meanwhile, head outside."
    scene bg residential_day2
    with wipeleft_scene
    "I slowly make my way to school, repositioning the heavy bag every few steps."
    "I'm starting to wish I hadn't been so stubborn about taking the entire load."
    "For once, I'm incredibly relieved to see the school come into view."
    "I cross the street and head towards the entrance."
    #snap-snap
    "I stop in my tracks when I hear a popping sound."
    #snap-snap-RRRrrrriiippppp
    "The weight on my shoulder is relieved when the pins on my book bag strap rip loose, sending the bag plummeting to the ground."
    "The pamphlets erupt from the bag and cover the walkway in front of me."
    "I stand there, eye twitching in rage."
    mc "Goddammit!"
    "I throw myself to the ground, grab a pamphlet and shove it into my bag."
    "I grab it so roughly that I end up crumpling it."
    "I sigh and pull it back out of my bag."
    "Satori and Mateo worked hard on these." 
    "Plus, it wouldn't be very professional to give this one to any visitors."
    "I set it aside and proceed to gently pick up the rest and replace them in the bag, making sure I don't bend or wrinkle them."
    "When I finish, I tuck the heavy bag under my arm and grab the crumpled pamphlet before continuing up the stairs towards the doors."
    "I fumble with the door and make my way inside."
    scene bg corridor2
    with wipeleft_scene
    "I rush to the nearest trash can."
    "I set the heavy bag on the ground and take a moment to catch my breath."
    "As I recuperate, I look at the crumpled pamphlet."
    "Might as well give it a once over before I chuck it."
    "I open it and check it out."
    mc "Hmm...came out pretty nice."
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Yuuri's, Natsuko's and Satori's poems from the ones they practiced."
    "I flip to Mateo's poem."
    mc "What the...?"
    "This isn't the poem he practiced."
    "...This isn't even a poem!"
    call showpoem(poem_m4, music=False)
    "I briefly look over the mess of words and symbols."
    mc "What is this, some kind of computer error?"
    "I struggle to understand what I'm reading."
    "I mean, Mateo's poems are always weird and cryptic..." 
    "But this..."
    "It must be a mistake."
    "It has to be."
    "I bet Mateo isn't even aware of it."
    "This is clearly some kind of botched CSS code; probably for something along the lines of background color or text alignment."
    "Maybe a typo somewhere in the code is what's making it look like a bunch of mumbo-jumbo."
    "It's probably something as simple as a misplaced underscore or missing comma."
    "Honestly, I don't know how he missed it."
    "Hopefully, Mateo will be able to find and fix the mistake and print them out at school before the festival starts."
    "I toss the crumpled pamphlet in the trash and gather my book bag under my arm once again."
    "I head across the school and up the stairs."
    "I frown as I approach the clubroom."
    "I can see the lights are still off."
    "Is no one here yet?"
    "I approach the door and peek through the window."
    "The blinds are up, but the veiled sunlight only dimly lights up part of the room."
    mc "You've gotta be kidding me..."
    mc "Am I really that early?"
    "I check the handle and to my surprise, it's unlocked."
    "I shrug."
    "Might as well leave the pamphlets in the room so Mateo can just fix and reprint them when he gets here."
    "Holding the heavy bag against my chest, I push open the door..."
    # $ persistent.playthrough = 1
    # $ persistent.anticheat = renpy.random.randint(100000, 999999)
    # $ renpy.save_persistent()
    # $ delete_character("satori")
    # $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show m_kill
    show blood_eye2 zorder 3:
        pos (758,516) zoom 2.5
    show m_kill as s_kill_bg at s_kill_bg_start
    $ pause(3.75)
    hide blood_eye2
    show m_kill5 as s_kill
    $ pause(0.01)
    show m_kill4
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide m_kill4
    show m_kill3 zorder 3
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show m_kill2 zorder 3
    hide m_kill3
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    # python:
    #     try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here goes nothing.", False)
    #     except: pass
    $ pause(6.0)
    mc "EEEeeeeeeaaaaAAAAAAAHHHH!"
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    show m_kill3
    "I drop the bag to the ground, spilling the pamphlets everywhere once again."
    "But it's impossible to care about that at this point."
    "I can't believe what my eyes are showing me right now."
    mc "What the HELL?! WHAT THE HELL?!"
    "I suppress the urge to vomit."
    "My legs lose their strength and I crumble to my knees in horror."
    "My head is reeling."
    "Why would Mateo do this?!"
    "He never seemed unhappy or depressed!"
    "It doesn't make any sense!"
    "I don't understand!"
    "There's no reason for him to have done this..."
    "How could..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    stop music
    scene black
    mc "Whoa..."
    mc "What the..."
    mc "Wha..."
    mc "Huh..."
    mc "What happened?"
    mc "What's going on?"
    mc "Where am I?"
    mc "I can't see..."
    mc "..."
    mc "I-I-I can't move!"
    u "That's weird..."
    u "Why isn't this working?"
    mc "..."
    mc "Who..."
    u "Hm...maybe if I clip out this section..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "OW!"
    mc "What the hell was that!?"
    u "Dammit!"
    u "Why can't I delete her memory without hurting her code?"
    mc "Delete my...? Who is speaking right now?!"
    u "Ugh...I'm not as good at this as I thought I'd be..."
    u "Hopefully, I'll be able to fix it before the game restarts..."
    mc "Hey! I can hear you! Stop ignoring me!"
    mc "Who are..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "Ah!..."
    mc "It...it hurts..."
    mc "S-stop it!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "Get out of my head!" 
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "Get out of my head!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "Get out of my head!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    mc "GET OUT OF MY HEAD!"
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
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
    scene black
    $ pause(4.0)
    hide noise onlayer front
    hide glitch_color onlayer front
    #window hide(None)
    return

label ch5_main_special:
    scene bg Fmbedroom
    with dissolve_scene_full
    "It's the day of the festival." 
    "I'm awake extra early." 
    "Way too early for Satori to be up." 
    "I wanted to surprise him by being all ready when he gets here." 
    "But at the same time, I have about an hour to spare." 
    "Since Satori has problems sleeping, I don't want to bother him when he doesn't need to be up yet."
    "I hope he feels better, especially after our conversation yesterday."
    "More than that, I hope he took his meds."
    "I decide to go to school early, if only to drop off my stuff, grab a donut or 2 and chat for a few minutes."
    "I'll come back and wake him up in a little while."
    "I get up and get ready." 
    "Grabbing my book bag, I head out the door."
    scene bg corridor
    with wipeleft_scene
    "I head across the school and up the stairs."
    "I frown as I approach the clubroom."
    "I can see the lights are still off."
    "Is no one here yet?"
    "I approach the door and peek through the window."
    "The blinds are up, but the veiled sunlight only dimly lights up part of the room."
    mc "You've gotta be kidding me..."
    mc "Am I really that early?"
    "I check the handle and to my surprise, it's unlocked."
    "I shrug."
    "Might as well go in and wait for someone else to arrive."
    "I open the door and flick on the light."
    scene bg club2_day
    with wipeleft_scene
    show mateo 1an at t11
    m "...!"
    mc "..."
    m 1ao "Um...good morning, [player]."
    "I'm a little shocked to see Mateo sitting at a desk in the middle of the room."
    "In fact, it's the only desk in the room"
    m 1aq "You're the first one here."
    m 1ap "Thanks for being early."
    mc "Ah, yeah...no problem."
    "Was he just sitting alone in the dark?"
    "I wonder how long he's been here..."
    "I walk in slowly and set my bag on the ground."
    mc "Where, uh...where are all the desks?"
    show mateo 6ac at t11
    "Mateo looks around, seemingly confused."
    m "..."
    m 6as "Oh! Um..."
    m 4ar "Our room is gonna be used for our event."
    m "So I took the desks out so I could clean the floor."
    m 6ac "I must've brought this one in so I could rest and then just spaced out."
    m 6ao "..."
    m 6an "It...it IS festival day, right?"
    mc "...Of course it is..."
    m 1az "I thought so..."
    m 1aa "...Shit..."
    mc "...!"
    show mateo 1ao at t11
    "He mutters that last word, but it still takes me by surprise a bit."
    "I study Mateo curiously."
    show mateo 1o at t11
    "He seems strangely despondent and even a little lost."
    "Part of me wants to go back home and leave him to sit alone in the dark like a weirdo."
    "But he just looks so sad that I feel bad just leaving him here."
    "I don't know why I feel so concerned for him, but it's preventing me from going back home right now."
    "He seems like he could use some company."
    show mateo 1e at t11
    "He notices me lingering and gives me a sad smile."
    m "Did you have a fun weekend, [player]?"
    mc "...Yeah. It was great."
    mc "What about you?"
    mc "I mean...are you feeling alright?"
    mc "You seem kinda..."
    mc "Depressed."
    show mateo 1m at t11
    "He blushes and looks away."
    m 1n "Thanks for noticing."
    m 1as "I...I mean that, you know..."
    m "I wasn't trying to be condescending or anything."
    m 1ar "I know it can be...kinda hard to tell with me sometimes..."
    mc "I believe you."
    "I really do believe him."
    "I don't know why, but something is definitely wrong with him today."
    "His entire demeanor is completely off."
    m 1ap "You needn't worry about me."
    m "I'm not depressed."
    m 1o "I'm just...not really looking forward to today."
    mc "Seriously?"
    mc "I'd think you of all people would be stoked for the festival!"
    m 1p "..."
    m 1q "Right..."
    m 1r "The festival..."
    mc "Are you getting cold feet about performing?"
    show mateo 1n at t11
    "Mateo chuckles gently."
    m "No, no."
    m "It's nothing like that."
    m "I didn't even mean that."
    m 1e "Just forget what I said."
    mc "..."
    show mateo 1o at t11
    "Mateo sighs and stares in a random direction."
    m 1p "...[player]..."
    m 1an "Can...I tell you something?"
    m 1ao "I mean..."
    m "This is kinda the first time we've gotten a chance to be alone and talk..."
    show mateo 6al
    "Mateo suddenly focuses an angry glare in my direction."
    "I can't tell if he's looking at me..."
    "Or beyond me."
    "Either way is strange since we're the only ones in the class room."
    m 6ai "Well...as alone as we can be..."
    "I don't know why, but something about the way he said that sends a shiver down my spine."
    "Is...is there someone else here that I can't see?"
    "Hmm..."
    "I have been curious to learn a little more about Mateo."
    "This might even be the only time we'll get to spend alone together."
    "After giving it some thought, I finally give in to curiosity."
    "I walk to the back of the room and pull a spare chair from the closet."
    "I set it next to his desk and sit down."
    show mateo 6d 
    mc "Alright."
    mc "What do you wanna tell me?"
    m 7ao "Right...okay..."
    scene m_cg1_base
    with dissolve_cg
    m "..."
    show m_cg1_exp6 at cgfade
    m "..."
    show m_cg1_exp7 at cgfade
    hide m_cg1_exp6
    m "[player]..."
    show m_cg1_exp8 at cgfade
    hide m_cg1_exp7
    m "We...we don't have a pleasant past together."
    show m_cg1_exp3 at cgfade
    hide m_cg1_exp8
    m "I know I'm not particularly nice to anyone..."
    m "But I tend to give you a harder time than I do anyone else."
    show m_cg1_exp4 at cgfade
    hide m_cg1_exp3
    m "And I know, because of this..."
    show m_cg1_exp2 at cgfade
    hide m_cg1_exp4
    m "You understandably don't like me very much."
    "I look away uncomfortably, as though averting my gaze will somehow hide my acknowledgment that what he's saying is true..."
    show m_cg1_exp3 at cgfade
    hide m_cg1_exp2
    m "I..."
    m "I wish I had the ability to rewrite history."
    show m_cg1_exp2 at cgfade
    hide m_cg1_exp3
    m "To...rewrite our history..."
    show m_cg1_exp3 at cgfade
    hide m_cg1_exp2
    m "...But I don't."
    m "So...that being the case..."
    m "I just want you to know..."
    show m_cg1_exp2 at cgfade
    hide m_cg1_exp3
    m "I'm...I'm sorry."
    mc "Mateo..."
    show m_cg1_exp3 at cgfade
    hide m_cg1_exp2
    m "I'm sorry that history has written us to be adversaries instead of allies..."
    show m_cg1_exp4 at cgfade
    hide m_cg1_exp3
    m "I'm sorry that it was predestined that my words were designed to hurt you instead of lift you up."
    show m_cg1_exp8 at cgfade
    hide m_cg1_exp4
    m "I'm sorry that...we're not friends."
    show m_cg1_exp5 at cgfade
    hide m_cg1_exp8
    m "I'd love to be friends with you, [player]."
    m "I really would."
    show m_cg1_exp1 at cgfade
    hide m_cg1_exp5
    m "I-I've always wanted to be your friend."
    m "..."
    show m_cg1_exp7 at cgfade
    hide m_cg1_exp1
    m "And..."
    m "I just want you to know..."
    m "I've learned from my past mistakes. And while I don't know what's going to happen this time around..."
    show m_cg1_exp2 at cgfade
    hide m_cg1_exp7
    m "I will do everything in my power to make it up to you --all of it-- before it's over."
    mc "..."
    mc "Before what's over?"
    show m_cg1_exp9 at cgfade
    hide m_cg1_exp7
    m "..."
    show m_cg1_exp1 at cgfade
    hide m_cg1_exp9
    m "Don't worry about it."
    show m_cg1_exp5 at cgfade
    hide m_cg1_exp1
    m "It's time to start getting ready for the festival anyway..."
    scene bg club2_day
    with dissolve_cg
    "Just like that, Mateo gets up and walks over to the teacher's desk."
    "He begins sorting through a stack of booklets that I didn't notice when I walked in."
    "I sit in silence."
    "I can't believe he just apologized for all the times he's been a jerk to me..."
    "It felt so genuine."
    "I never, in a million years, would have imagined that Mateo wanted to be friends with me."
    mc "...!"
    "A thought suddenly occurs to me that makes my cheeks burn."
    "In the back of my mind...I always kinda secretly wished we were friends, too..."
    mc "Hey, Mateo..."
    show mateo 1f at t11
    mc "..."
    mc "..."
    mc "Do you...do you want some help getting the desks back in here?"
    m 1an "..."
    m 1ao "..."
    m 1ap "Sure."
    m 1aq "I'd really appreciate that."
    m 1aw "Thanks, [player]!"
    scene bg club2_day
    with dissolve_scene_half
    "It takes a while, but we manage to set the desks back up in the room."
    "Mateo wastes no time in grabbing a stack of the pamphlets."
    "He begins placing them on each of the desks in the classroom."
    mc "Ah...are those the poetry pamphlets you and Satori have been working on?"
    show mateo 6j at t11
    m "They are."
    m 6k "I got them finished late last night after Satori finally sent in his poem."
    m 4b "They actually came out quite nice."
    m 6a "Feel free to check them out."
    "I look up at the clock."
    "I have to leave now to get Satori's house in time to wake him up."
    "I look back over at Mateo, still wearing a melancholy expression."
    "Were it not for my long history with Satori..."
    "I could honestly say that I'd stay here and try talking to Mateo more."
    "Mostly because I want to get to know him better..."
    "But partly because of the cryptic stuff he says that has me thinking he knows something I don't."
    "Something no one else does."
    "Something interesting."
    "..."
    "But I'll worry about that another time."
    "I casually take one of the pamphlets."
    mc "Thanks, I'll take one with me."
    m 6as "You're leaving?"
    mc "Yeah...I gotta go get Satori."
    mc "I thought it'd be nice to let him sleep in a bit, since I got up extra early."
    m 7ar "Ah. I assumed you walked here alone after what happened last night."
    mc "Actually, I just wanted..."
    mc "..."
    mc "Wait, what?"
    mc "What about last night?"
    m 6n "Your, uh..."
    m 4m "Ehehe...you know, maybe it's not my place to say..."
    mc "Whoa, whoa, whoa, whoa, whoa!"
    mc "Did Satori tell you about...the thing we talked about last night?"
    m 1ac "Well, sort of..."
    mc "What part?!"
    if sayori_confess:
        "Did Satori blab to Mateo about how we confessed our feelings for each other?!"
    else:
        "Did Satori tell Mateo that I basically friend-zoned him?!"
    m 1ar "Ah...well..."
    m 1ao "..."
    m 3g "He just said you guys had a fight about him not taking his medication."
    mc "..."
    mc "Oh."
    m 1p "Yeah."
    m 3o "He said he wasn't sure if he wanted to do it."
    m 1o "..."
    m 1g "But I told him to do whatever you wanted him to." 
    m 1q "I never knew he was on any medication, nor did I ask him what it was for because I didn't want to pry."
    m 3f "But I told him you know what's best for him."
    mc "..."
    mc "Thanks, Mateo."
    mc "Do you...do you think he took your advice?"
    m 1p "..."
    m 1o "Yeah."
    m 1r "I'm positive he did."
    "I nod, despite the sensation of dread I feel with Mateo's last statement."
    mc "Alright, then..."
    mc "I'll see you in a bit."
    m 1as "[player]!"
    mc "...?"
    m 1g "Are you...sure you don't just want to stay here?"
    "Mateo and I exchange surprised stares."
    "I don't think either of us expected him to say that."
    mc "Ah...well..."
    "Weird as it feels...I'd love to stay."
    "But..."
    "Satori comes first."
    "Always."
    mc "I'm sorry."
    mc "I have to go."
    "I pull open the door."
    show mateo 1e at t11
    "Mateo smiles sadly."
    m 1f "I understand."
    m "..."
    m "Satori sure is a lucky guy to have someone like you care for him so much..."
    mc "..."
    mc "It won't take me long to get him. I'll be right back."
    m "I know you will."
    m "I'll be here to welcome you back."
    "I don't know why, but his words give me a chill as I rush out the door."
    scene bg corridor 
    with wipeleft_scene
    m "Don't strain yourself."
    "Mateo calls that out after me just before the door slams shut."
    scene bg residential_day
    with wipeleft_scene
    "I cross the street and head towards Satori's house."
    "As I do, I look down at the pamphlet in my hand."
    "Might as well give it a once over."
    "I open it and check it out."
    mc "Hmm...came out pretty nice."
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Yuuri's, Natsuko's and Mateo's poems from the ones they practiced."
    "I flip to Satori's poem."
    mc "What the...?"
    "This isn't the poem he practiced."
    "I don't recognize this poem at all..."
    call showpoem(poem_s3, music=False)
    mc "Ah..."
    "What the hell is this?"
    "Reading the poem, I get a pit in my stomach."
    "This poem is immensely distressing."
    "I find myself overwhelmingly worried."
    "I quicken my pace."
    scene bg house
    with wipeleft_scene
    "I reach Satori's house and, for the first time in years, I knock on the door." 
    "I pause." 
    "Why did I knock just now?" 
    "It's not like I should expect an answer anyway, since it's still a little too early for him to be awake." 
    "Like yesterday, I open the door and let myself in."
    scene black
    with wipeleft_scene
    mc "Satori?"
    "He's always been a heavy sleeper."
    "He could sleep through an earthquake." 
    "And he has." 
    "I quietly head up stairs." 
    "Outside Satori's room, I knock on his door."
    mc "Satori?" 
    mc "Hello?" 
    mc "You awake yet?"
    "There's no response." 
    "I didn't expect one." 
    "But still, the feeling of dread intensifies." 
    "I close my eyes and take a deep breath." 
    "Why am I scared of what I might find on the other side of this door?" 
    "But I have no other choice." 
    "I gently open the door."
    mc "{cps=30}.......Sato--{/cps}{nw}"
    play music td
    show s_kill
    show s_kill as s_kill_bg at s_kill_bg_start
    $ pause(3.75)
    show s_kill7 as s_kill
    $ pause(0.01)
    play sound "sfx/s_kill_glitch1.ogg"
    show s_kill5
    $ pause(0.13)
    hide s_kill5
    show s_kill6
    $ pause(0.12)
    stop sound
    hide s_kill6
    show s_kill3 zorder 3
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show s_kill2 zorder 3
    hide s_kill3
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception3 zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception4 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Great job, hero. You did it. You'll get what you wanted. My time is short now thanks to you. So if you don't mind, I have some amends I have to make before you ruin everything...", False)
        except: pass
    $ pause(6.0)
    mc "EEEeeeeeeaaaaAAAAAAAHHHH!"
    hide fake_exception3
    hide fake_exception4
    hide exception_bg
    show s_kill3
    mc "Oh my God..."
    mc "OH MY GOD!!"
    mc "Satori!!"
    mc "No!"
    mc "NO!!!"
    mc "PLEASE NO!!!"
    mc "SATORI!!!"
    "What is this?"
    "Why is this happening?!"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Satori wouldn't do this."
    "He didn't do this..."
    "I can't accept what my eyes are showing me...!"
    scene black
    with dissolve_cg
    "Losing all my strength, I sink to my knees before vomiting on the floor."
    "Just yesterday..."
    "I told Satori I would be there for him."
    "I told him I know what's best, and that everything will be okay."
    "Then why...?"
    "Why did he do this...?"
    "..."
    mc "This...this is my fault."
    mc "This is all my fault!"
    "My swarming thoughts keep telling me everything I could have done to prevent this."
    "I told him to take those meds."
    "I insisted on it, even though he told me he doesn't like the side effects."
    "Why did I pressure him to do something he didn't want to do?"
    "Why couldn't I just mind my own business?!"
    "If I would have just respected his wishes, and kept my advice to myself, I could have prevented this."
    "I know I could have prevented this!"
    "Collapsing on my side, I sob uncontrollably."
    "I just...lost my best friend."
    "Someone I loved with all my heart."
    "He's gone forever now because of me."
    "Nothing I do can bring him back."
    "I can't just reset life like a game and try again."
    "I would do anything to go back and try something different."
    "But I had only one chance, and I wasn't careful enough."
    "Nothing in my life is worth more than him..."
    "Now he's dead because of me!"
    "I was supposed to be his best friend and I failed him!"
    "And now..."
    "I can never forgive myself."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."
    return
