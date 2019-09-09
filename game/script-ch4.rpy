label ch4_main:
    scene bg Fmbedroom
    with dissolve_scene_full
    play music t6
    "It's already Sunday." 
    if ch4_scene == "yuri":
        "I've been getting increasingly anxious about Yuuri's upcoming visit." 
        "I keep telling myself there's no reason to be nervous, but it hasn't helped much." 
        "Yuuri is clearly an introvert and a gentleman, but I think under it all, he's also a very intimate person."
        "He seems so uptight around the other guys. I'm hoping he relaxes and opens up a little more when it's just the two of us." 
        "We have been texting occasionally." 
        "He was a bit apprehensive at first but it wasn't long before I was already learning more about him." 
        "But putting Yuuri aside..." 
        "I haven't heard much of anything from Satori the past couple of days." 
        "I've called, texted and even went to his house." 
        "But each time I checked in on him, he's been passed out face down in his pillow." 
        "His \"bad day\" seems to be lingering and I don't know why." 
        "Between him and Yuuri's visit, my anxiety is through the roof." 
        "I look at the clock." 
        "Yuuri will be here in about 2 hours."
    else:
        "I've been getting increasingly anxious about Natsuko's upcoming visit." 
        "I keep telling myself there's no reason to be nervous, but it hasn't helped much." 
        "I wonder how different he's going to be when it's just the two of us?"
        "He seemed to be more openly flirty after the others left the clubroom." 
        "Meanwhile, he's been texting me a lot." 
        "We had sent each other one to double check, but it turned into a whole conversation." 
        "I'm a little surprised by how sweet he is on the phone." 
        "He's almost a different person." 
        "He's still quite flirty, but that's to be expected." 
        "But putting Natsuko aside..."
        "I haven't heard much of anything from Satori the past couple of days." 
        "I've called, texted and even went to his house." 
        "But each time I checked in on him, he's been passed out face down in his pillow." 
        "His \"bad day\" seems to be lingering and I don't know why." 
        "Between him and Natsuko's visit, my anxiety is through the roof." 
        "I look at the clock." 
        "Natsuko will be here in about 2 hours." 
    "Time for a quick, last-minute clean up." 
    "I get to work shoving clothes in the closet and papers with doodles on them into my desk drawers." 
    "Can't have my book bag just lying around, I suppose." 
    "I grab it so I can put that in the closet as well." 
    "The strap suddenly snaps and it falls to the ground, spilling everything out." 
    "I let out a long, exasperated sigh."
    mc "Awesome."
    "I drop to my knees and begin scooping up my various papers and text books." 
    "As I do so, I dismissively look through some of the papers." 
    "Let's see." 
    "Failed test..." 
    "Detention slip..." 
    "Notes I never used..." 
    "Countless doodles..." 
    "Another detention slip..." 
    "...?" 
    "I suddenly come across what appears to be a prescription bag with a couple of pill bottles inside." 
    mc "What the..." 
    "This isn't mine..."
    "I look it over and check for a name." 
    mc "...!"
    mc "S-Satori?!"
    "This must have been put into my bag by mistake when we took that trip down the stairs a few days ago." 
    "Since when is he on medication?" 
    "I pull out the bottles and scan their labels carefully."
    "I grab my phone and look up both medications." 
    "..."
    "..."
    mc "Whoa...what?! How?! Since when?!"
    "I hastily finish shoving everything else in my closet." 
    if ch4_scene == "yuri":
        "I don't have much time before Yuuri comes over." 
    else:
        "I don't have much time before Natsuko comes over." 
    "But despite this, I race out the door." 
    "Whether Satori likes it or not, I'm coming over and we are going to talk about this."

    scene bg residential_day
    with wipeleft_scene
    stop music fadeout 2.0
    "I don't even bother to text or call." 
    "I don't even knock." 
    "I just swing the door open and head inside." 
    "It's not unusual, after all." 
    "We hang out at each other's houses so often, we practically live together."
    scene bg black
    with wipeleft_scene
    "The house is quiet." 
    "Satori isn't anywhere on the first floor, so I head upstairs." 
    "I half expected him to come down and shoo me back out the door, but the entire house is silent." 
    "My heart races." 
    "I head up to his bedroom and gently open the door."
    scene bg satori_bedroom
    with wipeleft_scene
    show satori 11o at t11 zorder 2
    "I see him lying on the bed, but he promptly leaps to his feet, clearly startled by my sudden entrance."
    s 17j "Jeez, knock much?"
    "My blood pressure settles down a bit."
    show satori 11i at t11 
    "He looks tired and a bit irritated, but otherwise, okay." 
    "I quietly take a seat on the bed."
    show satori 11g at t11
    "He reluctantly sits down next to me." 
    show satori 11y at t11
    "He forces a smile." 
    "There's a moment of silence between us."
    s 12y "You didn't need to come over." 
    s 11k "I mean..." 
    s 11d "I'm happy to see you and everything..." 
    s 17g "But don't you have something more important to do today?"
    mc "..."
    mc "What do you mean?"
    if ch4_scene == "yuri":
        s 11f "Yuuri..." 
        s "You're supposed to be working with him today, aren't you?"
        mc "...How did..."
        "Satori had gone home by the time we decided that last meeting."
        "But I quickly realize how he knows."
        mc "Mateo told you, didn't he?" 
        s 11h "Of course."
        s "He's supposed to keep me up to date on the festival preparations." 
        s 11av "I'm the Vice President, after all..." 
        mc "Yeah...yeah." 
        mc "So how 'bout you?" 
        mc "You're helping him today, right?"
        s 11g "Yeah, but only online." 
        s "We don't have to meet up or anything." 
        s 11at "Anyway, I bet you're excited to be working with Yuuri, huh?"
    else:
        s 11f "Nat... You're supposed to be baking with him today, right?"
        mc "...how did you know that?"
        mc "...How did..."
        "Satori had gone home by the time we decided that last meeting."
        "But I quickly realize how he knows."
        mc "Mateo told you, didn't he?" 
        s 11h "Of course."
        s "He's supposed to keep me up to date on the festival preparations." 
        s 11av "I'm the Vice President, after all..." 
        mc "Yeah...yeah." 
        mc "So how 'bout you?" 
        mc "You're helping him today, right?"
        s 11g "Yeah, but only online." 
        s "We don't have to meet up or anything." 
        s 11at "Anyway, I bet you're excited to be baking with Nat, huh?"
    mc "Satori, I'd rather be working with you."
    show satori 11i at t11
    "Satori looks over at me briefly." 
    s "No you wouldn't." 
    if ch4_scene == "yuri":
        s 11au "I know you've wanted to be alone with Yuuri since you joined the club."
    else:
        s 11au "I know you've wanted to be alone with Nat since you joined the club."
    mc "That's not...!"
    mc "...Look, that's not what I came here to talk about." 
    mc "I'm here to talk about this."
    show satori 11o at t11
    "I hold up the bottle labeled ZYPREXA." 
    "Satori quickly snatches the bottle from my hands."
    s 11c "How the heck did you get this?!"
    mc "It was put in my backpack on accident a few days ago when we fell down the stairs."
    s 17at "Well, this explains why I've been able to sleep so well the past couple of days."
    mc "Yeah, I know."
    mc "I looked it up and saw one of the main side effects is insomnia."
    mc "Satori...how long have you been on this?"
    s 11k "..."
    s 11g "You're not gonna like the answer."
    mc "I don't care." 
    s "[player]..."
    mc "Don't '[player]' me!"
    s 17ac "Sigh. You're just gonna make me say it, aren't you?"
    mc "..."
    s 11av "Fine..."
    s "The truth is..."
    s 11k "I was diagnosed with Bipolar Disorder when I was 10 years old."
    s 17g "I've been on Zyprexa ever since."
    "The news hits me like a ton of bricks."
    "I don't even know how to respond."
    "I slowly rise to my feet, my shocked gaze locked on Satori's face."
    mc "T-t-ten?"
    s 14h "Told ya you weren't gonna like the answer..."
    mc "I..I just...I don't understand. We're best friends..."
    mc "We tell each other everything. Why wouldn't you tell me about this? Knowing I could help?"
    s 11ab "I didn't tell you because I didn't want you to worry about me." 
    s 11k "You do that a lot, you know." 
    s 11at "You spend so much time worrying about me that you don't have time to do important things."
    "I feel myself getting increasingly angrier at his words."
    mc "Of course I worry about you, you're my best friend!"
    mc "You're so important to me, I even worry about you when I watch you cross the street!"
    mc "I love you, you big stupid idiot! Why would you not tell me about this?!"
    mc "What is even the point of us being best friends if you're not gonna be open and honest with me about stuff like this?!"
    mc "God, I can't believe...you never told me..."
    s 12g "...Are you mad at me?"
    "I shake my head silently."
    mc "I just...I don't understand why you kept this from me."
    s 11av "You can never understand."
    mc "What, because you didn't want me to worry about you?"
    mc "C'mon, Satori."
    mc "That's ridiculous..."
    s 11g "To you, maybe."
    s "But having you worrying about me...and caring about me..."
    s 11h "It feels like a bat being swung against my head."
    s 11k "It's bittersweet to have anyone care about me."
    s 17h "That's why I wanted you to make friends with everyone in the club when you decided to join."
    s 15av "I figured, if I could get you to care for them, you'd stop caring about me..."
    mc "Really? Is that what you think?"
    "I walk away a few feet, staring at nothing."
    mc "You think I'm so shallow and heartless that I could just abandoned my best friend for the first guy to write me a poem?"
    mc "..."
    s 11g "..."
    "Now I feel myself becoming increasingly emotional."
    "I want to stop myself before I become irrational, but I find myself unable to curb my tongue."
    mc "Is that why you never told me about this, Satori?"
    "My voice cracks."
    mc "Am I that bad of a friend that you just felt you couldn't trust m-..."
    "Before I have a chance to finish, Satori jumps to his feet and wraps his arms around me, pulling me into an embrace."
    scene bg black
    with dissolve_cg
    "Tears freely begin to flow from my eyes as his embrace tightens." 
    s "Please..."
    s "Please don't do this..."
    "He begins to tremble."
    s "I...I don't want you to hurt...because of me..."
    s "I...I'm sorry I made you feel this way."
    mc "No..."
    "I wrap my arms around him in return."
    mc "I'm the one who's sorry." 
    mc "I'm so, so sorry you've been going through this for so long and I hardly even noticed." 
    mc "What kind of friend am I that I didn't even pick up on the fact that you were struggling with this?" 
    mc "How could I be so blind?"
    mc "I'm sorry, Satori..." 
    mc "I'm... I'm a terrible friend."
    s "..."
    s "No, [player]..."
    s "Don't say that." 
    "He holds me so tight against him, I can feel his heart pounding."
    "I instantly regret what I said before, as I predicted I would."
    "This isn't about me. This is about my best friend. It's my job to find out how I can help him."
    "I rest my face against his shoulder and sigh."
    s "You're the most wonderful friend anyone could ever ask for."
    s "I love you so much."
    s "That's why I didn't tell you."
    s "I don't deserve to have such an amazing and big-hearted person care about me so much."
    s "You just don't understand...how much it hurts..."
    mc "But why?"
    mc "Why do you feel so selfish and undeserving?"
    mc "The meds are working, right?"
    s "..."
    s "Yeah..."
    s "When I take them."
    scene bg satori_bedroom
    with dissolve_cg
    show satori 11k at t11
    "Satori and I release our embrace and slowly part."
    mc "What do you mean 'when you take them'?"
    "Satori shrugs indifferently."
    s 11at "I don't ALWAYS take them."
    s 17i "You read for yourself that they cause insomnia. I gotta get sleep sometime..."
    s "..."
    s 17h "So on days when I'm moodier than usual..."
    s "It's because I didn't take them, so that I could sleep."
    "I swallow nervously as I reach into my pocket and wrap my fingers around the 2nd pill bottle."
    mc "Well...I can understand that."
    mc "But, truthfully, those aren't the meds I was talking about."
    show satori 11ae at t11
    "I notice Satori's expression change as I pull the bottle labeled LITHIUM from my pocket."
    mc "I'm talking about this."
    "He backs away a couple steps."
    s 11ad "I don't need THAT stuff."
    mc "They wouldn't have prescribed it if you didn't need it, Satori."
    s 15ah "Well I don't need it, alright?"
    hide satori
    with wipeleft
    "He snaps as he crosses his arms and leans against the wall, his back turned."
    s "I'm not taking it. Period."
    "I sigh and stand up." 
    show satori 11ad at t11
    "I walk to the center of the room and stand near him."
    mc "You really need to reconsider that decision."
    s 17i "Yeah? And what makes you so sure of that?"
    mc "Because they only prescribe that stuff to people with depression..."
    mc "..."
    mc "People with..."
    mc "Suicidal thoughts."
    s 11au "There's nothing to worry about."
    s 18j "It's common for people with BPD to have bouts of depression."
    s 11at "I'm fine as long as I have the zyprexa."
    mc "It just seems weird that they'd prescribe such a serious medication made for severe depression to someone who just has 'bouts' of it..."
    s 14j "Look, they just overreacted when they prescribed it to me!"
    s 11i "I'm not gonna do anything crazy."
    s "So just drop it, okay?"
    mc "..."
    mc "'Sad Thoughts' was about your depression, wasn't it?"
    "Satori shakes his head and gives an annoyed grunt." 
    s 17j "I already told you..." 
    s "You looked too much into that poem." 
    s 11at "I'm sorry I ever wrote the stupid thing."
    mc "I'm not. I love that poem." 
    mc "It's my personal window into your mind." 
    mc "And when I look in that window and see that you have a little raincloud in your head..." 
    mc "Well, I can come in and give that raincloud a little hug." 
    mc "And make a big happy rainbow."
    s 11ap "[player], that's..." 
    s 11y "That's so corny."
    "Satori smiles a bit." 
    "Even though he's smiling, I can feel the melancholy radiating off of him." 
    mc "Satori..."
    s 11g "Yeah?"
    mc "..."
    mc "You were diagnosed with BPD when you were 10, and you said that's when they prescribed the zyprexa, right?"
    s 11b "Right."
    mc "..."
    mc "When was the lithium first prescribed to you?"
    s 11ab "..."
    s 11at "Doesn't matter."
    s 17j "I already told you I'm not taking it."
    show satori 11at at t11
    "He stubbornly walks over to his bedroom window."
    mc "Well, at least tell me what you get depressed about..."
    if ch4_scene == "yuri":
        s 11au "Yuuri's coming."
        "He cuts me off." 
        "I look down on the street and sure enough, I spot Yuuri walking towards my house carrying some bags." 
        "I completely forgot he was coming over." 
        "I look at Satori, who keeps his gaze on Yuuri below." 
    else:
        s 11au "Nat's coming."
        "He cuts me off." 
        "I look down on the street and sure enough, I spot Natsuko walking towards my house carrying some bags." 
        "I completely forgot he was coming over." 
        "I look at Satori, who keeps his gaze on Natsuko below."
    mc "Satori...if you need me today, I'll cancel.."
    s 13m "Don't do that, [player]!"
    "I jump back, startled." 
    show satori 11e at t11
    "Satori immediately realizes the effect of his outburst and shrinks back a little."
    s 12g "I'm sorry..."
    s "It's just..."
    s 17h "I'm sure he's been looking forward to this all weekend."
    s "Please don't ruin that for him."
    s 15d "Besides, I'll be busy today." 
    s "I still have some festival stuff to talk about with Mateo."
    mc "...Alright."
    "I get up and head for the door." 
    "I stop and look back at Satori, still standing in front of the window with his back to me."
    if ch4_scene == "yuri":
        mc "If, um...if you finish early with helping Mateo, feel free to come over to help me and Yuuri with the decorations."
    else:
        mc "If, um...if you finish early with helping Mateo, feel free to come over to help me and Natsu with the donuts..."
    "Satori merely shakes his head."
    s 11g "No, thanks." 
    s "I'll see him tomorrow at the festival." 
    s 11d "You two have fun."
    mc "Okay."
    mc "We'll have a good time at the festival, though, right?"
    mc "I mean..." 
    mc "If you're okay with it, I'd like to spend the day with you." 
    mc "Would... Would that be alright?"
    "Satori turns his head slightly."
    show satori 11k at t11
    "I was hoping for an excited grin, but instead, he gives me a sad smile." 
    "After a moment, he nods."
    s 17d "Of course, if that's what you want." 
    s 11k "But I wish you'd consider spending your time with everyone else."
    mc "I will." 
    mc "I plan on having fun with all my friends." 
    mc "The friends I wouldn't have if it weren't for you." 
    mc "But no matter how many new friends I make, I'll never be far from your side." 
    mc "Because we're best friends." 
    show satori 11y at t11
    mc "And you're stuck with me no matter what."
    show satori 11q at t11
    "Finally, I manage a smile out of Satori." 
    "There's real happiness in it this time."
    show satori 11d at t11 
    "It quickly fades, but it gives me hope that I can bring it back out again." 
    "I just wish he would tell me more about his depression so maybe I can help him."
    "I guess I'll just have to be patient and hope he eventually decides to confide in me."
    "I step out the door and grab the knob."
    mc "If you change your mind, feel free to drop by."
    "Satori gives me one more melancholy smile and nod before I slowly close the bedroom door behind me."
    #call expression "ch4_exclusive_" + ch4_scene
    call ch4_end
    return

