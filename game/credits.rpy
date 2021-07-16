# Credits.rpy

# This controls the ending of DDLC and your mod!

# Use this as a starting point if want to override this with your own.

# Import the datetime python library to calculate time.
init python:
    import datetime

# This defines the CGs that are deleted after a few seconds.
# These are the color CGs that are used in the base game.
image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)


image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)


image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)


image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)


image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)


image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)


image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)


image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)


image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)


# These are the CGs that have not been seen (grayed-out)
# image credits_cg1_locked:
#     "images/cg/credits/1b.png"
#     size (640, 360)

image credits_cg1_locked:
    LiveComposite((1280,720),
    (0, 0), im.Grayscale("mod_assets/images/cg/n_cg1_bg.png"),
    (0, 0), im.Grayscale("mod_assets/images/cg/natsuko_cg1.png"))
    size (640, 360)




image credits_cg2_locked:
    im.Grayscale("mod_assets/images/cg/natsuko_bg_cg2_exp1.png")
    size (640, 360)


image credits_cg3_locked:
    LiveComposite((1280,720),
    (0, 0), im.Grayscale("mod_assets/images/cg/yuuri_cg_bg.png"),
    (0, 0), im.Grayscale("mod_assets/images/cg/yuuri_cg1.PNG"))
    size (640, 360)


image credits_cg4_locked:
    im.Grayscale("mod_assets/images/cg/y_cg2_exp1.png")
    size (640, 360)


image credits_cg5_locked:
    im.Grayscale("mod_assets/images/cg/natsuko weekend_cg1.png")
    size (640, 360)


image credits_cg6_locked:
    im.Grayscale("mod_assets/images/cg/y_cg3_base.png")
    size (640, 360)


image credits_cg7_locked:
    LiveComposite((1280,720),
    (0, 0), im.Grayscale("mod_assets/images/cg/closet_wall.png"),
    (0, 0), im.Grayscale("mod_assets/images/cg/satori_cg1.png"))
    size (640, 360)


image credits_cg8_locked:
    im.Grayscale("mod_assets/images/cg/s_cg2_base.png")
    size (640, 360)


image credits_cg9_locked:
    im.Grayscale("mod_assets/images/cg/satori weekend cg1.png")
    size (640, 360)


image credits_cg10_locked:
    im.Grayscale("mod_assets/images/satori_void/sat_void_tears2_scream1.png")
    size (640, 360)


# This defines the CG's that are not removed
# if the user gets a perfect ending (100% Completion)
image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size (640, 360)

# DDLC Logo
image credits_logo:
    "/mod_assets/GUI/modLogo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    1.5
    linear 2.0 alpha 0

# Team Salvato Logo
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# Style fonts for the credits
style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_header_med = ParameterizedText(style="credits_header", ypos=-60)
image credits_header_big = ParameterizedText(style="credits_header", ypos=-80)
image credits_header_big2 = ParameterizedText(style="credits_header", ypos=-90)
image credits_header_xtrabig = ParameterizedText(style="credits_header", ypos=-100)
image credits_header_xxtrabig = ParameterizedText(style="credits_header", ypos=-205)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image credits_text_big = ParameterizedText(style="credits_text", ypos=5)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)
image title = ParameterizedText(style="credits_header", xalign=0.5)

# Credit animations to make the credits and images move.
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_center:
    xalign 0.5
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250


