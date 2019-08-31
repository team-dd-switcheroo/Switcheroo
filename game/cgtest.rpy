label cgtest:

    $ chapter = 0
    call poem

    scene bg club_day
    with dissolve_scene_full
    "Y CH1: [y_poemappeal[0]], N: [n_poemappeal[0]], S: [s_poemappeal[0]]"

    call cg2_y_bad
    
label cg2_y_bad:
    if y_poemappeal[0] <= 0:
        show yuuri 1a at t11 zorder 2
        y 1a "Let's see what you've written for today."
        y 1d "Hmm...well done, [player]. Your skills are already improving."
        mc "You really think so?"
        mc "Wow, thanks, Yuuri!"
        mc "That means a lot coming from you!"
        y 1c "Haha! It's nothing."
        y 1b "I'm happy to inspire my fellow writers."
        y "I know you're new to this..."
        y "So, don't worry too much if it feels like you can't get your poem to feel perfect."
        y "You needn't be afraid to be a little more daring."
        mc "How can I do that?"
        y 1i "Well...metaphors can go a long way."
        mc "Coming up with clever or beautiful metaphors is super challenging for me."
        y 1b "It doesn't have to be."
        y 3b "Writing shouldn't be a robotic activity."
        y 3m "The secret is to just let your mind wander through your feelings and write down the things you see and hear."
        y "That's one way to truly enable your reader to see inside your mind."
        y 1y "When you think about it, it's a very intimate exercise."
        mc "I see."
        mc "That's certainly an interesting technique!"
        mc "Thank you for sharing that with me."
        y 1d "I have an example of that, if you'd like to read it."
        mc "Of course."
        mc "Is this the poem you wrote for today?"
        "Yuuri nods and hands me his poem."
        return
    else:
        show yuuri 1a at t11
        y "Ah, is it my turn? Let's see how it compares to yesterday's..." 
        y 1u "Hm. I see." 
        y 1s "It's a bit different. I respect you for trying different things, [player]." 
        y 1f "Were you inspired by Natsuko's poem? Or Satori's perhaps?"
        mc "Well, I guess you can say that."
        y 1i "I thought so. I'm happy that you're experimenting." 
        y 3j "It's important to find inspiration in everyone's styles."
        "I can tell he's less enthused about this poem."
        mc "So, if you had to compare it to yesterday's..."
        y 6r "Yesterday's was a masterpiece!"
        y 6p "..."
        "Yuuri blushes and swiftly turns away."
        y 6o "I-I'm sorry. This poem is good too... It's just..."
        mc "Haha! It's okay, Yuuri! You're allowed to have a favorite."
        y 6q "Of course. I'm sorry. My stupid mind...it likes to trick me into thinking I did something wrong." 
        y 4f "Anyway... You don't need to be afraid to be a little more daring." 
        y "Metaphors can go a long way..."
        mc "Coming up with clever or beautiful metaphors is super challenging for me."
        y 1b "It doesn't have to be."
        y 3b "Writing shouldn't be a robotic activity."
        y 3m "The secret is to just let your mind wander through your feelings and write down the things you see and hear."
        y "That's one way to truly enable your reader to see inside your mind."
        y 1y "When you think about it, it's a very intimate exercise."
        mc "I see."
        mc "That's certainly an interesting technique!"
        mc "Thank you for sharing that with me."
        y 1d "I have an example of that, if you'd like to read it."
        mc "Of course."
        mc "Is this the poem you wrote for today?"
        "Yuuri nods and hands me his poem."
        return