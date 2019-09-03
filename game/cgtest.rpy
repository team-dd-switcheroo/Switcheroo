label cgtest:
    show natsuko 1l at t11 zorder 2
    n "Say...this one's actually better than your last one." 
    n "It's nice to see you putting in some effort!"
    mc "Oh...that's good."
    n 1y "I mean...I still hate it." 
    n 1c "It's trying way too hard to be serious." 
    n 3z "But, you know...nice attempt!"
    mc "...!"
    "Why you rude, little..."
    mc "Please...do explain."
    label ch2_n_bad_sharedwithch3:
        n 5b "Look, poems don't have to be all deep-sounding just to express something." 
        n 3e "It's just gonna sound like you're forcing it, unless you naturally don't suck at it." 
        n 3w "The best advice I can give: don't bother with this style until you're on Yuuri's level..."
        show natsuko 6p
        "Natsuko stops short all of a sudden."
        n "Wait a minute..."
        n 6o "You're just trying to impress Yuuri, aren't you?"
        mc "Whoa, what're you talking about?" 
        mc "And keep your voice down..."
        n 7h "Oh, don't try to play dumb, [player]." 
        n 7r "Everyone knows Yuuri is totally into this angsty crap."
        "Natsuko practically throws my poem back at me."
        n 7w "Tell you what..." 
        n "You go ahead and impress Yuuri with your whiny little emo poems." 
        n 7b "I'll be over here writing real poetry." 
        n "Hit me up when you're ready to take this seriously." 
        n 7y "Buh-bye now."
        show natsuko at thide
        hide natsuko
        "With that, Natsuko dismisses me." 
        "Whatever." 
        "At least he's not the one I was trying to impress in the first place."
        jump cg2_end

label cg2_end:
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    show mateo 6b at t11
    m "Alright, guys!"
    m "We're all done reading each other's poems, right?"
    m 6x "I have something extra planned for today, so if all of you could come sit at the front of the room..."
    return