label ch4_end:
    scene bg Fmbedroom
    with wipeleft_scene
    stop music fadeout 2.0
    show satori 11av at t11
    "Once we're in my room, I shut the door and take a seat on my bed." 
    "I feel anxious over what Satori might tell me." 
    mc "So, um...what's on your mind?"
    s "..." 
    s 11k "I've been thinking about what you said this morning." 
    s 17k "About how we're best friends and we trust each other with everything." 
    s "And..." 
    s "Well..." 
    s 11f "You're right."
    s "You deserve to know what's going on."
    "I smile a little in relief."
    "Looks like he's going to open up to me after all." 
    "I lean forward a bit, my full attention on Satori."
    mc "I'm all ears."
    mc "Tell me everything, Satori." 
    mc "The more I know, the more I can do to help."
    s 11k "Right..."
    s "..."
    s 17h "The Lithium was prescribed to me last year..."
    s 15av "...After I was diagnosed with chronic depression."
    "I sigh and nod."
    "I knew it."
    mc "I see..."
    mc "Do you know what caused you to become depressed?"
    "He nods."
    s 11f "Yeah. I do."
    s 11h "It was because I came to a realization."
    mc "What did you realize?"
    "He takes a deep breath."
    s 11ax "I realized...I have...feelings..."
    play music t9
    s "Selfish, selfish feelings..."
    mc "...?"
    mc "Selfish feelings?"
    mc "I...I don't think I understand..."
    s 11ay "It's easy, [player]."
    s "I discovered..."
    s 15az "...That I hate the idea of you getting a...a boyfriend."
    s 15an "Isn't that disgusting of me?"
    s 15w "To act like you're a shiny toy that I want only for myself?" 
    s 11v "I mean..."
    s "You're such an amazing, smart, funny person."
    s 17e "Everyone deserves to be around you."
    s 15ax "And even knowing that..."
    s 15aw "I still hate the thought of you being...with someone else."
    s 15ay "I realized...someone as selfish as me doesn't deserve to be around someone as wonderful as you."
    s 11av "That's why I didn't want to take the Lithium."
    s 11aw "Don't you see? I deserve to feel this way."
    s "I deserve to hurt..."
    s "I deserve...to be punished for being weak and selfish."
    s 11v "Why do you think I never personally invited you to the club?"
    s 11w "I didn't want them to be around you..."
    s 13w "To see how beautiful and amazing you are."
    s 15an "I knew they'd be head over heels for you."
    s 12aw "I mean...sure, I was excited to have you visit."
    s 17v "And after you decided to join, I figured it'd be a great chance for us to get to spend even more time together."
    s 15aw "But...on our way home that day...you...you said you liked them..."
    s "You wanted them to...like you."
    s 15v "And...I just want you to be happy."
    s 15ax "..."
    s 15ay "Agreeing to help you...giving you advice on how to impress them...it..."
    s 15az "It felt like my heart being ripped in half..."
    s 15an "But...it was a bittersweet blessing in disguise, you know?"
    s 15v "I figured if you got closer to one of them, you'd forget about me."
    s "You wouldn't have me to hold you back."
    s 15aw "If you stopped caring about me..."
    s "You wouldn't care if anything happened to me..."
    mc "Satori..."
    s 15w "Hold on!"
    s 15u "There's something else..." 
    s 11v "I realized that the closer you got to each of them..." 
    s 13an "The more it felt like a spear going through my heart." 
    s "[player]..." 
    s "Just the thought of you doing anything...romantic...with one of them..."
    s 13am "It hurts so much!" 
    s "It makes me sad and angry; at them and at myself!" 
    s 13az "The thought of you with anyone else but me makes me want to die!"
    mc "Satori, don't say things like that!"
    s 13w "I can't help it, [player]!" 
    s 13an "The truth is..." 
    s 13v "I...I love you." 
    mc "..."
    s "Those are my true feelings." 
    s 15v "I've always loved you."
    s 11aw "And...starting last year..."
    s 11v "I realized...I'm in love with you." 
    s "I mean..."
    s 17v "We've been saying it to each other for years." 
    s "But I don't just say it to you because it's a thing to say."
    s 15v "I mean it every single time."
    "Satori suddenly steps closer to me, gently taking my hands in his own."
    s 11u "What about you?"
    s "Do you mean it, [player]?"
    s 11v "Do you feel anything at all when you tell me that you love me?"
    "I meet Satori's gaze." 
    "I owe it to my best friend to be completely honest with him." 
    mc "Satori, listen to me." 
    menu:
        mc "Every time I tell you that I love you, I mean..."
        "I'm in Love with You":
            $ sayori_confess = True
            call ch4_end_yes
        "I Love You Like a Brother":
            $ sayori_confess = False
            call ch4_end_no
    return

