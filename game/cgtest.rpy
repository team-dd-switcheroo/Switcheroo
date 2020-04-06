label cgtest:
    scene bg Fmbedroom
    with wipeleft_scene
    stop music fadeout 2.0
    show satori 11av at t41
    show blood_eye zorder 3:
        pos (758,516) zoom 2.5
    $ pause(3.75)
    hide blood_eye
    return