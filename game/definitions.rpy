# Definitions.rpy

# This section defines stuff for DDLC and your mod!

# Use this as a starting point if you would like to override with your own.

define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
# Change this to True to enable Developer Mode
define config.developer = "Auto"  # Or True

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # Get's position of Music
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # Delete's All Saves
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # Delete's Characters
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass

    # Restores Character's CHR
    def restore_all_characters():
        try: renpy.file("../characters/mateo.chr")
        except: open(config.basedir + "/characters/mateo.chr", "wb").write(renpy.file("mateo.chr").read())
        try: renpy.file("../characters/natsuko.chr")
        except: open(config.basedir + "/characters/natsuko.chr", "wb").write(renpy.file("natsuko.chr").read())
        try: renpy.file("../characters/yuuri.chr")
        except: open(config.basedir + "/characters/yuuri.chr", "wb").write(renpy.file("yuuri.chr").read())
        try: renpy.file("../characters/satori.chr")
        except: open(config.basedir + "/characters/satori.chr", "wb").write(renpy.file("satori.chr").read())
        try: renpy.file("../characters/femc.chr")
        except: open(config.basedir + "/characters/femc.chr", "wb").write(renpy.file("femc.chr").read())
    
    # Restores Characters if their playthough matches current run.
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("satori")
        elif persistent.playthrough == 3:
            delete_character("satori")
            delete_character("natsuko")
            delete_character("yuuri")
        elif persistent.playthrough == 4:
            delete_character("mateo")

    # Controls time.
    def pause(time=None):
        #global _windows_hidden
        if not time:
            #_windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            #_windows_hidden = False
            return
        if time <= 0: return
        #_windows_hidden = True
        renpy.pause(time)
        #_windows_hidden = False

# Music

# This section is where you can reference DDLC audio and add your own!
# audio. - tells Ren'Py this is sound
# t1 - tells Ren'Py the label of the music/sound file
# <loop 22.073> - tells Ren'Py to loop the song at that time interval
# "bgm/1.ogg" - location of your music
define audio.t1 = "<to 138.026 loop 15.396 to 138.026>mod_assets/audio/main_theme.ogg" #Title theme
define audio.t1g = "<to 138.026 loop 15.396 to 136.719>mod_assets/audio/main_theme.ogg" #Title theme wobbly section
define audio.t2 = "<to 156.290 loop 0.026 to 78.290>mod_assets/audio/ohayou_satori.ogg" #Ohayou Satori!
define audio.t2g = "<to 156.290 loop 0.026 to 76.505>mod_assets/audio/ohayou_satori_glitch.ogg" #Ohayou Satori! Wobbly Section
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg" #Ohayou Satori! Rapid Glitch
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg" #Ohayou Satori! Gradual Pitch Increase
define audio.t3 = "<loop 0.027 to 56.024>mod_assets/audio/in_game_main_theme.ogg"   #Main theme (in-game theme)
define audio.t3g = "<loop 0 to 56.655>mod_assets/audio/in_game_main_theme_glitch.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg" 
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t4 = "<loop 57.630>mod_assets/audio/poem_game.ogg"  #Poemgame
define audio.t4g = "<loop 1.000>bgm/4g.ogg" #Static and Error
define audio.t5 = "<loop 7.444>mod_assets/audio/okay_everyone.ogg" 
define audio.t5_2 = "<loop 7.444>mod_assets/audio/okay_everyone_2.ogg"  #Okay Everyone!