label ch4_end_yes:
    mc "I'm in love with you." 
    show satori 11e at t11
    mc "I've felt this way for a while too."
    mc "I mean...of course I mean it when I say it." 
    mc "And if we both love each other this much, well..." 
    mc "There's no point in worrying about me doing anything with the others!" 
    mc "These past few days in the club have been amazing." 
    mc "I've made some great new friends because of you." 
    mc "But being in the club has also made me realize something else." 
    mc "Satori...you're my reason for waking up in the morning."
    mc "Not just because of school." 
    mc "But because I want nothing more than to have yours be the first face I see every day." 
    mc "I've had so much fun in the club because you and I get to spend more time together than ever before." 
    mc "Whether or not I've had fun with the others is irrelevant." 
    mc "The only thing that matters to me is getting to spend every day with you."
    "Satori stares at me in bewilderment."
    "I expect him to hug me, but that doesn't seem to be the case."
    s "...[player]..." 
    s 11k "For years, I've dreamed of hearing you say that you feel the same way about me as I feel about you." 
    s "This is supposed to be the happiest moment in my life." 
    mc "..."
    mc "Supposed to be?"
    mc "Satori..."
    show satori 15ao at t11
    "Satori's look of shock suddenly transforms into one of frustration."
    s 13ah "No!"
    s 13am "What have I done?"
    s "Confess to you..."
    s "I shouldn't have confessed to you!"
    s 13an "That's not why I came here!"
    s 13ao "Why did I do that?!"
    s "Why did I make the stupid mistake of expressing my feelings!?"
    s 13ak "Ugh, I just made everything WORSE!"
    mc "Satori, what're you..."
    s 13ah "NO!"
    "He slams his fist against my wall."
    s 13az "WHY CAN'T I STOP BEING SELFISH?!"
    mc "Would you calm down!?"
    show satori 13an at t11
    mc "You're not being selfish!"
    mc "What's wrong with me wanting to be with you?"
    mc "Isn't that what you want?"
    s 13ao "Yes...No!..."
    s 13am "I DON'T KNOW!!!"
    mc "Well, Jesus, dude!"
    mc "I hate to have to point this out, but..."
    mc "Maybe you'll think a little more clearly if you took your medication!"
    show satori 13v at t11
    mc "And I mean both of them!"
    mc "Because it's really hard for me to try to help you when you're warping the meaning of your feelings in a way that makes you sound like you're being the bad guy here!"
    mc "And you're not!"
    mc "You're a wonderful person who I love with all my heart and I just want you to take care of yourself!"
    s 13ak "...I just want YOU to hate me!"
    s "Why is that so hard?"
    mc "I just want YOU to TAKE YOUR MEDS!!"
    mc "WHY IS THAT SO HARD!?"
    "We stare each other down with annoyed scowls."
    show satori 13af
    "I didn't mean to yell at him."
    "I'm just frustrated by his inability to think rationally right now, even though it's not really his fault."
    "I can imagine he's not the only one with these problems who doesn't like taking his meds..."
    s 11ao "..."
    s 11ac "You...want me to take them that bad?"
    s 11at "Fine."
    s au "I will."
    mc "..."
    mc "Seriously?"
    mc "You're not just trying to placate me?"
    s 11av "No."
    s "I'm being 100% honest with you."
    s 11k "When I go home...I will take my meds."
    mc "The lithium, too?"
    s 11ax "..."
    s 11ay "Yeah."
    mc "...Alright."
    mc "Thank you."
    mc "I know the other zyprexa messes with your sleep...but...try to take some of that too, okay?"
    s 11k "Sure thing."
    "I nod, eying him curiously."
    mc "Okay, then."
    mc "I appreciate you doing that for me, Satori."
    mc "The meds really will help, you know."
    s 11ay "..."
    s "They sure will." 
    "His anger fades into bland complacence."
    "It has me a little worried about him being alone tonight."
    mc "...Do you wanna stay over for a little bit?"
    mc "Play a few games?"
    show satori 11av at t11
    "Satori stares off in a random direction and gives an empty smile."
    s 11d "No, thanks."
    s "I think I'm gonna turn in early."
    mc "Alright. Good idea."
    mc "We'll both wanna be up early tomorrow anyway, right?"
    s 11k "...Right."
    hide satori
    "He starts to leave."
    "I still feel uneasy with his emotionless responses."
    mc "Satori..."
    "He stops in front of my bedroom door, though he doesn't turn to face me."
    "I walk over and stand between him and the door."
    "He keeps his head down."
    "Slowly, I lean in and embrace him."
    scene black # show satori weekend cg1
    with dissolve_cg
    "He refrains from hugging me back."
    "Undeterred, I pull him closer."
    #show satori weekend cg2
    "We stand in silence for a few moments before I finally feel his muscles relax a bit."
    "A few more moments pass and his arms slowly wrap around me in return."
    #show satori weekend cg3 
    s "I just...I just want the raincloud to go away..."
    "He whispers this in a trembling voice."
    "I lean my head against his chest."
    #show satori weekend cg4
    mc "It will."
    mc "It might take a little while, but the sunshine will come back and chase that old raincloud away."
    mc "I'll make sure of it."
    mc "You trust me, right?"
    s "...Yeah."
    scene bg Fmbedroom
    with dissolve_cg
    show satori 11aw at t11
    "We slowly part."
    mc "Are you sure you're gonna be okay tonight?"
    s 11v "...Yeah. I'm sure."
    mc "Okay."
    mc "We're gonna have lots of fun at the festival, right?"
    s "...Of course."
    s 11t "It'll be great."
    show satori at thide
    hide satori
    "He gives me another sad smile before quietly leaving the room."
    "I hear him trot down the stairs and leave through the front door." 
    "I watch from my window as he heads down the street to his house."
    "I can't help but feel a sense of uneasiness." 
    "What if my suggestion for him to take his meds backfires and it ends up making him worse?"
    "What if I should be doing something more, or something different?" 
    "I know these thoughts will continue to plague me until I see if my suggestion works or not."
    "If he takes my advice, I should notice any changes in his behavior by tomorrow." 
    "I hope he'll be back to his normal, cheerful self by then."
    "Either way, I'm willing to do whatever it takes to give Satori a happy life with me."
    return

