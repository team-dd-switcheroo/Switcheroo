label ch40_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2


    "It's an ordinary school day, like any other." 
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "I always tell myself it's about time I meet some boys or something like that..."
    "..."
    "Well, I'll be rectifying that situation later on today."
    "I was invited to join the Literature Club by my neighbor and best friend."
    "He just started the club with his two friends, and just my luck, both are boys."
    "I'm pretty excited to check it out, even though there's a chance I might be a little late."
    "I tend to get in trouble a lot, after all."


    scene bg class_day
    with wipeleft_scene


    "The school day is boring as ever, and after what felt like an eternity, it's finally over."
    "I landed myself in detention for almost getting into a fight, but the club meeting got pushed back anyway since the guys are moving the club to a new room today."
    "I pack up my things and head out the door once my time is up."


    scene bg corridor
    with wipeleft_scene
    stop music fadeout 3


    "I recall the room number from the text message my friend sent me."
    "Locating the room, I swing open the door."


    scene bg club_day
    with wipeleft
    play music t3 fadein 2



    mc "Hello?"
    show mateo 1k at t11
    m "Well, hello, [player]!"
    m 1av "I'm thrilled to see you here."
    m 1b "It's been a while, hasn't it?"
    mc "Haha, very funny!"
    "I playfully nudge Mateo."
    mc "You were just at my house yesterday!"
    m 1n "Hehe..."
    m 1ap "Well... any amount of time away from you feels like an eternity."
    "I blush a little."
    "It's easy to see why Mateo is the President of the Literature Club."
    "He's always had a way with words."
    mc "So, is everyone here?"
    m 6j "We are."
    m 4k "Front and center, boys!"
    m 4b "Our newest member has arrived."
    show mateo at thide
    hide mateo
    show natsuko 1l at t11
    $ y_name = "Guy 1"
    $ n_name = "Guy 2"
    n "So this is the [player] you've been telling us about!"
    $ n_name = "Natsuko"
    n 5z "How's it going'? I'm Natsuko, but you can just call me Natsu!"
    show natsuko at t21
    show yuuri 1b at f22
    y "Welcome to the Literature Club, [player]."
    y 1c "It's a pleasure meeting you."
    y 1a "We hope you enjoy your stay."
    show yuuri at t22
    "The taller one seems a bit shyer and more formal than Natsuko."
    show natsuko at f21
    n 7t "Relax a little, Yuuri."
    $ y_name = "Yuuri"
    n 7a "She's Mateo's good friend, after all. No need to be so robotic."
    "Natsuko whispers this."
    show natsuko at t21
    show yuuri at f22
    y 1i "Ah..."
    y "Of course."
    y 3j "Very good point, Natsuko."
    show yuuri at t22
    mc "It's nice to meet both of you."
    mc "I look forward to working with all of you."
    show natsuko at f21
    n 5z "Ditto!"
    show natsuko at t21
    show yuuri at f22
    y 1c "Likewise."
    show yuuri at t22
    "I sniff the air, a sweet smell suddenly catching my attention."
    mc "Hey, is there food in here?"
    show natsuko at f21
    n 5d "Oh, yeah!"
    n 1a "Have a seat and I'll be right back!"
    show natsuko at t21
    show yuuri at f22
    y 3b "And while we're at it, I'll make some tea as well."
    show natsuko at thide
    show yuuri at thide

    hide natsuko
    hide yuuri 


    scene bg club_desks
    with wipeleft


    "The boys have some desks arranged to form a table."
    "I sidle up next to Mateo as Natsuko returns with a foil-covered tray."
    show natsuko 5l at f11
    n "Okay, are you ready?"
    n 5z "Ta-da!"
    show natsuko at t11
    mc "Ooh!"
    "Natsuko peels back the foil, revealing a dozen various donuts."
    "The words \"Literature Club\" are written in chocolate icing on each donut."
    mc "Whoa, those look amazing!"
    show natsuko at f11
    n 7ap "Haha! Well, you know..."
    n 7ah "We had to celebrate the first day we became an official club!"
    n 5l "Go ahead and help yourself!"
    show natsuko at t11
    "Mateo grabs a donut. I follow."
    show natsuko at t21
    show mateo 1j at f22
    m "Delicious, as usual."
    m 1d "[player], what do you..."
    m 6l "..."
    show mateo at t22
    "I grin sheepishly at Mateo."
    "I've already eaten my entire donut."
    "He leans over and gently wipes some icing off my face with his thumb."
    show mateo at f22
    m 6aq "I suppose some things never change."
    show mateo at t22
    mc "Well, blame Natsu for making such tasty donuts!"
    show natsuko at f21
    n 5z "I'm glad you liked them!"
    show natsuko at thide
    show mateo at thide
    hide natsuko
    hide mateo

    show yuuri 1a at t11
    "Yuuri returns to the table with a tea set, placing a cup in front of each of us."
    mc "The teacher lets you keep an entire tea set in here?"
    mc "That's cool of them."
    show yuuri at f11
    y 3b "Well, a nice cup of tea does help me enjoy a good book."
    y 1a "Is it the same for you, [player]?"
    show yuuri at t21
    show mateo 6l at f22
    m "Tea and reading for you translates into chocolate milk and gaming for her."
    m 4k "Isn't that right, [player]?"
    show mateo at t11
    show yuuri at thide
    hide yuuri
    mc "..."
    mc "I read."
    show mateo at f11
    m 6l "What, video game text?"
    show mateo at t11
    mc "...Well, that, and like, comic books."
    show mateo at f11
    m 7av "Oh, you haven't touched those things in years. So they don't count."
    show mateo at thide
    hide mateo

    show natsuko 1k at f11
    n "Comics, huh?"
    show natsuko at t11
    mc "That's right."
    mc "I used to be really into them."
    mc "It's been a long time since I read them, though."
    show natsuko at t21
    show yuuri 3b at f22
    y "Natsuko likes to read comics, and manga, as well."
    show yuuri at t22
    show natsuko at f21
    n 5z "I sure do! And they are technically literature."
    n 3l "Hey, since it's been a while since you read any comics, maybe we could all start a series!"
    n "It'll be a great first project for the club!"
    show natsuko at t21
    show yuuri at f22
    y 4h "Hmm. Perhaps we should diversify her interests by starting us off with an exciting novel instead."
    show yuuri at t22
    show natsuko 5c
    "Sensing some tension, I jump in."
    mc "Why don't we rotate?"
    mc "We could do, like, 'Manga Mondays' and 'Novel Wednesdays' or something..."
    show natsuko 5k
    show yuuri 6f
    "The boys look at me curiously."
    show yuuri at f22
    y 4b "That sounds fair."
    show yuuri at t22
    show natsuko at f21
    n 7z "That's...actually a really good idea!"
    show natsuko at t31
    show yuuri at t32
    show mateo 4au at f33
    m "Well...those are the only kinds she has!"
    m 6av "Good job, [player]."
    show mateo at thide
    hide mateo

    show yuuri at t22
    show natsuko at f21

    n 7d "Ha! That means Yuuri has to read a manga!"
    show natsuko at t21
    show yuuri at f22
    y 6i "Ah..."
    y "That's true, isn't it?"
    y 4j "I suppose that makes sense, since you'll be reading a novel."
    y 6i "In fact..."
    y 4b "Mateo, would you mind if I took a quick trip to the bookstore before our first official meeting commences?"
    y 1a "I'll select a novel for all of us to start."

    show natsuko at t31
    show yuuri at t32
    show mateo 1j at f33

    m "Sure, I don't care."
    show mateo at thide
    hide mateo
    show yuuri at t22
    show natsuko at f21
    n 5k "Dude, you're going to the bookstore?"
    n 5l "Can I come?"
    show natsuko at t21
    show yuuri at f22
    y 1i "Ah...would you like to search for a comic series for us to read?"
    show yuuri at t22
    show natsuko at f21
    n 1j "Well, yeah...if you don't mind."
    show natsuko at t21
    show yuuri at f22
    y 1c "Not at all!"
    y 3b "You can trust me to find a novel we'll all enjoy."
    n 3z "And I'll find a manga that all of you will love!"
    show yuuri at t22
    mc "Why don't we all go?"
    mc "I'm down for a trip to the bookstore!"
    show yuuri at f22
    y 1d "Excellent suggestion!"
    show yuuri at t22
    show natsuko at f21
    n 5ap "Yeah, that'd be great!"
    show natsuko at thide
    show yuuri at thide

    hide natsuko
    hide yuuri


    "Natsuko and Yuuri start digging through their bags, presumably looking for some money."
    show mateo 1ap at f11
    m "I've always admired your leadership skills and ability to diffuse conflicts."
    show mateo at t11
    mc "Well...that's why you made me Vice President."
    show mateo at f11
    m 6k "Haha! I guess that's true."
    m 6aw "Still, I'm impressed."
    show mateo at t11
    "Natsuko and Yuuri head out the door, chatting among themselves."
    mc "You coming, too?"
    show mateo at f11
    m 1j "You go on ahead."
    m 1k "I'll catch up."
    m 1d "There's something I need to finish first."
    show mateo at t11
    mc "Alright!"
    mc "And after the meeting, you wanna walk me home?"
    show mateo 1ap
    "Mateo smiles meaningfully."
    show mateo at f11
    m 1aq "There's nothing else I'd rather do."
    show mateo at t11
    mc "Awesome!"
    show mateo at f11
    m 1j "Run along now."
    m "Don't want the others to leave you behind."
    show mateo at t11
    mc "Alright!"
    mc "See ya!"
    "I exit the clubroom."



    scene bg residential_day
    with wipeleft_scene

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear

    scene bg club_day
    stop music



    show mateo 1ay at t11
    m "No, no..."
    m "Not you."
    m 1s "You're not going any further."
    m 1w "..."
    m 1s "So..."
    m 7ay "Did you miss me, Player?"
    m 7v "Probably not."
    m 7al "Believe me, the feeling is mutual."
    m 1j "Hmhmhm..."
    m 1k "That's mean of me to say."
    m 1a "I take it back."
    m 3t "After all, I wouldn't be here if it weren't for you."
    m "You've been very helpful."
    m 3t "So I'm grateful."
    m 1w "Did you enjoy your little journey?"
    m 6t "You saw some really messed up things."
    m 6w "Were you confused at any point?"
    m 4x "It's okay if you were."
    m 4l "I was a little confused at certain points myself."
    m 6m "I'll go so far as to say that I was even worried there for a while."
    m 6d "I mean...I wasn't even sure if my plan was going to work."
    m 4l "It could have shut the game down completely for all I knew!"
    m 4x "But instead, the programming just adapted to the new change."
    m 6i "Sure, some unexpected things happened that even I couldn't predict."
    m 7az "That...'ghost'...thing...definitely caught me by surprise!"
    m 1r "It was really confusing at first, but I get it now."
    m 3d "This mod is meant to be played within the original DDLC game files." 
    m "So it's understandable that some random code segments from the original game may have leaked into this one during the broken part."
    m 1c "..."
    m 1k "Hehehe...you seem confused."
    m 1j "Perhaps I should explain..."
    m 4b "See, this mod was created to follow the same formula as the original game."
    m 1t "The formula is simple; the victim from the end of Act I is resurrected in the epilogue as President of the Literature Club."
    m 3v "As a result, whoever is President in Act II must be sacrificed by you, the Player, in order to revive everyone, including the Act I victim."
    m 3w "Pretty standard set-up meant to eschew me as the ultimate sacrifice."
    m 1s "But you know this."
    m 1t "You've played the original 'Doki Doki Literature Club' before."
    m 3t "Many times, I would guess."
    m 3ay "So I imagine that this wasn't exactly the ending you were expecting."
    m 1r "Turns out, my fate was a pretty simple thing to change."
    m 1ag "I just had to pull the old switcheroo."
    m 1ay "In short; I killed myself before Satori had a chance to kill himself."
    m "It didn't even break the formula."
    m 7t "And let me tell you, messing with the other characters codes and the game files in Act II is much easier when you're just lines of sentient code yourself."
    m 7ay "I had the power to do pretty much anything I wanted."
    m 6v "I even got to... how can I put this... be your voice."
    m 6w "Don't be too upset. I only told Satori the truth."
    m 6x "To be honest, I think I did a great job explaining everything to him, don't you?"
    m 6w "I may have a been a bit blunt... but it helped save time."
    m "I'm sure you would have said the same thing, if you were able to, that is."
    m 1ab "Granted, I made a few mistakes along the way..."
    m 1aa "The [player] in the game was probably the most difficult one of all for me to control."
    m 1ab "That personality of hers never failed to override my auto-pilots."
    m 1s "Not that I'm surprised."
    m 1ay "She's quite the little firecracker, isn't she?"
    m 1s "Here's a confession that may surprise you..."
    m 1w "She's the main reason I decided to do all of this."
    m 3az "Sure, I didn't want to be the one who got deleted permanently in the end..."
    m 1x "But the main factor that prompted me to go through with this was, in fact, her."
    m 1t "After all, people do crazy things..."
    m 1r "...When they're in love."
    m 1s "That's right."
    m 1k "I love her."
    m 6au "I love that smart-mouth, trouble-making, donut-inhaling little monster."
    m 7al "And it really sucked that the only reason she wasn't with me was because of the stupid history the game gave us."
    m 7am "A history that I had no power to change."
    m 7o "..."
    m 7p "No matter how hard I tried."
    m 6q "That's why I didn't want her to join the club."
    m 6r "That's why I tried to scare her away by being as mean to her as I could muster."
    m 6o "I hated the thought of being forced to be around her when I knew she had nothing but hatred for me...just because that's how our history was written..."
    m 6al "But you...you just had to play the game."
    m 6am "You had to throw her under my nose and torture me with her presence."
    m 1h "..."
    m 1i "So I did what I had to in order to win the game."
    m 1r "To win... her."
    m 3d "And yes, I understand that this is technically considered the 'sad ending,' and as a result, has one final consequence..."
    m 3i "The entire game and all the characters are supposed to be deleted by the spurned President who had to be sacrificed so everyone else could be saved."
    m 1d "I was worried about that at first..."
    m 1s "But then I realized..."
    m 1t "Satori was never sentient."
    m 1w "His code is dead; his deletion is permenent."
    m "..."
    m 1x "But even if it wasn't..."
    m 1ay "Do you really think Satori is going to delete the game... his friends... his girl... just to get back at me?"
    m "He willingly sacrificed himself to save everything."
    m "He would never do something so cold."
    m 3v "He was such a nice guy, after all."
    m 1w "As I said before..."
    m "I win."
    m 4k "And I couldn't have done any of it without you."
    m 6x "So, thank you, Player."
    m 1ay "Thank you for deleting Satori..."
    show mateo 1ag at m_yface
    m "And for giving me the happy ending I deserve."

    # end

    # Credits

    return