# Doki Poem Theme
define audio.tmateo = "<loop 4.444>bgm/5_monika.ogg" #Okay Everyone! (Mateo)
define audio.tsatori = "<loop 4.444>bgm/5_sayori.ogg" #Okay Everyone! (Satori)
define audio.tnatsuko = "<loop 4.444>bgm/5_natsuki.ogg" #Okay Everyone! (Natsuko)
define audio.tyuuri = "<loop 4.444>bgm/5_yuri.ogg" #Okay Everyone! (Yuuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 4.414>mod_assets/audio/play_with_me.ogg" #Play With Me
define audio.t6_2 = "<loop 4.414>mod_assets/audio/play_with_me_2.ogg" #Play with me 2
define audio.t6_2f = "<loop 4.414>mod_assets/audio/play_with_me_2_fast.ogg" #Play with me 2 sped-up 1.5 times
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 3.898>mod_assets/audio/poem_panic.ogg" #Poem Panic!
define audio.t7a = "<loop 11.761 to 19.559>mod_assets/audio/poem_panic.ogg"
define audio.t7b = "<from 35.167 to 42.984 loop 35.169>mod_assets/audio/poem_panic.ogg"
define audio.t7g = "<loop 46.055>mod_assets/audio/poem_panic_glitch.ogg"
define audio.t8 = "<loop 8.324>mod_assets/audio/daijoubu.ogg" #Daijoubu
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #My Feelings
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed (My Feelings)
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>mod_assets/audio/my_confession_2.ogg" #Yuri Confession
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.door_knock = "mod_assets/audio/door_knock.ogg"
define audio.bap_half = "mod_assets/audio/bap_half.ogg"
define audio.bap_full = "mod_assets/audio/bap_full.ogg"
define audio.fire_alarm = "<loop 0>mod_assets/audio/fire_alarm.ogg"
define audio.light_switch = "mod_assets/audio/light_switch.ogg"
define audio.breathing_audio = "mod_assets/audio/creepy_breathing.ogg"
define audio.giggle_audio = "mod_assets/audio/creepy_giggle.ogg"
define audio.shrieking_audio = "mod_assets/audio/shrieking.ogg"
define audio.scatter_books = "mod_assets/audio/scatter_books.ogg"
define audio.growing_fire = "<loop 0>mod_assets/audio/growing_fire.ogg"
define audio.tearing_flesh = "mod_assets/audio/tearing_flesh.ogg"
define audio.stab = "<from 4 to 5>sfx/stab.ogg"
define audio.fall = "sfx/fall.ogg"

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg residential_day2 = "mod_assets/images/bg/residential2.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg corridor2 = "mod_assets/images/bg/corridor2.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club2_day = "mod_assets/images/bg/clubroom2.png" # Start of DDLC BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg satori_bedroom = "mod_assets/images/bg/satori_bedroom.png" # Sayori's Room BG
image bg satori_bedroom2 = "mod_assets/images/bg/satori_bedroom2.png" # Sayori's 2nd Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg house2 = "mod_assets/images/bg/house2.png" # Sayori's 2nd House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

image bg glitch = LiveTile("bg/glitch.jpg")

image bg club_desks = "mod_assets/images/bg/club_desks.png"
image bg Fmbedroom = "mod_assets/images/bg/femc_bedroom.png"
image bg Fmbedroom2 = "mod_assets/images/bg/femc_bedroom2.png"

# Act 2 Assets Per Day
image bg class_act2 = "mod_assets/images/bg/class_act2.png"
image bg class2_act2 = "mod_assets/images/bg/class2_act2.png"
image bg act2_corridor = "mod_assets/images/bg/act2_corridor.png"
image bg act2_stairs = "mod_assets/images/bg/act2_stairs.png"
image bg act2_corridor2 = "mod_assets/images/bg/act2_corridor2.png"
image bg club_act2_glitch3 = "mod_assets/images/bg/club2_act2_glitch3.png"
image bg club_act2_glitch2 = "mod_assets/images/bg/club_act2_glitch2.png"
image bg club_act2_glitch = "mod_assets/images/bg/club_act2_glitch.png"
image bg club_act2 = "mod_assets/images/bg/club_act2.png"
image bg club_desks_act2 = "mod_assets/images/bg/club_desks_act2.png"
image bg club_act2_dark = "mod_assets/images/bg/club_act2_dark.png"
image bg club_act2_ghost_yuri1 = "mod_assets/images/bg/club_act2_ghost_yuri1.png"
image bg club_act2_ghost_yuri2 = "mod_assets/images/bg/club_act2_ghost_yuri2.png"
image bg club_act2_ghost_yuri3 = "mod_assets/images/bg/club_act2_ghost_yuri3.png"
image bg club_act2_ghost_yuri4 = "mod_assets/images/bg/club_act2_ghost_yuri4.png"
image bg club2_act2 = "mod_assets/images/bg/club2_act2.png"
image bg club2_act2_bloodwall = "mod_assets/images/bg/club2_act2_bloodwall.png"
image bg closet_act2 = "mod_assets/images/bg/closet_act2.png"
image bg residential_act2 = "mod_assets/images/bg/residential_act2.png"

image splash_glitch_alt:

    parallel:
        choice:
            "mod_assets/images/cg/splash-glitch.png"
        choice:
            "mod_assets/images/cg/splash-glitch2.png"
    choice:
        pause 0.07
    choice:
        pause 0.1
    choice:
        0.003
    choice:
        0.3

    repeat

# Yuri ghost with transparency
image yuri_ghost_img = "mod_assets/images/bg/club_act2_ghost_yuri_trns.png"
image yuri_ghost_bg = "mod_assets/images/bg/club_act2_ghost_yuri2_trns.png"

screen yuri_ghost:
    zorder 200
    add "yuri_ghost_img" at slow_appear