label ch4_end_no:
    show satori 11v at t11
    mc "...I love you like a brother." 
    show satori 11e at t11
    mc "I'm comfortable doing everything with you." 
    mc "I can tell you anything and everything." 
    mc "I mean, I know we're not really siblings." 
    mc "But...we might as well be, you know?" 
    show satori 11aw at t11
    mc "And there's nothing wrong with that."
    mc "I'll always love you. Nothing is gonna change that."
    mc "I'll be here for you whenever you need me."
    mc "No matter what..."
    mc "You'll always be my buddy."
    s 11az "I... I see..."
    "Satori's eyes fill with tears." 
    "He slowly backs away from me."
    s 11v "So this is what it feels like to be stabbed in the chest..."
    mc "...Satori..."
    s 11u "No. You're 100% right, [player]." 
    s 15aw "We...we're better off keeping things the way they've always been." 
    s "I mean...everything was perfect before I accidentally showed my feelings." 
    s 15az "We wouldn't even be having this conversation right now if it hadn't been for that stupid, selfish mistake."
    "Satori has a hard time keeping his voice steady."
    s 15v "I trust you to know what's best for me." 
    s "Keeping things the way they've always been." 
    s 11aw "It's what I want too..."
    "He looks away, tears streaming down his face."
    s 11ay "Really...this couldn't have turned out better..."
    "I swallow nervously, realizing that me turning down his confession could seriously impact his depression."
    mc "Satori..."
    mc "I...I know you don't want to hear this..."
    mc "But...now that you have the lithium on hand...please consider taking it."
    "He gives an emotionless chuckle."
    s 11t "It wouldn't have been an issue either way."
    s "I have tons of it stockpiled in my medicine cabinet."
    mc "Well...it would make me really happy if you started taking it."
    mc "I'm sure it'll help you a lot..."
    s 11y "..."
    s "You know what?"
    s 11t "Maybe I will."
    mc "Really?"
    s 11y "..."
    s 11t "Sure."
    s "If it'll make you happy..."
    mc "It will."
    "Satori passively nods."
    s "Alright."
    s "When I go home, I'll take my meds."
    mc "The lithium, too?"
    s "...Of course."
    mc "Thank you."
    mc "And in return, I'll make sure you have a lot of fun at the festival tomorrow."
    mc "Sound good?"
    s 11aw "..."
    s 11t "Yeah."
    s 17t "I'm sure it'll be fun." 
    show satori at thide
    hide satori
    "Satori gives me one more sad smile as he leaves my room."
    "I listen as he wordlessly descends the stairs and walks out the front door." 
    "I look out my window and watch him slowly cross the street and make his way to his house." 
    "I can't help but feel a sense of uneasiness." 
    "What if my suggestion for him to take his meds backfires and it ends up making him worse?"
    "What if I should be doing something more, or something different?" 
    "I know these thoughts will continue to plague me until I see if my suggestion works or not."
    "If he takes my advice, I should notice any changes in his behavior by tomorrow." 
    "I hope he'll be back to his normal, cheerful self by then."
    "Either way, I'm willing to do whatever it takes to help Satori get through this difficult time." 
    return