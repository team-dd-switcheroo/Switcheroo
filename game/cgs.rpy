## cgs.rpy

# This defines all Character Graphics (CGs) in DDLC
# such as Yuri Chocolate CG and Natsuki Manga CG.

# Use this as a base if you want to override the CGs from DDLC with your own.

## Yuri Chocolate CG

# Feeding Yuuri Chocolate
# This is the slowly fading background
# image y_cg2_bg:
#     "mod_assets/images/cg/y_cg2_bg1.png"
#     6.0
#     "mod_assets/images/cg/y_cg2_bg2.png" with Dissolve(1)
#     2
#     "mod_assets/images/cg/y_cg2_bg1.png" with Dissolve(1)
#     1
#     repeat

#Yuri's Face
image y_cg2_base:
    "mod_assets/images/cg/y_cg2_base.png"
image y_cg2_nochoc:
    "mod_assets/images/cg/y_cg2_exp2.png"
    on hide:
        linear 0.5 alpha 0

# Animated Details to Yuri's CG
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

# Expressions

# Surprised Yuri
image y_cg2_exp1:
    "mod_assets/images/cg/y_cg2_exp1.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_exp2:
    "mod_assets/images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Embarrassed Yuri
image y_cg2_exp3:
    "mod_assets/images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_exp4:
    "mod_assets/images/cg/y_cg2_exp4.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_exp5:
    "mod_assets/images/cg/y_cg2_exp5.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_exp6:
    "mod_assets/images/cg/y_cg2_exp6.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_exp7:
    "mod_assets/images/cg/y_cg2_exp7.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_exp8:
    "mod_assets/images/cg/y_cg2_exp8.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Particles during Yuri CG
image y_cg2_dust1:
    "mod_assets/images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust2:
    "mod_assets/images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust3:
    "mod_assets/images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "mod_assets/images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

## Natsuko Reading Fiction CG

# Background/Base
image n_cg1_bg:
    "mod_assets/images/cg/n_cg1_bg.png"
image n_cg1_base:
    "mod_assets/images/cg/natsuko_cg1.png"

# Expressions

# Happy Natsuko
image n_cg1_exp1:
    "mod_assets/images/cg/natsuko_cg4.png"
# Smirk Natsuko
image n_cg1_exp2:
    "mod_assets/images/cg/natsuko_cg2.png"
# Huh?
image n_cg1_exp3:
    "mod_assets/images/cg/natsuko_cg3.png"