# This is where the credit scroll starts
label credits:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
    scene black
    $ consolehistory = []
    play music td
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 4.58
    show title "Based on Doki Doki Literature club by Dan Salvato" as title at credits_scroll_center
    pause 2
    # Each CG appears. If it has not been seen, it is grayed out. If it's
    # not a perfect ending, the CG images are deleted after a few seconds
    $ lockedtext = "_locked"
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    
    # Actual names for Credits, where you plug in stuff
    
    show credits_header "Written By" as credits_header2 at credits_text_scroll_left
    show credits_text "MW Roach" as credits_text_2 at credits_text_scroll_left


    
    $ lockedtext = "_locked"
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    
    show credits_header "Proofreading" as credits_header_1 at credits_text_scroll_right
    show credits_text "Tormuse" as credits_text_1 at credits_text_scroll_right

    $ lockedtext = "_locked"
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    

    show credits_header_med "Sprites, Menu Art & Chibis" as credits_header_2 at credits_text_scroll_left
    show credits_text "Yagamirai10\nPlyesdayk\nBlackRabbitArtworks\nSoldat" as credits_text_2 at credits_text_scroll_left
    

    
    $ lockedtext = "_locked"
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    
    show credits_header_big "Background Art" as credits_header_1 at credits_text_scroll_right
    show credits_text "Velinquent\nDarkSnyder76\nCyrke\nKimagure After!\nPlyesdayk" as credits_text_1 at credits_text_scroll_right
    
    $ lockedtext = "_locked"
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    
    show credits_header "CGs" as credits_header_2 at credits_text_scroll_left
    show credits_text "Plyesdayk\nFabuwhatsoeverFox\nCeridwenArt" as credits_text_2 at credits_text_scroll_left
    
    $ lockedtext = "_locked"
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    
    show credits_header_big2 "Music & Audio" as credits_header_1 at credits_text_scroll_right
    show credits_text "Dan Salvato\nJellio\nNumsOic\nMetrid Siardily\nGanstaofSA\nFreeSound.org" as credits_text_1 at credits_text_scroll_right

    
    $ lockedtext = "_locked"
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    
    show credits_header_xxtrabig "Coding" as credits_header_2 at credits_text_scroll_left
    show credits_text_big "GanstaofSA\nBigBoss\nGalo\nKarasil Sothren\nCorrupt\nCPG Yuri\nGoodfaithyuki\nSlightlySimple\nMW Roach" as credits_text_2 at credits_text_scroll_left
    
    $ lockedtext = "_locked"
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    
    show credits_header_xtrabig "Playtesters" as credits_header_1 at credits_text_scroll_right
    show credits_text "MW Roach\nCode.Zero\nWhispereon\nRemember4Ender\nMochu\nGantsaofSA" as credits_text_1 at credits_text_scroll_right

    
    # show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "_locked"
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    
    show credits_header "Voice Acting" as credits_header_2 at credits_text_scroll_left
    show credits_text "Mewtwo Riley" as credits_text_2 at credits_text_scroll_left
    
    $ lockedtext = "_locked"

    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())

    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_right
    show credits_text "Mateo" as credits_text_1 at credits_text_scroll_right
    
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())


    # Don't know what to add past the credits scroll so leaving it like this

    return

    
    # if not persistent.clearall:
    #     call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
    # else:
    #     call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")

    # call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
    # call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
    # call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
    # call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
    # $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    
    # Hides console and shows the Team Salvato Logo/Thank You
    # call hideconsole
    # show credits_ts
    # show credits_text "made with love by":
    #     zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
    #     linear 2.0 alpha 1
    #     4.5
    #     linear 2.0 alpha 0
    # pause 9.3
    # play sound page_turn
    # show poem_end with Dissolve(1)

    # Fade to black and make the player quit
    # label postcredits_loop:
    #     # Game reloads to the postcredits_loop
    #     $ persistent.autoload = "postcredits_loop"

    #     # Disables Main Menu, Quick Menu, Everything
    #     $ config.keymap['game_menu'] = []
    #     $ config.keymap['hide_windows'] = []
    #     $ renpy.display.behavior.clear_keymap_cache()
    #     $ quick_menu = False
    #     $ config.skipping = False
    #     $ config.allow_skipping = False

    #     # Fade to black
    #     scene black

    #     # Shows either Monika's or Dan's Goodbye Message
    #     show poem_end
    #     $ pause()
        
    #     # Fakes Error Corruption. Makes the player quit the game.
    #     call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    #     return