transform slow_appear:
    alpha 0.0
    easeout 30 alpha 1.0


image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

image flames:
    "mod_assets/images/yuuri_fire/Fire_1.png"
    0.3
    "mod_assets/images/yuuri_fire/Fire_2.png"
    0.3
    "mod_assets/images/yuuri_fire/Fire_3.png"
    0.3
    "mod_assets/images/yuuri_fire/Fire_4.png"
    0.3
    "mod_assets/images/yuuri_fire/Fire_5.png"
    0.3
    "mod_assets/images/yuuri_fire/Fire_6.png"
    0.3
    "mod_assets/images/yuuri_fire/Fire_7.png"
    0.3
    repeat

image flames_mask:
    "mod_assets/images/bg/veinmask.png"
    pause 0.2
    "mod_assets/images/bg/veinmask1.png"
    pause 0.2
    "mod_assets/images/bg/veinmask2.png"
    pause 0.2
    "mod_assets/images/bg/veinmask3.png"
    pause 0.2
    "mod_assets/images/bg/veinmask4.png"
    pause 0.2
    
    repeat

# Character Definitions

# This is where the characters bodies and faces are defined.
# They are defined by left half, right half and their head.

init python:

    def DefineImagesSatori(faces):
        for i in faces:
            if i == "":
                face = "a"
            else:
                face = i
            renpy.image("satori 1"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 2"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 3"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 4"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 5"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 6"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 7"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 8"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 9"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 10"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 11"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1bl.png", (0, 0), "mod_assets/images/satori/1br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 12"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2bl.png", (0, 0), "mod_assets/images/satori/1br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 13"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3bl.png", (0, 0), "mod_assets/images/satori/2br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 14"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4bl.png", (0, 0), "mod_assets/images/satori/3br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 15"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3bl.png", (0, 0), "mod_assets/images/satori/1br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 16"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1bl.png", (0, 0), "mod_assets/images/satori/2br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 17"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4bl.png", (0, 0), "mod_assets/images/satori/1br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 18"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1bl.png", (0, 0), "mod_assets/images/satori/3br.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 19"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1cl.png", (0, 0), "mod_assets/images/satori/1cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 20"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4cl.png", (0, 0), "mod_assets/images/satori/1cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 21"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2cl.png", (0, 0), "mod_assets/images/satori/2cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 22"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3cl.png", (0, 0), "mod_assets/images/satori/3cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 23"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2cl.png", (0, 0), "mod_assets/images/satori/1cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 24"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1cl.png", (0, 0), "mod_assets/images/satori/2cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 25"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3cl.png", (0, 0), "mod_assets/images/satori/1cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))
            renpy.image("satori 26"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1cl.png", (0, 0), "mod_assets/images/satori/3cr.png", (0, 0), "mod_assets/images/satori/"+face+".png"))

    def DefineImagesNatsuko(faces):
        for i in faces:
            if i == "":
                face = "a"
            else:
                face = i
            renpy.image("natsuko 1"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 2"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 3"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 4"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 5"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 6"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 7"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 8"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3bl.png", (0, 0), "mod_assets/images/natsuko/1br.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 9"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1bl.png", (0, 0), "mod_assets/images/natsuko/1br.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 10"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2bl.png", (0, 0), "mod_assets/images/natsuko/1br.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 11"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1bl.png", (0, 0), "mod_assets/images/natsuko/2br.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 12"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3bl.png", (0, 0), "mod_assets/images/natsuko/1br.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))
            renpy.image("natsuko 13"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4b.png", (0, 0), "mod_assets/images/natsuko/"+face+".png"))

    def DefineImagesYuuri(faces):
        for i in faces:
            if i == "":
                face = "a"
            else:
                face = i
            renpy.image("yuuri 1"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 2"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 3"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 4"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 5"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 6"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 7"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 8"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1bl.png", (0, 0), "mod_assets/images/yuuri/1br.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 9"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3bl.png", (0, 0), "mod_assets/images/yuuri/1br.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 10"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2bl.png", (0, 0), "mod_assets/images/yuuri/2br.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 11"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3bl.png", (0, 0), "mod_assets/images/yuuri/2br.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))
            renpy.image("yuuri 12"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4b.png", (0, 0), "mod_assets/images/yuuri/"+face+".png"))

    def DefineImagesMateo(faces):
        for i in faces:
            if i == "":
                face = "a"
            else:
                face = i
            renpy.image("mateo 1"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/"+face+".png"))
            renpy.image("mateo 2"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/"+face+".png"))
            renpy.image("mateo 3"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/"+face+".png"))
            renpy.image("mateo 4"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/"+face+".png"))
            renpy.image("mateo 5"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/"+face+".png"))
            renpy.image("mateo 6"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/"+face+".png"))
            renpy.image("mateo 7"+i,im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/4.png", (-30, 14), "mod_assets/images/mateo/"+face+".png"))

    DefineImagesSatori(["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","aa","ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az","aaa","aab","aac","aad","aae","aaf","aag","aah","aai","aaj","aak","aal","aam","aan","aao","aap","aaq","aar","aas","aat","aau","aav","aaw","aax","aay","aaz"])
    DefineImagesNatsuko(["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","aa","ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az","aaa", "aae","aab","aac","aad"])
    DefineImagesYuuri(["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","aa","ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","y1","y2","y3","y4","y5","y6","y7","y8","aaa","aab","aac","aad","aae","aaf","aag","aah","aai","aaj","aak","aal","aam","aan","aao","aap","aaq","aar","aas","aat","aau","aav","aaw","aax","aay","aaz","at","au","av","aw","ax","ay","az","yandere10","yandere11","yandere12","yandere13","yandere14","yandere15","yandere16","yandere17","yandere18","yandere19","yandere20"])
    DefineImagesMateo(["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","aa","ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az","aaa","aab","aac","aad"])

# Sayori's Definitions

image satori glitch:
    "mod_assets/images/satori/glitch1.png"
    pause 0.01666
    "mod_assets/images/satori/glitch2.png"
    pause 0.01666
    "mod_assets/images/satori/glitch3.png"
    pause 0.01666
    repeat

# natsuko

image natsuko scream = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/scream.png")
image natsuko scream_blood1 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/scream_blood.png")
image natsuko scream_blood2 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/scream_blood2.png")
image natsuko glitcha = im.Composite((960, 960), (0, 0),"mod_assets/images/natsuko/natsuko_ghost_glitch.png")
image natsuko glitchb = im.Composite((960, 960), (0, 0),"mod_assets/images/natsuko/natsuko_ghost_glitch2.png")
image natsuko glitch:
    "mod_assets/images/natsuko/glitch1.png"
    pause 0.1
    "mod_assets/images/natsuko/glitch2.png"
    pause 0.1
    "mod_assets/images/natsuko/glitch3.png"
    repeat

image natsuko ghost_glitch:
    "mod_assets/images/natsuko/natsuko_ghost_glitch.png"
    0.1
    "mod_assets/images/natsuko/natsuko_ghost_glitch2.png"
    0.1
    "natsuko 7g"

image natsuko fight = "mod_assets/images/natsuko/n_fight.png"

    ##############################################
    ############ Natsuko fucking dies ############
    ##############################################


image bleed:
    "mod_assets/images/natsuko_death/bleed_1.png"
    0.07
    "mod_assets/images/natsuko_death/bleed_2.png"
    0.07
    "mod_assets/images/natsuko_death/bleed_3.png"
    0.07
    "mod_assets/images/natsuko_death/bleed_4.png"
    0.07
    "mod_assets/images/natsuko_death/bleed_5.png"
    0.07
    "mod_assets/images/natsuko_death/bleed_6.png"
    0.07
    repeat

image natsuko_drip:
    "mod_assets/images/natsuko_death/drip_1.png"
    0.07
    "mod_assets/images/natsuko_death/drip_2.png"
    0.07
    "mod_assets/images/natsuko_death/drip_3.png"
    0.07
    "mod_assets/images/natsuko_death/drip_4.png"
    0.07
    repeat


image natsuko_stabby:
    "mod_assets/images/natsuko_death/stab_1.png"
    0.07
    "mod_assets/images/natsuko_death/stab_2.png"
    0.07
    "mod_assets/images/natsuko_death/stab_3.png"
    0.07
    "mod_assets/images/natsuko_death/stab_4.png"
    0.07
    "mod_assets/images/natsuko_death/stab_5.png"
    0.07
    alpha 0


image satori kill1 = "mod_assets/images/natsuko_death/s_kill1.png"
image satori kill2 = "mod_assets/images/natsuko_death/s_kill2.png"

image natsuko death1 = "mod_assets/images/natsuko_death/nat_death_sprite1.png"
image natsuko death2 = "mod_assets/images/natsuko_death/nat_death_sprite2.png"
# yuuri

image yuuri glitch:
    "mod_assets/images/yuuri/glitch1.png"
    pause 0.1
    "mod_assets/images/yuuri/glitch2.png"
    pause 0.1
    "mod_assets/images/yuuri/glitch3.png"
    repeat

image yuuri fight = "mod_assets/images/yuuri/y_fight.png"
image yuuri crazy = "mod_assets/images/yuuri/eyes_full2.png"

image yuuri glitch:
    parallel:
        choice:
            "mod_assets/images/yuuri/yuuri_glitch.png"
        choice:
            "mod_assets/images/yuuri/yuuri_glitch2.png"
    pause 0.2
    repeat

image yuuri ligther:
    "mod_assets/images/yuuri_fire/yuuri_lighter.png"
    1
    "mod_assets/images/yuuri_fire/yuuri_lighter_flame1.png"
    0.3
    block:
        "mod_assets/images/yuuri_fire/yuuri_lighter_flame2.png"
        0.3
        "mod_assets/images/yuuri_fire/yuuri_lighter_flame3.png"
        0.3
        "mod_assets/images/yuuri_fire/yuuri_lighter_flame4.png"
        0.3
        repeat

image giga_yuuri = "mod_assets/images/yuuri/giga_yuuri.png"


# Mateo the Douchebag

image mateo glitch:
    "mod_assets/images/mateo/glitch1.png"
    pause 0.1
    "mod_assets/images/mateo/glitch2.png"
    pause 0.1
    "mod_assets/images/mateo/glitch3.png"
    repeat

image femc 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/b.png")
image femc 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/c.png")
image femc 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/d.png")
image femc 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/e.png")
image femc 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/f.png")
image femc 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/g.png")
image femc 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/h.png")
image femc 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/i.png")
image femc 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/j.png")

image femc 2 = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 2a = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 2b = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/b.png")
image femc 2c = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/c.png")
image femc 2d = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/d.png")
image femc 2e = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/e.png")
image femc 2f = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/f.png")
image femc 2g = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/g.png")
image femc 2h = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/h.png")
image femc 2i = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/i.png")
image femc 2j = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/j.png")

image femc 3 = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 3a = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 3b = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/b.png")
image femc 3c = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/c.png")
image femc 3d = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/d.png")
image femc 3e = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/e.png")
image femc 3f = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/f.png")
image femc 3g = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/g.png")
image femc 3h = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/h.png")
image femc 3i = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/i.png")
image femc 3j = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/2l.png", (0, 0), "mod_assets/images/femc/1r.png", (0, 0), "mod_assets/images/femc/j.png")

image femc 4 = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 4a = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/a.png")
image femc 4b = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/b.png")
image femc 4c = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/c.png")
image femc 4d = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/d.png")
image femc 4e = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/e.png")
image femc 4f = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/f.png")
image femc 4g = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/g.png")
image femc 4h = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/h.png")
image femc 4i = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/i.png")
image femc 4j = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/1l.png", (0, 0), "mod_assets/images/femc/2r.png", (0, 0), "mod_assets/images/femc/j.png")

image femc 5 = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/a.png")
image femc 5a = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/a.png")
image femc 5b = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/b.png")
image femc 5c = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/c.png")
image femc 5d = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/d.png")
image femc 5e = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/e.png")
image femc 5f = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/f.png")
image femc 5g = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/g.png")
image femc 5h = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/h.png")
image femc 5i = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/i.png")
image femc 5j = im.Composite((960, 960), (0, 0), "mod_assets/images/femc/3.png", (0, 0),"mod_assets/images/femc/j.png")

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', image='femc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='satori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='mateo', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuko', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define u = Character('???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

# Persistent Variables

# These variables are load at game startup and exist on all saves.
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

# Other Persistent Variables
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Satori"
default m_name = "Mateo"
default n_name = "Natsuko"
default y_name = "Yuuri"

# Poem Variables
# This is how much each character likes your poem day by day
# -1 - Bad, 0 - Neutral, 1 - Good
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem game
default poemwinner = ['sayori', 'sayori', 'sayori']

# This keeps track on who already read your poem
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This stores how many poems you read so far.
default poemsread = 0

# This stores who likes your poem the most.
# This controls which exclusive scene you will get each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# Tracks whether we watched Natsuki's and Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# Tracks whether Yuri runs away after the first exclusive scene of Act 2
default y_gave = False
default y_ranaway = False

# Tracks if we get to Natsuki's and Yuri's third poem
default n_read3 = False
default y_read3 = False

# Tracks who we chose to side with in Chapter 1
default ch1_choice = "sayori"

default n_poemearly = False

# Tracks whether we wanted to help Sayori and/or Monika
default help_sayori = None
default help_monika = None

# Tracks who we chose to spend time with in Chapter 4
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# Tracks if we accepted Sayori's Confession
default sayori_confess = True

# We read Natsuki's third poem in Chapter 23
default natsuki_23 = None

default persistent.efuse = False

default played_sound = False # For the flesh eating sound
