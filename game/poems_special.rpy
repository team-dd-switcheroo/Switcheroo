# Poem_special.rpy

# This defines the special poems that the player might be shown to the player
# Only three poems are ever shown to the player, at random

image poem_special_arm = "mod_assets/images/poem_special/special_poem1_mat_run.png" # A Riddle (Mateo Edition)
image poem_special_an = "mod_assets/images/poem_special/special_poem2_both.png" # A Nightmare
image poem_special_a4m = "mod_assets/images/poem_special/poem_special5_both.png" # Anything for mother
image poem_special_dyr = "mod_assets/images/poem_special/special_poem7_both.png" # FeMC diary page
image poem_special_dyr_y = "mod_assets/images/poem_special/poem_special6_both.png" # Yuuri diary page
image poem_special3 = "poem_special/poem_special3.png" # Nothing is Real
image poem_special4 = "poem_special/poem_special4.png" # Cutting Memento
image poem_special5: # Stare at the dot/I love you
    "poem_special/poem_special5a.png"
    10.0
    "poem_special/poem_special5b.png"
image poem_special6 = "poem_special/poem_special6.png" # A Joke
image poem_special7a = "poem_special/poem_special7a.png"
image poem_special7b = "poem_special/poem_special7b.png"
image poem_special8 = "poem_special/poem_special8.png" # A Dream
image poem_special9 = "poem_special/poem_special9.png" # Things I Like About Papa
image poem_special10 = "poem_special/poem_special10.png" # Go to Therapy
image poem_special11 = "poem_special/poem_special11.png" # A Dream 2

# Ending Poem where we can either get Monika's or Dan's Final Poem
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

# All of these define a label for showing a poem
label poem_special_1:
    $ quick_menu = False
    play sound page_turn
    show poem_special1 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_2:
    $ quick_menu = False
    play sound page_turn
    show poem_special2 with Dissolve(1.0)
    $ pause()
    play sound "sfx/giggle.ogg"
    $ quick_menu = True
    return
label poem_special_3:
    $ quick_menu = False
    play sound page_turn
    show poem_special3 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_4:
    $ quick_menu = False
    play sound page_turn
    show poem_special4 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_5:
    $ quick_menu = False
    play sound page_turn
    show poem_special5 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_6:
    $ quick_menu = False
    play sound page_turn
    show poem_special6 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_7:
    $ quick_menu = False
    play sound page_turn
    show poem_special7a as ps with Dissolve(1.0)
    $ pause()
    show poem_special7b as ps
    $ pause(0.01)
    $ quick_menu = True
    return
label poem_special_8:
    $ quick_menu = False
    play sound page_turn
    show poem_special8 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_9:
    $ quick_menu = False
    play sound page_turn
    show poem_special9 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_10:
    $ quick_menu = False
    play sound page_turn
    show poem_special10 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_11:
    $ quick_menu = False
    play sound page_turn
    show poem_special11 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_arm:
    $ quick_menu = False
    play sound page_turn
    show poem_special_arm with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_an:
    $ quick_menu = False
    play sound page_turn
    show poem_special_an with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return

label poem_special_a4m:
    $ quick_menu = False
    play sound page_turn
    show poem_special_a4m with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return

label poem_special_dyr:
    $ quick_menu = False
    play sound page_turn
    show poem_special_dyr with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_dyr_y:
    $ quick_menu = False
    play sound page_turn
    show poem_special_dyr_y at truecenter with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
