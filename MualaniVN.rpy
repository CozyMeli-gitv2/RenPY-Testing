# the letter after define is the shortcut for when i call upon it
# within quotations put the name that appears.


define M = Character("Mualani", color="#FF69B4", window_background="gui/textbox_mualani.png")


image bg natlan = "bg_natlan.png"
image bg natlan_shop = "bg_natlan_shop.png"
image mualani chibi = "mualani_chibi.png"
image mualani chibi surfboard = "mualani_chibi_surfboard.png"

# LINK START

label start:

    play music "genshin_ost_tribe.mp3"

    scene bg natlan with fade


    show mualani chibi at center with dissolve
    M "Hey traveler! My name is Mualani, a member of the people of the springs!"
    M "I don't think you've met me before!"
    M "forgor"

   
    hide mualani chibi with dissolve
    show mualani chibi surfboard at center with moveinleft

    M "placeholder"
    M "placeholder"

    hide mualani chibi surfboard with dissolve

    show mualani chibi at center with dissolve

    M "Now, let me take you to my shop where I work.. sometimes!"

    play music "genshin_ost_shop.mp3"
    scene bg natlan_shop with wipeleft

    show mualani chibi at center with dissolve

    M "Welcome to my shop!."


    return