# Glitched Natsuki CG
image n_cg1b = LiveComposite((1280,720), (0,0), "images/cg/n_cg1b.png", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

## Natsuko Reading Fiction Act 2

image n_act2_cg1_bg:
    "mod_assets/images/cg/n_cg1_bg_act2.png"

image n_act2_cg1_exp1:
    "mod_assets/images/cg/nat act11 day1 cg1.png"

image n_act2_cg1_exp2:
    "mod_assets/images/cg/nat act11 day1 cg2.png"

image n_act2_cg1_exp3:
    "mod_assets/images/cg/nat act11 day1 cg3.png"

image n_act2_cg1_exp4:
    "mod_assets/images/cg/nat act11 day1 cg4.png"

image n_act2_cg1_exp5:
    "mod_assets/images/cg/nat act11 day1 cg5.png"

image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    size (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    size (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    size (30, 20)

# Natsuko Closet CG

# Closet Background
image n_cg2_bg:
    "mod_assets/images/cg/n_cg2_bg.png"
# Natsuki herself
image natsuko_bg_cgbase2:
    "mod_assets/images/cg/natsuko_bg_cgbase2.png"
# Surprised Natsuki
image natsuko_bg_cg2_exp1:
    "mod_assets/images/cg/natsuko_bg_cg2_exp1.png"
# Shouting Natsuki
image natsuko_bg_cg2_exp2:
    "mod_assets/images/cg/natsuko_bg_cg2_exp2.png"
image natsuko_bg_cg2_exp3:
    "mod_assets/images/cg/natsuko_bg_cg2_exp3.png"

# Natsuko Wall CG
# Cake on Face
image n_cg3_base:
    "mod_assets/images/cg/natsuko weekend_cg1.png"
# Embaressed
image n_cg3_exp1:
    "mod_assets/images/cg/natsuko weekend_cg2.png"
# Smirk
image n_cg3_exp2:
    "mod_assets/images/cg/natsuko weekend_cg3.png"
# ...Thirsty?
image n_cg3_exp3:
    "mod_assets/images/cg/natsuko weekend_cg4.png"

# Yuuri Readtime CG

# Base Image with Yuri and Classroom
image y_cg1_base:
    "mod_assets/images/cg/yuuri_cg_bg.png"

# Expressions

# Side-eye at MC/Camera
image y_cg1_exp1:
    "mod_assets/images/cg/yuuri_cg1.png"

# Talking
image y_cg1_exp2:
    "mod_assets/images/cg/yuuri_cg2.png"

# Ooh? Huh?
image y_cg1_exp3:
    "mod_assets/images/cg/yuuri_cg3.png"

# Uh... Worried Yuuri
image y_cg1_exp4:
    "mod_assets/images/cg/yuuri_cg4.png"

# Hide Blush Yuuri
image y_cg1_exp5:
    "mod_assets/images/cg/yuuri_cg5.png"

# Act 2

# Side-eye at MC/Camera
image y_act2_day1_cg1:
    "mod_assets/images/cg/y_act2_day1_cg1.png"

# Smiling
image y_act2_day1_cg2:
    "mod_assets/images/cg/y_act2_day1_cg2.png"

# Uh... Worried Yuuri
image y_act2_day1_cg3:
    "mod_assets/images/cg/y_act2_day1_cg3.png"

# Ooh? Huh?
image y_act2_day1_cg4:
    "mod_assets/images/cg/y_act2_day1_cg4.png"

# Blush Yuuri
image y_act2_day1_cg5:
    "mod_assets/images/cg/y_act2_day1_cg5.png"

# Hide Blush Yuuri
image y_act2_day1_cg6:
    "mod_assets/images/cg/y_act2_day1_cg6.png"

# Yuuri MC Room CG
image y_cg3_base:
    "mod_assets/images/cg/y_cg3_base.png"

image y_cg3_exp1:
    "mod_assets/images/cg/y_cg3a_base.png"

# Satori Blazer CG
image s_cg1_base:
    "mod_assets/images/cg/closet_wall.png"

# Awkward
image s_cg1_exp1:
    "mod_assets/images/cg/satori_cg1.png"

# Nervous/Ehehe...
image s_cg1_exp2:
    "mod_assets/images/cg/satori_cg2.png"

# Upset Satori
image s_cg1_exp3:
    "mod_assets/images/cg/satori_cg3.png"

# Uh... Worried Satori
image s_cg1_exp4:
    "mod_assets/images/cg/satori_cg4.png"

# Hide Blush Satori
image s_cg1_exp5:
    "mod_assets/images/cg/satori_cg5.png"

image s_cg2_base:
    "mod_assets/images/cg/s_cg2_base.png"
image s_cg2_exp1:
    "mod_assets/images/cg/s_cg2_exp1.png"
image s_cg2_exp2:
    "mod_assets/images/cg/s_cg2_exp2.png"
image s_cg2_exp3:
    "mod_assets/images/cg/s_cg2_exp3.png"
image s_cg2_exp4:
    "mod_assets/images/cg/s_cg2_exp4.png"

# Satori Hug CG
image s_cg3_base:
    "mod_assets/images/cg/satori weekend cg1.png"
image s_cg3_exp1:
    "mod_assets/images/cg/satori weekend cg2.png"
image s_cg3_exp2:
    "mod_assets/images/cg/satori weekend cg3.png"
image s_cg3_exp3:
    "mod_assets/images/cg/satori weekend cg4.png"

# Mateo Suicide CG

# Sayori Room BG (Normal Lighting)
image m_kill:
    subpixel True
    "mod_assets/images/cg/mateo death cg.png"

# Sayori Hanging Sprite
image m_kill2:
    subpixel True
    "mod_assets/images/cg/mateo death cg2.png"

# Glitch Lighting
image m_kill3:
    subpixel True
    "mod_assets/images/cg/mateo death cg3.png"

# Glitch Lighting with Sayori Hanging Sprite
image m_kill4:
    subpixel True
    "mod_assets/images/cg/mateo glitch death cg.png"

image m_kill5:
    subpixel True
    "mod_assets/images/cg/mateo saturated death cg.png"

# The One and Only Mateo CG I think
image m_cg1_base:
    "mod_assets/images/cg/mateo_cg1.png"

image m_cg1_exp1:
    "mod_assets/images/cg/mateo_cg2.png"

image m_cg1_exp2:
    "mod_assets/images/cg/mateo_cg3.png"

image m_cg1_exp3:
    "mod_assets/images/cg/mateo_cg4.png"

image m_cg1_exp4:
    "mod_assets/images/cg/mateo_cg5.png"

image m_cg1_exp5:
    "mod_assets/images/cg/mateo_cg6.png"

image m_cg1_exp6:
    "mod_assets/images/cg/mateo_cg7.png"

image m_cg1_exp7:
    "mod_assets/images/cg/mateo_cg8.png"

image m_cg1_exp8:
    "mod_assets/images/cg/mateo_cg9.png"

image m_cg1_exp9:
    "mod_assets/images/cg/mateo_cg10.png"

# The actual death sequence
image s_kill:
    subpixel True
    "mod_assets/images/cg/satori_death_cg.png"

# Sayori Hanging Sprite
image s_kill2:
    subpixel True
    "mod_assets/images/cg/satori_death_cg2.png"

image s_kill3:
    subpixel True
    "mod_assets/images/cg/satori_death_cg3.png"

image s_kill4:
    subpixel True
    "mod_assets/images/cg/satori_death_cg3_noise.png"

image s_kill5:
    subpixel True
    "mod_assets/images/cg/satori_glitch1.png"
    
image s_kill6:
    subpixel True
    "mod_assets/images/cg/satori_glitch2.png"

image s_kill7:
    subpixel True
    "mod_assets/images/cg/satori_saturated_death_cg.png"

# Yuri Stab CG
# This is displayed using a ConditionSwitch to switch between
# different Yuri stab images
image y_kill = ConditionSwitch(
    "persistent.yuri_kill >= 1380", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 1180", "images/cg/y_kill/3c.png",
    "persistent.yuri_kill >= 1120", "images/cg/y_kill/3b.png",
    "persistent.yuri_kill >= 920", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 720", "images/cg/y_kill/2c.png",
    "persistent.yuri_kill >= 660", "images/cg/y_kill/2b.png",
    "persistent.yuri_kill >= 460", "images/cg/y_kill/2a.png",
    "persistent.yuri_kill >= 260", "images/cg/y_kill/1c.png",
    "persistent.yuri_kill >= 200", "images/cg/y_kill/1b.png",
    "True", "images/cg/y_kill/1a.png",

    )

# Animations for Sayori Hanging CG
transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
